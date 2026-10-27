import sys
sys.stdout.reconfigure(encoding='utf-8')
import re
import os

print("=== STARTING COMPLETE PORTFOLIO POLISH ===")

# ----------------------------------------------------
# 1. UPDATE index.html
# ----------------------------------------------------
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1a. Ensure header has header--ready
html = re.sub(r'class="header header--paper header--wide(?!\s*header--ready)"',
              'class="header header--paper header--wide header--ready"', html)

# 1b. Add hero__branch if not present
if 'hero__branch' not in html:
    branch_html = '''
        <!-- Cherry Blossom Branch hanging from top right -->
        <div class="hero__branch" aria-hidden="true">
          <img src="./public/images/sakura-hero-branch.png" alt="" width="736" height="1023" loading="eager" decoding="async">
        </div>
'''
    html = html.replace('<!-- Hero Title & Content -->', branch_html + '\n        <!-- Hero Title & Content -->')

# 1c. Wrap contact postcard and form in home-contact__layout
if 'home-contact__layout' not in html:
    html = html.replace('<!-- Postcard contact card -->', '<div class="home-contact__layout">\n          <!-- Postcard contact card -->')
    html = html.replace('</form>\n\n        </div>', '</form>\n          </div><!-- /.home-contact__layout -->\n        </div>')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Updated index.html successfully.")

# ----------------------------------------------------
# 2. UPDATE main.js (subtle petals so text is never blocked)
# ----------------------------------------------------
with open('main.js', 'r', encoding='utf-8') as f:
    js = f.read()

# Make petals gentle and non-intrusive
js = re.sub(r'this\.maxPetals\s*=\s*\d+;', 'this.maxPetals = 20;', js)
js = re.sub(r'size:\s*10\s*\+\s*Math\.random\(\)\s*\*\s*14', 'size: 6 + Math.random() * 8', js)
js = re.sub(r'opacity:\s*0\.65\s*\+\s*Math\.random\(\)\s*\*\s*0\.35', 'opacity: 0.35 + Math.random() * 0.3', js)

with open('main.js', 'w', encoding='utf-8') as f:
    f.write(js)
print("Updated main.js petal simulation settings.")

# ----------------------------------------------------
# 3. BUILD MASTER style.css
# ----------------------------------------------------
with open('_reference_kigo/scripts/kigo_clean_core.css', 'r', encoding='utf-8') as f:
    kigo_core = f.read()

# Sanitize minified core rules
kigo_core = re.sub(r'main\s*\{[^}]*inset:0[^}]*overflow:hidden[^}]*position:fixed[^}]*\}', 
                   'main{position:relative;overflow:visible;}', kigo_core)
kigo_core = re.sub(r'#__nuxt\s*\{[^}]*position:absolute[^}]*\}', 
                   '#__nuxt{position:relative;width:100%;margin:0 auto;max-width:var(--max-width);padding:0 var(--padding-horizontal-page);}', kigo_core)
kigo_core = re.sub(r'(body\s*\{[^}]*);overflow:hidden;([^}]*\})', r'\1;overflow-x:hidden;\2', kigo_core)
kigo_core = re.sub(r'(html\s*\{[^}]*);overflow:hidden;([^}]*\})', r'\1;overflow-x:hidden;\2', kigo_core)
kigo_core = re.sub(r'\.scrollable\s*\{[^}]*position:fixed[^}]*\}', 
                   '.scrollable{position:relative;width:100%;}', kigo_core)
kigo_core = re.sub(r'\.header--wide\s*\{[^}]*margin-left:calc\(50% - 50vw\)[^}]*\}',
                   '.header--wide{width:100%;margin-left:0;padding-inline:var(--edge-padding);}', kigo_core)
kigo_core = re.sub(r'\.nav-item__mask\s*\{[^}]*opacity:0[^}]*\}',
                   '.nav-item__mask{opacity:1;display:flex;flex-direction:column;position:relative;row-gap:.2rem;z-index:10;}', kigo_core)
kigo_core = re.sub(r'\.spring-calligraphy__trace\s*\{[^}]*opacity:0[^}]*\}',
                   '.spring-calligraphy__trace{opacity:1;stroke-dasharray:none;stroke-dashoffset:0;stroke:white;}', kigo_core)

