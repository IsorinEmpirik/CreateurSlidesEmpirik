#!/usr/bin/env python3
"""
fetch_logos.py · Recuperer les logos officiels de marques/outils.

Strategie en 3 couches (fallback automatique) :
  1. simpleicons.org CDN (SVG vectoriel) · pour marques tech populaires
  2. Wikipedia Commons API (iiurlwidth · PNG serveur-rendu) · pour marques connues
  3. Scraping HTML officiel (apple-touch-icon / og:image / icon-png) · pour marques de niche

Usage :
  python scripts/fetch_logos.py \
    --simpleicons openai cloudflare perplexity googleanalytics \
    --wikipedia "ChatGPT-Logo.svg=openai" "Bing_Fluent_Logo_Text.svg=bing" \
    --scrape "https://www.dispano.fr/=dispano" "https://www.egger.com/=egger"

Toutes les images vont dans assets/logos/. Si une cible existe deja en PNG valide,
elle est skip (cache).
"""
import argparse, urllib.request, urllib.parse, json, re, time, sys
from pathlib import Path

LOGOS_DIR = Path('assets/logos')
LOGOS_DIR.mkdir(parents=True, exist_ok=True)

UA_LIST = [
    {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'},
    {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:121.0) Gecko/20100101 Firefox/121.0', 'Referer': 'https://www.google.com/'},
    {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Safari/605.1.15', 'Referer': 'https://duckduckgo.com/'},
]

def fetch(url, timeout=20, decode=False):
    """Fetch avec rotation User-Agent si 403/blocked."""
    last_exc = None
    for headers in UA_LIST:
        try:
            req = urllib.request.Request(url, headers=headers)
            data = urllib.request.urlopen(req, timeout=timeout).read()
            return data.decode('utf-8', 'ignore') if decode else data
        except urllib.error.HTTPError as e:
            last_exc = e
            if e.code in (403, 429):
                continue  # try next UA
            raise
        except Exception as e:
            last_exc = e
            raise
    if last_exc:
        raise last_exc

def is_valid_png(path):
    if not path.exists() or path.stat().st_size < 1000:
        return False
    with open(path, 'rb') as f:
        return f.read(8).startswith(b'\x89PNG')

def absolutize(base, href):
    if href.startswith('http'): return href
    if href.startswith('//'): return 'https:' + href
    if href.startswith('/'):
        from urllib.parse import urlparse
        u = urlparse(base)
        return f"{u.scheme}://{u.netloc}{href}"
    return base.rstrip('/') + '/' + href

# === Layer 1 : simpleicons CDN ===========================================
def fetch_simpleicons(slug, dst_name, color="0A3856"):
    """Renvoie SVG (a convertir manuellement en PNG via outils tiers)."""
    out = LOGOS_DIR / f"{dst_name}.svg"
    try:
        data = fetch(f"https://cdn.simpleicons.org/{slug}/{color}")
        if data and b'<svg' in data[:200]:
            out.write_bytes(data)
            return True, f"simpleicons '{slug}'"
    except Exception as e:
        return False, f"simpleicons '{slug}': {e}"
    return False, f"simpleicons '{slug}': no SVG"

# === Layer 2 : Wikipedia Commons via API ================================
def fetch_wikipedia(filename, dst_name, width=400):
    """Wikipedia API rend le SVG en PNG cote serveur (haute resolution)."""
    out = LOGOS_DIR / f"{dst_name}.png"
    if is_valid_png(out):
        return True, "cached"
    try:
        api = ("https://commons.wikimedia.org/w/api.php"
               "?action=query&format=json&prop=imageinfo&iiprop=url"
               f"&iiurlwidth={width}&titles=File:{urllib.parse.quote(filename)}")
        data = json.loads(fetch(api))
        for pid, page in data['query']['pages'].items():
            if int(pid) < 0:
                return False, f"file '{filename}' not found"
            if 'imageinfo' not in page:
                continue
            thumb_url = page['imageinfo'][0].get('thumburl') or page['imageinfo'][0].get('url')
            if not thumb_url:
                return False, "no URL in API response"
            png_data = fetch(thumb_url)
            if png_data[:8].startswith(b'\x89PNG'):
                out.write_bytes(png_data)
                return True, f"Wikipedia '{filename}'"
            else:
                # may be SVG or other · save as appropriate ext
                ext = '.svg' if b'<svg' in png_data[:200] else '.bin'
                out.with_suffix(ext).write_bytes(png_data)
                return True, f"Wikipedia '{filename}' (non-PNG)"
    except Exception as e:
        return False, f"Wikipedia '{filename}': {str(e)[:80]}"

# === Layer 3 : Scraping HTML officiel (avec persistance multi-pages) ====
def fetch_official_site(site_url, dst_name):
    """Extrait logo depuis HTML : apple-touch-icon, og:image, icon-png,
    puis fallback agressif sur <img class='logo'>, <svg id='logo'>,
    pages /press, /brand, /media, /about."""
    out = LOGOS_DIR / f"{dst_name}.png"
    if is_valid_png(out):
        return True, "cached"

    # Pages à crawler dans l'ordre (la home en 1er, puis les pages spécifiques)
    base = site_url.rstrip('/')
    pages_to_try = [
        site_url,
        f"{base}/press", f"{base}/press-kit", f"{base}/media",
        f"{base}/media-kit", f"{base}/brand", f"{base}/brand-assets",
        f"{base}/about", f"{base}/about-us", f"{base}/qui-sommes-nous",
    ]

    all_candidates = []
    for page_url in pages_to_try:
        try:
            html = fetch(page_url, decode=True)
        except Exception:
            continue  # page n'existe pas, on passe

        # 1. apple-touch-icon (180x180 PNG HD)
        for m in re.finditer(r'<link[^>]+(?:rel=["\'](apple-touch-icon[^"\']*?)["\'][^>]+href=["\']([^"\']+)["\']|href=["\']([^"\']+)["\'][^>]+rel=["\']apple-touch-icon)', html, re.I):
            href = m.group(2) or m.group(3)
            all_candidates.append(('apple-touch-icon', absolutize(page_url, href)))
        # 2. og:image
        m = re.search(r'<meta[^>]+property=["\']og:image["\'][^>]+content=["\']([^"\']+)["\']', html, re.I)
        if m:
            all_candidates.append(('og:image', absolutize(page_url, m.group(1))))
        # 3. icon PNG
        m = re.search(r'<link[^>]+rel=["\']icon["\'][^>]+type=["\']image/png["\'][^>]+href=["\']([^"\']+)["\']|<link[^>]+type=["\']image/png["\'][^>]+rel=["\']icon["\'][^>]+href=["\']([^"\']+)["\']', html, re.I)
        if m:
            href = m.group(1) or m.group(2)
            all_candidates.append(('icon-png', absolutize(page_url, href)))
        # 4. <img> avec class/alt/src contenant "logo" (fallback aggressif)
        for m in re.finditer(r'<img[^>]+(?:class|alt|src)=["\'][^"\']*logo[^"\']*["\'][^>]*>', html, re.I):
            img_tag = m.group(0)
            src_match = re.search(r'src=["\']([^"\']+)["\']', img_tag, re.I)
            if src_match:
                src = src_match.group(1)
                if src.endswith(('.png', '.svg', '.jpg', '.jpeg', '.webp')):
                    all_candidates.append(('img-logo', absolutize(page_url, src)))
        # 5. <a> ou <div> avec class "logo" contenant un <img>
        for m in re.finditer(r'<(?:a|div|span)[^>]+class=["\'][^"\']*logo[^"\']*["\'][^>]*>.*?<img[^>]+src=["\']([^"\']+)["\']', html, re.I | re.DOTALL):
            all_candidates.append(('img-in-logo-container', absolutize(page_url, m.group(1))))
        # 6. liens de téléchargement explicites (/logo.png, /brand.svg…) dans le HTML
        for m in re.finditer(r'href=["\']([^"\']+(?:logo|brand)[^"\']*\.(?:png|svg|zip))["\']', html, re.I):
            all_candidates.append(('download-link', absolutize(page_url, m.group(1))))

    # Dédupliquer en gardant l'ordre
    seen = set()
    candidates = []
    for kind, url in all_candidates:
        if url not in seen:
            seen.add(url)
            candidates.append((kind, url))

    if not candidates:
        return False, f"no candidate found across {len(pages_to_try)} pages"

    for kind, url in candidates:
        try:
            data = fetch(url)
            if len(data) < 500:
                continue
            if data[:8].startswith(b'\x89PNG'):
                ext = '.png'
            elif data[:3] == b'\xff\xd8\xff':
                ext = '.jpg'
            elif b'<svg' in data[:200]:
                ext = '.svg'
            else:
                continue
            out.with_suffix(ext).write_bytes(data)
            return True, f"{kind} from {url}"
        except Exception:
            continue
    return False, f"no candidate worked across {len(pages_to_try)} pages ({len(candidates)} candidates tried)"

# === Layer 4 : Brandfetch.com API (fallback pour sites 403/Cloudflare) ===
def fetch_brandfetch(domain, dst_name):
    """Récupère le logo via l'API publique brandfetch.com.
    Utile pour les domaines qui bloquent le scraping HTML (Cloudflare, 403...).
    `domain` = ex. 'lemoniteur.fr' (sans https://, sans www)."""
    out = LOGOS_DIR / f"{dst_name}.png"
    if is_valid_png(out):
        return True, "cached"
    # nettoyer le domaine
    clean = domain.replace('https://', '').replace('http://', '').replace('www.', '').rstrip('/')
    try:
        # Step 1 : search to get brandId + icon URL
        api_url = f"https://api.brandfetch.io/v2/search/{urllib.parse.quote(clean)}"
        data = json.loads(fetch(api_url))
        if not data or not isinstance(data, list):
            return False, f"brandfetch '{clean}': no result"
        # Trouver l'entrée la plus pertinente (qualityScore)
        best = max(data, key=lambda d: d.get('qualityScore', 0) or 0)
        icon_url = best.get('icon')
        if not icon_url:
            return False, f"brandfetch '{clean}': no icon in result"
        img_data = fetch(icon_url)
        if len(img_data) < 500:
            return False, f"brandfetch '{clean}': image too small"
        # Convertir l'extension détectée (webp / png / svg)
        if img_data[:8].startswith(b'\x89PNG'):
            ext = '.png'
        elif img_data[:4] == b'RIFF' and img_data[8:12] == b'WEBP':
            ext = '.webp'
        elif img_data[:3] == b'\xff\xd8\xff':
            ext = '.jpg'
        elif b'<svg' in img_data[:200]:
            ext = '.svg'
        else:
            ext = '.bin'
        out.with_suffix(ext).write_bytes(img_data)
        return True, f"brandfetch '{clean}' (qualityScore={best.get('qualityScore', 0):.2f})"
    except Exception as e:
        return False, f"brandfetch '{clean}': {str(e)[:80]}"

# === CLI =================================================================
def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('--simpleicons', nargs='*', default=[],
        help="Liste de slugs simpleicons (ex: openai cloudflare) ou 'slug=dest'")
    parser.add_argument('--wikipedia', nargs='*', default=[],
        help="Liste 'Filename.svg=dest' pour Wikipedia Commons")
    parser.add_argument('--scrape', nargs='*', default=[],
        help="Liste 'https://site.com/=dest' pour scraping HTML officiel (multi-pages : home + /press + /brand + /media + /about + variantes)")
    parser.add_argument('--brandfetch', nargs='*', default=[],
        help="Liste 'domain.com=dest' pour API brandfetch (fallback sites avec Cloudflare/403)")
    parser.add_argument('--auto', nargs='*', default=[],
        help="Mode tout-en-un : 'marque=dest' essaie automatiquement les 4 couches dans l'ordre jusqu'à trouver. Idéal pour les marques inconnues.")
    parser.add_argument('--color', default='0A3856',
        help="Couleur hex pour simpleicons (sans #), defaut: bleu Empirik 0A3856")
    args = parser.parse_args()

    if not (args.simpleicons or args.wikipedia or args.scrape or args.brandfetch or args.auto):
        parser.print_help()
        sys.exit(0)

    total_ok, total_fail = 0, 0

    if args.simpleicons:
        print("\n=== Layer 1 : simpleicons CDN (SVG) ===")
        for spec in args.simpleicons:
            slug, dst = (spec.split('=', 1) if '=' in spec else (spec, spec))
            ok, info = fetch_simpleicons(slug, dst, args.color)
            print(f"  {'ok    ' if ok else 'FAIL  '}{dst}.svg  ({info})")
            total_ok += ok; total_fail += not ok
            time.sleep(0.2)

    if args.wikipedia:
        print("\n=== Layer 2 : Wikipedia Commons (PNG rendu) ===")
        for spec in args.wikipedia:
            filename, dst = spec.split('=', 1)
            ok, info = fetch_wikipedia(filename, dst)
            print(f"  {'ok    ' if ok else 'FAIL  '}{dst}.png  ({info})")
            total_ok += ok; total_fail += not ok
            time.sleep(0.3)

    if args.scrape:
        print("\n=== Layer 3 : Scraping HTML multi-pages officiel ===")
        for spec in args.scrape:
            site, dst = spec.split('=', 1)
            ok, info = fetch_official_site(site, dst)
            print(f"  {'ok    ' if ok else 'FAIL  '}{dst}.png  ({info})")
            total_ok += ok; total_fail += not ok
            time.sleep(0.5)

    if args.brandfetch:
        print("\n=== Layer 4 : brandfetch.com (API publique) ===")
        for spec in args.brandfetch:
            domain, dst = spec.split('=', 1)
            ok, info = fetch_brandfetch(domain, dst)
            print(f"  {'ok    ' if ok else 'FAIL  '}{dst}.png  ({info})")
            total_ok += ok; total_fail += not ok
            time.sleep(0.3)

    if args.auto:
        print("\n=== Mode AUTO : 4 couches en cascade ===")
        for spec in args.auto:
            brand, dst = (spec.split('=', 1) if '=' in spec else (spec, spec))
            print(f"\n  → '{brand}' → {dst}")
            success = False
            # Couche 1 : simpleicons (slug = brand en lowercase sans espaces)
            slug = brand.lower().replace(' ', '').replace('-', '').replace('.', '')
            ok, info = fetch_simpleicons(slug, dst, args.color)
            if ok:
                print(f"    [1] OK simpleicons : {info}")
                success = True
            else:
                print(f"    [1] FAIL simpleicons : {info}")
            # Couche 2 : Wikipedia (essai avec nom + "_logo.svg" et "Logo_<nom>.svg")
            if not success:
                for variant in [f"{brand}_logo.svg", f"Logo_{brand}.svg", f"{brand}.svg", f"{brand.replace(' ', '_')}_logo.svg"]:
                    ok, info = fetch_wikipedia(variant, dst)
                    if ok:
                        print(f"    [2] OK Wikipedia : {info}")
                        success = True
                        break
                if not success:
                    print(f"    [2] FAIL Wikipedia : 4 variantes essayées")
            # Couche 3 : scraping (essai sur domaine deviné)
            if not success:
                for tld in ['.com', '.fr', '.org', '.net']:
                    url = f"https://www.{brand.lower().replace(' ', '')}{tld}/"
                    ok, info = fetch_official_site(url, dst)
                    if ok:
                        print(f"    [3] OK scraping : {info}")
                        success = True
                        break
                if not success:
                    print(f"    [3] FAIL scraping : 4 TLDs essayés")
            # Couche 4 : brandfetch
            if not success:
                for tld in ['.com', '.fr', '.org', '.net']:
                    domain = f"{brand.lower().replace(' ', '')}{tld}"
                    ok, info = fetch_brandfetch(domain, dst)
                    if ok:
                        print(f"    [4] OK brandfetch : {info}")
                        success = True
                        break
                if not success:
                    print(f"    [4] FAIL brandfetch : 4 TLDs essayés")
            total_ok += success
            total_fail += not success
            if not success:
                print(f"    ⚠️  '{brand}' INTROUVABLE par les 4 couches automatiques.")
                print(f"        → Escalader manuellement (voir CLAUDE.md §2.6 'Persistance obligatoire' : crawl /press, Wikipedia EN, Google Images, Wayback Machine)")
            time.sleep(0.5)

    print(f"\nTotal : {total_ok} OK, {total_fail} FAIL")
    print(f"Logos disponibles dans {LOGOS_DIR}/")
    if total_fail > 0:
        print(f"\n⚠️  {total_fail} logo(s) en échec. NE PAS ABANDONNER — appliquer les méthodes manuelles d'escalade (CLAUDE.md §2.6).")

if __name__ == '__main__':
    main()