# Master custom stylesheet that overrides and perfects every section
custom_css = """
/* ==========================================================================
   KIGO STUDIO DESIGN SYSTEM & THEME TOKENS
   ========================================================================== */
:root {
  --color-paper: #ffffff;
  --color-paper-warm: #efece8;
  --color-ink: #202020;
  --color-ink-soft: #4a4144;
  --color-ink-muted: #6e6e6e;

  --red: #d62828;
  --sakura: #db5b7f;
  --sakura-glow: rgba(219, 91, 127, 0.22);
  --dark-grey: #202020;

  --border-subtle: rgba(32, 32, 32, 0.08);
  --border-card: rgba(32, 32, 32, 0.12);
  --border-strong: rgba(32, 32, 32, 0.2);

  --font-title: 'Kanit', 'Poppins', -apple-system, sans-serif;
  --font-serif: 'Playfair Display', Georgia, serif;
  --font-body: 'Poppins', -apple-system, BlinkMacSystemFont, sans-serif;
  --font-kanji: 'Noto Serif JP', serif;

  --display: 'Kanit', 'Poppins', -apple-system, sans-serif;
  --display-italic: 'Playfair Display', Georgia, serif;

  --header-height: 80px;
  --max-width: 1400px;
  --edge-padding: clamp(16px, 3.5vw, 48px);
  --section-spacing: clamp(4.5rem, 8vw, 8rem);
  --p-section-y: clamp(4.5rem, 8vw, 8rem);
}

*, *::before, *::after {
  box-sizing: border-box;
}

html {
  font-size: 16px;
  scroll-behavior: smooth;
  background-color: var(--color-paper);
  color: var(--color-ink);
  overflow-x: hidden;
}

body {
  font-family: var(--font-body);
  background-color: var(--color-paper);
  color: var(--color-ink);
  line-height: 1.6;
  min-height: 100vh;
  position: relative;
  overflow-x: hidden;
  margin: 0;
  -webkit-font-smoothing: antialiased;
}

#__nuxt {
  position: relative !important;
  width: 100% !important;
  min-height: 100vh !important;
  margin: 0 auto !important;
  padding: 0 !important;
  overflow: visible !important;
}

main.home, main {
  position: relative !important;
  width: 100% !important;
  min-height: 100vh !important;
  overflow: visible !important;
  display: block !important;
}

/* ==========================================================================
   GLOBAL SAKURA CANVAS & CURSOR
   ========================================================================== */
.sakura-canvas {
  position: fixed !important;
  inset: 0 !important;
  width: 100vw !important;
  height: 100vh !important;
  pointer-events: none !important;
  z-index: 1 !important;
  opacity: 0.6 !important;
}

#customCursor {
  position: fixed;
  pointer-events: none;
  z-index: 9999;
  width: 44px;
  height: 44px;
  border-radius: 50%;
  transform: translate(-50%, -50%);
  display: flex;
  align-items: center;
  justify-content: center;
  transition: width 0.2s ease, height 0.2s ease, background 0.2s ease;
  border: 1px solid rgba(32, 32, 32, 0.4);
  background: rgba(255, 255, 255, 0.3);
  backdrop-filter: blur(4px);
  -webkit-backdrop-filter: blur(4px);
  visibility: hidden;
}

#customCursor.is-hovering {
  width: 72px;
  height: 72px;
  background: rgba(219, 91, 127, 0.15);
  border-color: var(--sakura);
}

#customCursor .cursor-label {
  font-family: var(--font-title);
  font-size: 9px;
  font-weight: 700;
  letter-spacing: 0.08em;
  color: #202020;
  text-transform: uppercase;
  text-align: center;
  padding: 0 4px;
}

/* ==========================================================================
   HEADER & NAVIGATION
   ========================================================================== */
.header {
  position: sticky !important;
  top: 0 !important;
  width: 100% !important;
  height: var(--header-height) !important;
  z-index: 104 !important;
  background: rgba(255, 255, 255, 0.94) !important;
  backdrop-filter: blur(14px) !important;
  -webkit-backdrop-filter: blur(14px) !important;
  border-bottom: 1px solid rgba(32, 32, 32, 0.08) !important;
  pointer-events: all !important;
  display: block !important;
  transition: transform 0.3s ease, background-color 0.3s ease !important;
}

.header__wrapper {
  max-width: var(--max-width);
  margin: 0 auto;
  height: 100%;
  padding-inline: var(--edge-padding);
}

.header__wrapper nav {
  display: flex !important;
  align-items: center !important;
  justify-content: space-between !important;
  height: 100% !important;
  width: 100% !important;
}

.header__logo-container {
  display: flex !important;
  align-items: center !important;
  text-decoration: none !important;
  pointer-events: all !important;
  cursor: pointer !important;
}

.header__logo {
  cursor: pointer;
  pointer-events: all;
  height: 32px;
  width: auto;
}

.header__navigation {
  display: flex !important;
  align-items: center !important;
  gap: clamp(1rem, 2.2vw, 2.2rem) !important;
  list-style: none !important;
  margin: 0 !important;
  padding: 0 !important;
  pointer-events: all !important;
  opacity: 1 !important;
  visibility: visible !important;
}

@media (max-width: 1024px) {
  .header__navigation {
    display: none !important;
  }
}

.nav-item {
  position: relative;
  display: flex;
  align-items: center;
}

.nav-item__mask {
  opacity: 1 !important;
  visibility: visible !important;
  display: flex !important;
  align-items: center !important;
}

.nav-link {
  font-family: var(--font-title) !important;
  font-size: clamp(13px, 1vw, 14.5px) !important;
  font-weight: 600 !important;
  letter-spacing: 0.04em !important;
  text-transform: uppercase !important;
  color: #202020 !important;
  text-decoration: none !important;
  display: inline-flex !important;
  align-items: center !important;
  gap: 6px !important;
  position: relative !important;
  padding: 6px 4px !important;
  transition: color 0.2s ease !important;
  cursor: pointer !important;
  background: none !important;
  border: none !important;
}

.nav-link:hover {
  color: var(--red) !important;
}

.nav-item__dot {
  width: 5px !important;
  height: 5px !important;
  background: var(--red) !important;
  border-radius: 50% !important;
  opacity: 0 !important;
  transform: scale(0.4) !important;
  transition: opacity 0.2s ease, transform 0.2s ease !important;
}

.nav-link:hover .nav-item__dot,
.nav-item.is-active .nav-item__dot {
  opacity: 1 !important;
  transform: scale(1) !important;
}

.header__actions {
  display: flex !important;
  align-items: center !important;
  gap: clamp(0.8rem, 1.6vw, 1.6rem) !important;
  pointer-events: all !important;
  opacity: 1 !important;
  visibility: visible !important;
}

.language {
  display: flex;
  align-items: center;
  gap: 0.4rem;
}

.language__icon {
  width: 18px;
  height: 18px;
  stroke: #202020;
}

.language__locale {
  font-family: var(--font-title);
  font-size: 13px;
  font-weight: 700;
  text-decoration: none;
  color: #202020;
  opacity: 0.45;
  transition: opacity 0.2s ease, color 0.2s ease;
}

.language__locale.current,
.language__locale:hover {
  opacity: 1;
}

.header__button {
  opacity: 1 !important;
  visibility: visible !important;
}

.contact-postcard-cta {
  display: inline-flex !important;
  align-items: center !important;
  gap: 0.6rem !important;
  font-family: var(--font-title) !important;
  font-size: 12.5px !important;
  font-weight: 700 !important;
  letter-spacing: 0.08em !important;
  text-transform: uppercase !important;
  color: #202020 !important;
  text-decoration: none !important;
  border: 1px solid rgba(32, 32, 32, 0.35) !important;
  padding: 7px 16px !important;
  border-radius: 2px !important;
  transition: all 0.25s ease !important;
  background: transparent !important;
}

.contact-postcard-cta:hover {
  border-color: var(--red) !important;
  background: var(--red) !important;
  color: #ffffff !important;
}

.contact-postcard-cta__kanji {
  font-family: var(--font-kanji);
  font-size: 13px;
  font-weight: 700;
  color: var(--red);
  transition: color 0.25s ease;
}

.contact-postcard-cta:hover .contact-postcard-cta__kanji {
  color: #ffffff;
}

@media (min-width: 1025px) {
  .header__navigation-mobile {
    display: none !important;
  }
}

@media (max-width: 1024px) {
  .header__navigation-mobile {
    display: flex !important;
    align-items: center !important;
    opacity: 1 !important;
    visibility: visible !important;
    pointer-events: all !important;
  }
  .header__button {
    display: none !important;
  }
}

.header__menu-toggle {
  background: none;
  border: none;
  cursor: pointer;
  padding: 4px;
  display: flex;
  align-items: center;
  justify-content: center;
}

.hamburger-line {
  stroke: #202020;
  stroke-width: 2;
  transition: transform 0.3s ease;
}

/* ==========================================================================
   HERO SECTION WITH TOP-RIGHT SAKURA BRANCH
   ========================================================================== */
.hero {
  position: relative !important;
  min-height: calc(100vh - var(--header-height)) !important;
  display: flex !important;
  flex-direction: column !important;
  justify-content: center !important;
  padding: clamp(2rem, 5vw, 4rem) var(--edge-padding) clamp(4rem, 6vw, 6rem) !important;
  overflow: hidden !important;
  background-color: #ffffff !important;
  isolation: isolate !important;
  width: 100% !important;
}

/* Misty landscape watercolor art in background */
.hero__landscape {
  position: absolute;
  inset: 0;
  z-index: 0;
  pointer-events: none;
}

.hero__landscape img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  object-position: 70% center;
  opacity: 0.55;
}

.hero__landscape::after {
  content: "";
  position: absolute;
  inset: 0;
  background: linear-gradient(90deg, #ffffff 25%, rgba(255, 255, 255, 0.7) 60%, rgba(255, 255, 255, 0.1) 100%);
}

/* SAKURA BRANCH ART HANGING FROM TOP RIGHT (Exact Kigo Studio Aesthetic) */
.hero__branch {
  position: absolute;
  top: -15px;
  right: 0;
  width: clamp(260px, 32vw, 480px);
  height: auto;
  pointer-events: none;
  z-index: 2;
  filter: drop-shadow(0 10px 25px rgba(219, 91, 127, 0.12));
}

.hero__branch img {
  width: 100%;
  height: auto;
  display: block;
}

@media (max-width: 640px) {
  .hero__branch {
    width: 220px;
    opacity: 0.75;
  }
}

.hero__content {
  position: relative;
  z-index: 3;
  max-width: var(--max-width);
  margin: 0 auto;
  width: 100%;
}

.hero-title__above {
  display: block;
  margin-bottom: 0.8rem;
}

/* Authentic Japanese Spring Calligraphy Mark */
.spring-calligraphy {
  width: clamp(75px, 8vw, 105px) !important;
  height: clamp(75px, 8vw, 105px) !important;
  color: var(--red) !important;
  display: block !important;
  opacity: 1 !important;
  visibility: visible !important;
}

.spring-calligraphy__trace {
  opacity: 1 !important;
  stroke: white !important;
  stroke-dasharray: none !important;
  stroke-dashoffset: 0 !important;
  animation: none !important;
}

.hero-title__heading {
  font-family: var(--font-title);
  font-size: clamp(3rem, 6.5vw, 7.5rem);
  font-weight: 800;
  letter-spacing: -0.055em;
  line-height: 0.94;
  text-transform: uppercase;
  margin: 0;
  color: #202020;
}

.hero-title__line {
  display: block;
  white-space: nowrap;
}

.hero-title__accent {
  font-family: var(--font-serif) !important;
  font-style: italic !important;
  font-weight: 700 !important;
  color: var(--sakura) !important;
  text-transform: none !important;
  letter-spacing: -0.03em !important;
}

.hero__description {
  font-family: var(--font-body);
  font-size: clamp(1rem, 1.2vw, 1.18rem);
  color: var(--color-ink-soft);
  line-height: 1.6;
  margin-top: 1.8rem;
  max-width: 32rem;
}

/* ==========================================================================
   CLIENTS / TECHNOLOGIES SECTION
   ========================================================================== */
.home-clients {
  padding: clamp(4.5rem, 8vw, 8rem) var(--edge-padding);
  position: relative;
  background: #ffffff;
  border-top: 1px solid rgba(32, 32, 32, 0.06);
}

.home-clients__head {
  display: flex !important;
  align-items: center !important;
  justify-content: space-between !important;
  flex-wrap: wrap !important;
  gap: clamp(2rem, 4vw, 4rem) !important;
  max-width: var(--max-width) !important;
  margin: 0 auto clamp(3rem, 5vw, 5rem) !important;
}

.home-clients__haiku,
.home-clients__title,
.home-clients__reel {
  grid-area: auto !important;
  margin: 0 !important;
  position: relative !important;
}

.home-clients__haiku {
  font-family: var(--font-kanji) !important;
  font-size: clamp(1.2rem, 1.8vw, 1.6rem) !important;
  font-weight: 600 !important;
  writing-mode: vertical-rl !important;
  letter-spacing: 0.18em !important;
  line-height: 1.6 !important;
  color: #202020 !important;
}

@media (max-width: 900px) {
  .home-clients__haiku {
    writing-mode: horizontal-tb !important;
  }
}

.home-clients__title {
  font-family: var(--font-title) !important;
  font-size: clamp(2.2rem, 4.4vw, 4.6rem) !important;
  font-weight: 800 !important;
  letter-spacing: -0.05em !important;
  line-height: 1.02 !important;
  text-transform: uppercase !important;
  color: #202020 !important;
  flex: 1 1 350px !important;
  width: auto !important;
}

.home-clients__reel {
  width: clamp(240px, 25vw, 340px) !important;
  aspect-ratio: 16 / 9 !important;
  background: #181818 !important;
  border-radius: 6px !important;
  overflow: hidden !important;
  box-shadow: 0 12px 32px rgba(0, 0, 0, 0.12) !important;
  display: flex !important;
  align-items: center !important;
  justify-content: center !important;
  flex-shrink: 0 !important;
}

.home-reel__poster {
  width: 100%;
  height: 100%;
  background: #181818;
  border: none;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 1rem;
  color: #ffffff;
}

.home-reel__poster-brand {
  font-family: var(--font-title);
  font-size: 1.3rem;
  font-weight: 700;
}

.home-reel__poster-brand em {
  font-family: var(--font-serif);
  font-style: italic;
  color: var(--sakura);
}

.home-reel__play {
  width: 36px;
  height: 36px;
  border: 1px solid rgba(255, 255, 255, 0.4);
  display: flex;
  align-items: center;
  justify-content: center;
  transition: transform 0.25s ease;
}

.home-reel__poster:hover .home-reel__play {
  transform: scale(1.1);
  border-color: var(--sakura);
}

.home-clients__layout {
  display: grid !important;
  grid-template-columns: minmax(0, 1fr) minmax(0, 1.4fr) !important;
  align-items: center !important;
  gap: clamp(2rem, 5vw, 6rem) !important;
  max-width: var(--max-width) !important;
  margin: 0 auto !important;
}

@media (max-width: 900px) {
  .home-clients__layout {
    grid-template-columns: 1fr !important;
  }
}

.home-clients__logos {
  position: relative !important;
  width: 100% !important;
  max-width: 480px !important;
}

.home-clients__grid {
  display: grid !important;
  grid-template-columns: repeat(3, minmax(0, 1fr)) !important;
  gap: 1.2rem !important;
  list-style: none !important;
  padding: 0 !important;
  margin: 0 !important;
}

@media (max-width: 600px) {
  .home-clients__grid {
    grid-template-columns: repeat(2, minmax(0, 1fr)) !important;
  }
}

.home-clients__cell {
  background: #fbf9f7 !important;
  border: 1px solid rgba(32, 32, 32, 0.08) !important;
  border-radius: 6px !important;
  padding: 1.2rem !important;
  display: flex !important;
  align-items: center !important;
  justify-content: center !important;
  aspect-ratio: 2 / 1 !important;
  transition: all 0.25s ease !important;
}

.home-clients__cell:hover {
  background: #ffffff !important;
  border-color: rgba(32, 32, 32, 0.2) !important;
  transform: translateY(-3px) !important;
  box-shadow: 0 8px 20px rgba(0, 0, 0, 0.06) !important;
}

.home-clients__mark img {
  max-width: min(80%, 140px) !important;
  max-height: 48px !important;
  object-fit: contain !important;
  filter: brightness(0.18) !important;
  transition: filter 0.25s ease !important;
}

.home-clients__cell:hover .home-clients__mark img {
  filter: brightness(0) !important;
}

/* ENLARGED DANCER FIGURE EXACTLY MATCHING KIGO.STUDIO */
.home-clients__figure {
  margin: 0 !important;
  position: relative !important;
  width: 100% !important;
  max-width: 760px !important;
  display: flex !important;
  align-items: center !important;
  justify-content: center !important;
  pointer-events: none !important;
  z-index: 2 !important;
}

.client-dancer {
  width: 100% !important;
  max-width: 720px !important;
  height: clamp(520px, 68vh, 920px) !important;
  aspect-ratio: 2 / 3 !important;
  position: relative !important;
  margin: 0 auto !important;
  filter: drop-shadow(0 20px 45px rgba(0, 0, 0, 0.08)) !important;
}

.client-dancer img,
.client-dancer__pose {
  width: 100% !important;
  height: 100% !important;
  object-fit: contain !important;
  position: absolute !important;
  inset: 0 !important;
  display: block !important;
  transition: opacity 0.5s ease-in-out !important;
}

/* ==========================================================================
   PORTFOLIO SELECTED WORK SECTION
   ========================================================================== */
.home-work {
  padding: clamp(4.5rem, 8vw, 8rem) var(--edge-padding);
  background-color: var(--color-paper-warm);
}

.home-work__head {
  max-width: var(--max-width);
  margin: 0 auto 2.5rem;
}

.home-work__eyebrow {
  font-family: var(--font-kanji);
  font-size: 0.95rem;
  font-weight: 700;
  letter-spacing: 0.18em;
  color: var(--red);
  display: block;
  margin-bottom: 0.6rem;
}

.home-work__description {
  font-size: 1.05rem;
  color: var(--color-ink-soft);
  margin-top: 0.8rem;
}

.home-work__filters {
  display: flex;
  gap: 0.8rem;
  flex-wrap: wrap;
  max-width: var(--max-width);
  margin: 0 auto 3.5rem;
}

.work-filter {
  font-family: var(--font-title);
  font-size: 0.82rem;
  font-weight: 700;
  letter-spacing: 0.06em;
  text-transform: uppercase;
  padding: 0.5rem 1.3rem;
  border: 1px solid rgba(32, 32, 32, 0.2);
  border-radius: 99px;
  background: transparent;
  color: var(--color-ink);
  cursor: pointer;
  transition: all 0.2s ease;
}

.work-filter:hover {
  border-color: var(--red);
  color: var(--red);
}

.work-filter--active {
  background: #202020 !important;
  border-color: #202020 !important;
  color: #ffffff !important;
}

.home-work__grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(360px, 1fr));
  gap: clamp(1.8rem, 3vw, 2.8rem);
  max-width: var(--max-width);
  margin: 0 auto;
  list-style: none;
  padding: 0;
}

.work-card {
  background: #ffffff;
  border: 1px solid rgba(32, 32, 32, 0.12);
  border-radius: 8px;
  overflow: hidden;
  transition: transform 0.35s ease, box-shadow 0.35s ease;
  display: flex;
  flex-direction: column;
}

.work-card:hover {
  transform: translateY(-8px);
  box-shadow: 0 20px 45px rgba(0, 0, 0, 0.1);
}

.work-card__inner {
  display: flex;
  flex-direction: column;
  height: 100%;
}

.work-card__image-link {
  display: block;
  aspect-ratio: 16 / 11;
  overflow: hidden;
  background: #1a1a1a;
  position: relative;
}

.work-card__image {
  width: 100%;
  height: 100%;
}

.work-card__image img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  transition: transform 0.6s ease;
}

.work-card:hover .work-card__image img {
  transform: scale(1.05);
}

.work-card__meta {
  padding: 1.8rem;
  display: flex;
  flex-direction: column;
  flex: 1;
}

.work-card__tags {
  display: flex;
  flex-wrap: wrap;
  gap: 6px;
  margin-bottom: 0.8rem;
}

.work-tag {
  font-family: var(--font-title);
  font-size: 0.72rem;
  font-weight: 700;
  letter-spacing: 0.06em;
  text-transform: uppercase;
  padding: 3px 8px;
  background: rgba(219, 91, 127, 0.1);
  color: var(--sakura);
  border-radius: 3px;
}

.work-card__title {
  font-family: var(--font-title);
  font-size: 1.35rem;
  font-weight: 700;
  letter-spacing: -0.03em;
  color: var(--color-ink);
  margin: 0 0 0.5rem;
}

.work-card__subtitle {
  font-size: 0.94rem;
  color: var(--color-ink-soft);
  line-height: 1.55;
  margin: 0 0 1.5rem;
  flex: 1;
}

.work-card__result {
  display: flex;
  align-items: baseline;
  gap: 0.5rem;
  padding-top: 1rem;
  border-top: 1px solid rgba(32, 32, 32, 0.08);
}

.result-value {
  font-family: var(--font-title);
  font-size: 1.6rem;
  font-weight: 800;
  color: var(--red);
}

.result-label {
  font-size: 0.85rem;
  color: #777777;
}

/* ==========================================================================
   EXPERIENCE & EDUCATION SECTION
   ========================================================================== */
.home-team {
  padding: clamp(4.5rem, 8vw, 8rem) var(--edge-padding);
  background-color: var(--color-paper-warm);
  border-top: 1px solid rgba(32, 32, 32, 0.08);
}

.home-team__head {
  max-width: var(--max-width);
  margin: 0 auto 3rem;
}

.home-team__eyebrow {
  font-family: var(--font-kanji);
  font-size: 0.95rem;
  font-weight: 700;
  letter-spacing: 0.18em;
  color: var(--red);
  display: block;
  margin-bottom: 0.6rem;
}

.home-team__grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
  gap: 2rem;
  max-width: var(--max-width);
  margin: 0 auto;
}

.team-card {
  background: #ffffff;
  border: 1px solid rgba(32, 32, 32, 0.12);
  border-radius: 8px;
  padding: 2.2rem;
  display: flex;
  flex-direction: column;
  transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.team-card:hover {
  transform: translateY(-6px);
  box-shadow: 0 16px 36px rgba(0, 0, 0, 0.08);
}

.team-card__role {
  font-family: var(--font-title);
  font-size: 1.25rem;
  font-weight: 800;
  color: var(--color-ink);
  margin-bottom: 0.3rem;
}

.team-card__name {
  font-family: var(--font-serif);
  font-style: italic;
  font-size: 1.05rem;
  color: var(--sakura);
  margin-bottom: 0.4rem;
}

.team-card__period {
  font-family: var(--font-title);
  font-size: 0.78rem;
  font-weight: 700;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  color: #888888;
  margin-bottom: 1.2rem;
}

.team-card__bio {
  font-size: 0.95rem;
  color: var(--color-ink-soft);
  line-height: 1.6;
  margin-bottom: 1.5rem;
  flex: 1;
}

.team-card__skills {
  display: flex;
  flex-wrap: wrap;
  gap: 6px;
  list-style: none;
  padding: 0;
  margin: 0;
}

.team-card__skills li {
  font-family: var(--font-title);
  font-size: 0.75rem;
  font-weight: 600;
  padding: 3px 10px;
  background: rgba(0, 0, 0, 0.04);
  border-radius: 99px;
  color: #444444;
}

/* ==========================================================================
   FAQ SECTION (With Omamori Talisman & Ornamental Borders)
   ========================================================================== */
.service-faq {
  display: grid;
  grid-template-columns: minmax(0, 4fr) minmax(0, 7fr);
  gap: clamp(2rem, 5vw, 6rem);
  padding: clamp(4.5rem, 8vw, 8rem) var(--edge-padding);
  position: relative;
  isolation: isolate;
  background: #ffffff;
  max-width: var(--max-width);
  margin: 0 auto;
}

@media (max-width: 900px) {
  .service-faq {
    grid-template-columns: 1fr;
  }
}

.service-faq__head {
  display: flex;
  flex-direction: column;
  position: relative;
}

.service-faq__omamori {
  width: min(100%, 300px);
  margin-top: 2rem;
}

.service-faq__omamori img {
  width: 100%;
  height: auto;
  display: block;
}

.faq__list {
  list-style: none;
  padding: 0;
  margin: 0;
  display: flex;
  flex-direction: column;
  gap: 1.2rem;
}

.faq__item {
  position: relative;
  background: #ffffff;
  border: 1px solid rgba(32, 32, 32, 0.14);
  border-radius: 4px;
  padding: 1.5rem 2rem;
  transition: border-color 0.25s ease, box-shadow 0.25s ease;
}

.faq__item.is-open {
  border-color: var(--sakura);
  box-shadow: 0 8px 25px rgba(219, 91, 127, 0.1);
}

.faq__question {
  width: 100%;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 1.2rem;
  font-family: var(--font-title);
  font-size: clamp(1.05rem, 1.6vw, 1.25rem);
  font-weight: 700;
  letter-spacing: -0.02em;
  color: var(--color-ink);
  cursor: pointer;
  text-align: left;
  background: none;
  border: none;
  padding: 0;
}

.faq__icon {
  width: 18px;
  height: 18px;
  position: relative;
  flex-shrink: 0;
}

.faq__icon::before,
.faq__icon::after {
  content: "";
  position: absolute;
  background: currentColor;
  transition: transform 0.25s ease;
}

.faq__icon::before {
  top: 50%;
  left: 0;
  width: 100%;
  height: 2px;
  transform: translateY(-50%);
}

.faq__icon::after {
  top: 0;
  left: 50%;
  width: 2px;
  height: 100%;
  transform: translateX(-50%);
}

.faq__item.is-open .faq__icon::after {
  transform: translateX(-50%) rotate(90deg);
  opacity: 0;
}

.faq__answer {
  display: none;
  padding-top: 1rem;
  color: var(--color-ink-soft);
  font-size: 0.95rem;
  line-height: 1.65;
}

.faq__item.is-open .faq__answer {
  display: block;
}

/* ==========================================================================
   CONTACT / POSTCARD SECTION (Two-Column Editorial Layout)
   ========================================================================== */
.home-contact {
  padding: clamp(4.5rem, 8vw, 8rem) var(--edge-padding);
  background-color: var(--color-paper-warm);
  border-top: 1px solid rgba(32, 32, 32, 0.08);
}

.home-contact__inner {
  max-width: var(--max-width);
  margin: 0 auto;
}

.home-contact__head {
  text-align: center;
  margin-bottom: 3.5rem;
}

.home-contact__eyebrow {
  font-family: var(--font-kanji);
  font-size: 0.95rem;
  font-weight: 700;
  letter-spacing: 0.18em;
  color: var(--red);
  display: block;
  margin-bottom: 0.6rem;
}

.home-contact__layout {
  display: grid;
  grid-template-columns: minmax(0, 1fr) minmax(0, 1fr);
  gap: clamp(2rem, 4vw, 4rem);
  align-items: start;
}

@media (max-width: 900px) {
  .home-contact__layout {
    grid-template-columns: 1fr;
  }
}

.postcard {
  background: #ffffff;
  border: 1px solid rgba(32, 32, 32, 0.14);
  border-radius: 8px;
  padding: 2.5rem;
  box-shadow: 0 12px 35px rgba(0, 0, 0, 0.06);
}

.postcard__header {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  border-bottom: 1px solid rgba(32, 32, 32, 0.1);
  padding-bottom: 1.5rem;
  margin-bottom: 1.8rem;
}

.postcard__stamp {
  width: 52px;
  height: 60px;
  border: 2px dashed var(--red);
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 3px;
}

.postcard__stamp-kanji {
  font-family: var(--font-kanji);
  font-size: 24px;
  font-weight: 800;
  color: var(--red);
}

.postcard__from {
  font-family: var(--font-title);
  font-size: 0.85rem;
  font-weight: 700;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  color: #666666;
  text-align: right;
  line-height: 1.4;
}

.postcard__to {
  font-family: var(--font-title);
  font-size: 1.4rem;
  font-weight: 800;
  letter-spacing: -0.02em;
  color: var(--color-ink);
  margin-bottom: 1rem;
}

.postcard__to em {
  font-family: var(--font-serif);
  font-style: italic;
  color: var(--sakura);
}

.postcard__greeting {
  font-size: 0.98rem;
  color: var(--color-ink-soft);
  line-height: 1.65;
  margin-bottom: 2rem;
}

.postcard__links {
  display: flex;
  flex-direction: column;
  gap: 0.6rem;
}

.postcard__link {
  font-family: var(--font-title);
  font-size: 0.92rem;
  font-weight: 600;
  color: var(--sakura);
  text-decoration: underline;
  text-underline-offset: 4px;
  transition: color 0.2s ease;
}

.postcard__link:hover {
  color: var(--red);
}

.contact-form {
  background: #ffffff;
  border: 1px solid rgba(32, 32, 32, 0.14);
  border-radius: 8px;
  padding: 2.5rem;
  box-shadow: 0 12px 35px rgba(0, 0, 0, 0.06);
}

.contact-form__group {
  margin-bottom: 1.4rem;
}

.contact-form__label {
  display: block;
  font-family: var(--font-title);
  font-size: 0.82rem;
  font-weight: 700;
  letter-spacing: 0.04em;
  text-transform: uppercase;
  color: #202020;
  margin-bottom: 0.5rem;
}

.contact-form__input,
.contact-form__textarea {
  width: 100%;
  padding: 0.85rem 1.1rem;
  border: 1px solid rgba(32, 32, 32, 0.18);
  border-radius: 4px;
  font-family: var(--font-body);
  font-size: 0.95rem;
  color: #202020;
  background: #fbf9f7;
  transition: border-color 0.2s ease, background 0.2s ease;
  box-sizing: border-box;
}

.contact-form__input:focus,
.contact-form__textarea:focus {
  outline: none;
  border-color: var(--red);
  background: #ffffff;
}

.contact-form__submit {
  width: 100%;
  justify-content: center;
  padding: 1rem;
  cursor: pointer;
}

/* ==========================================================================
   SITE FOOTER (Dark Japanese Zen Aesthetic)
   ========================================================================== */
.site-footer {
  background-color: #161616 !important;
  color: #e5e5e5 !important;
  padding: clamp(4rem, 7vw, 6rem) var(--edge-padding) 2.5rem !important;
  border-top: 1px solid rgba(255, 255, 255, 0.08) !important;
}

.site-footer__inner {
  display: grid;
  grid-template-columns: minmax(0, 1.4fr) minmax(0, 2.6fr);
  gap: clamp(2rem, 5vw, 5rem);
  max-width: var(--max-width);
  margin: 0 auto;
}

@media (max-width: 900px) {
  .site-footer__inner {
    grid-template-columns: 1fr;
  }
}

.site-footer__logo text {
  fill: #ffffff !important;
}

.site-footer__tagline {
  color: #999999;
  font-size: 0.95rem;
  margin: 0.6rem 0;
}

.site-footer__location {
  color: #777777;
  font-size: 0.88rem;
  margin: 0;
}

.site-footer__nav {
  display: grid;
  grid-template-columns: repeat(3, minmax(0, 1fr));
  gap: 2rem;
}

@media (max-width: 600px) {
  .site-footer__nav {
    grid-template-columns: 1fr;
  }
}

.site-footer__nav-group {
  display: flex;
  flex-direction: column;
  gap: 0.6rem;
}

.site-footer__nav-label {
  font-family: var(--font-title);
  font-size: 0.78rem;
  font-weight: 700;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  color: var(--sakura);
  margin-bottom: 0.4rem;
}

.site-footer__link {
  color: #aaaaaa;
  text-decoration: none;
  font-size: 0.92rem;
  transition: color 0.2s ease;
}

.site-footer__link:hover {
  color: #ffffff;
}

.site-footer__bottom {
  max-width: var(--max-width);
  margin: 4rem auto 0;
  padding-top: 2rem;
  border-top: 1px solid rgba(255, 255, 255, 0.08);
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.site-footer__copy {
  color: #666666;
  font-size: 0.85rem;
  margin: 0;
}

.site-footer__kanji {
  font-family: var(--font-kanji);
  font-size: 1.1rem;
  color: #666666;
  margin: 0;
}

/* ==========================================================================
   FINAL OVERRIDE & CLEANUP
   ========================================================================== */
html, body {
  overflow-x: hidden !important;
}

body {
  overflow-y: auto !important;
  min-height: 100vh !important;
  height: auto !important;
  background-color: #ffffff !important;
  color: #202020 !important;
}

#__nuxt, main.home, main, .home__group, .home__content {
  overflow: visible !important;
  position: relative !important;
  height: auto !important;
}
"""

master_css = kigo_core + "\n\n" + custom_css

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(master_css)

print(f"Master style.css written: {len(master_css)} bytes.")
print("=== COMPLETE BUILD FINISHED SUCCESSFULLY ===")
