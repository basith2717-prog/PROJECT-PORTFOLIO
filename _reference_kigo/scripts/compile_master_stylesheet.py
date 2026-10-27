import os
import re

print("Starting compilation of master stylesheet...")

# 1. Load clean kigo core
with open('_reference_kigo/scripts/kigo_clean_core.css', 'r', encoding='utf-8') as f:
    kigo_core = f.read()

# 2. Define custom overrides and portfolio additions
preamble = """/* ==========================================================================
   KIGO STUDIO OFFICIAL DESIGN SYSTEM & PORTFOLIO ENGINE
   Crafted with Japanese Digital Zen Brutalism matching https://kigo.studio
   ========================================================================== */

:root {
  --color-paper: #ffffff;
  --color-paper-warm: #efece8;
  --color-ink: #202020;
  --color-ink-soft: #4a4144;
  --color-ink-muted: #6e6e6e;

  --red: #d62828;
  --sakura: #db5b7f;
  --sakura-glow: rgba(219, 91, 127, 0.28);
  --teal: #21464b;
  --coral: #a13d27;
  --umber: #6f342d;
  --dark-grey: #272727;

  --border-subtle: rgba(39, 39, 39, 0.12);
  --border-card: rgba(39, 39, 39, 0.18);
  --rule: rgba(39, 39, 39, 0.16);

  /* Typography mappings to Google Fonts */
  --font-title: 'Kanit', 'Poppins', sans-serif;
  --font-serif: 'Playfair Display', Georgia, serif;
  --font-body: 'Poppins', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
  --font-kanji: 'Noto Serif JP', serif;

  --display: 'Kanit', 'Poppins', sans-serif;
  --display-italic: 'Playfair Display', Georgia, serif;
  --title: 'Kanit', 'Poppins', sans-serif;
  --serif: 'Playfair Display', Georgia, serif;

  /* Layout */
  --header-height: 80px;
  --max-width: 1400px;
  --edge-padding: clamp(16px, 3.5vw, 48px);
  --section-spacing: clamp(4.5rem, 8vw, 8.5rem);
  --p-section-y: clamp(4.5rem, 8vw, 8.5rem);

  /* Easing */
  --ease-rise: cubic-bezier(0.65, 0, 0.25, 1);
  --ease-soft: cubic-bezier(0.25, 0.7, 0.25, 1);
  --ease-spring: cubic-bezier(0.34, 1.56, 0.64, 1);
}

/* Base HTML & Window Scrolling Reset (Ensuring smooth natural browser scrolling) */
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
  -moz-osx-font-smoothing: grayscale;
}

#__nuxt {
  position: relative;
  width: 100%;
  min-height: 100vh;
  margin: 0 auto;
  overflow: visible;
}

main.home {
  position: relative;
  width: 100%;
  min-height: 100vh;
  overflow: visible;
  display: block;
}

.scrollable {
  position: relative;
  width: 100%;
  overflow: visible;
}

/* Override Nuxt Vue transitions to ensure immediate visibility */
.header__button,
.nav-item__mask,
.home-clients__haiku,
.service-menu-image,
.header__navigation-mobile,
.spring-calligraphy__trace {
  opacity: 1 !important;
  stroke-dashoffset: 0 !important;
}

.header__navigation-mobile {
  opacity: 1 !important;
}
"""

portfolio_sections = """
/* ==========================================================================
   HEADER NAVIGATION ALIGNMENT & INTERACTION
   ========================================================================== */
.header {
  position: sticky;
  top: 0;
  width: 100%;
  height: var(--header-height);
  z-index: 104;
  pointer-events: none;
  background: rgba(255, 255, 255, 0.92);
  backdrop-filter: blur(12px);
  -webkit-backdrop-filter: blur(12px);
  border-bottom: 1px solid rgba(39, 39, 39, 0.08);
  transition: transform 0.3s ease, background-color 0.3s ease;
}

.header__wrapper {
  height: 100%;
  max-width: var(--max-width);
  margin: 0 auto;
  padding-inline: var(--edge-padding);
}

.header__wrapper nav {
  display: flex;
  align-items: center;
  justify-content: space-between;
  height: 100%;
  width: 100%;
}

.header__logo-container {
  display: flex;
  align-items: center;
  text-decoration: none;
  pointer-events: all;
  cursor: pointer;
}

.header__navigation {
  display: flex;
  align-items: center;
  gap: clamp(1rem, 2.2vw, 2rem);
  list-style: none;
  margin: 0;
  padding: 0;
  pointer-events: all;
}

@media (max-width: 1024px) {
  .header__navigation {
    display: none;
  }
}

.nav-link {
  font-family: var(--font-title);
  font-size: clamp(13px, 1vw, 15px);
  font-weight: 600;
  letter-spacing: 0.02em;
  text-transform: uppercase;
  color: var(--color-ink);
  text-decoration: none;
  display: inline-flex;
  align-items: center;
  gap: 6px;
  position: relative;
  padding: 6px 0;
  transition: color 0.2s ease;
  cursor: pointer;
}

.nav-link:hover {
  color: var(--sakura);
}

.nav-item__dot {
  width: 5px;
  height: 5px;
  background: var(--red);
  border-radius: 50%;
  opacity: 0;
  transform: scale(0.5);
  transition: opacity 0.2s ease, transform 0.2s ease;
}

.nav-link:hover .nav-item__dot,
.nav-item.is-active .nav-item__dot {
  opacity: 1;
  transform: scale(1);
}

.header__actions {
  display: flex;
  align-items: center;
  gap: clamp(0.8rem, 1.6vw, 1.6rem);
  pointer-events: all;
}

.language {
  display: flex;
  align-items: center;
  gap: 0.5rem;
}

.language__icon {
  width: 18px;
  height: 18px;
  stroke: var(--color-ink);
}

.language__locale {
  font-family: var(--font-title);
  font-size: 13px;
  font-weight: 700;
  text-decoration: none;
  color: var(--color-ink);
  opacity: 0.45;
  transition: opacity 0.2s ease, color 0.2s ease;
}

.language__locale.current,
.language__locale:hover {
  opacity: 1;
}

.contact-postcard-cta {
  display: inline-flex;
  align-items: center;
  justify-content: space-between;
  gap: 10px;
  padding: 6px 18px;
  border: 1px solid #121212;
  background: transparent;
  color: #121212;
  font-family: var(--font-title);
  font-size: clamp(13px, 1vw, 15px);
  font-weight: 700;
  letter-spacing: 0.04em;
  text-transform: uppercase;
  text-decoration: none;
  line-height: 1.2;
  min-height: 40px;
  pointer-events: all;
  transition: background-color 0.25s ease, color 0.25s ease, border-color 0.25s ease;
}

.contact-postcard-cta:hover {
  background: #121212;
  color: #ffffff;
}

.contact-postcard-cta__kanji {
  font-family: var(--font-kanji);
  font-size: 20px;
  color: var(--red);
  line-height: 1;
  transition: transform 0.2s ease;
}

.contact-postcard-cta:hover .contact-postcard-cta__kanji {
  transform: scale(1.15);
}

.header__navigation-mobile {
  display: none;
  align-items: center;
  pointer-events: all;
}

@media (max-width: 1024px) {
  .header__navigation-mobile {
    display: flex;
  }
}

.header__menu-toggle {
  background: none;
  border: none;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  width: 44px;
  height: 44px;
  padding: 0;
  color: var(--color-ink);
}

/* ==========================================================================
   MEGA MENU & MOBILE DRAWER TOGGLE STATES
   ========================================================================== */
.nav-dropdown {
  position: fixed;
  inset: 0;
  background: #ffffff;
  z-index: 102;
  display: flex;
  flex-direction: column;
  height: min(580px, 85svh);
  border-bottom: 1px solid var(--rule);
  clip-path: inset(0 0 100% 0);
  transition: clip-path 0.8s cubic-bezier(0.6, 0, 0.2, 1);
  pointer-events: none;
}

.nav-dropdown.is-active,
.nav-dropdown[aria-hidden="false"] {
  clip-path: inset(0 0 0 0);
  pointer-events: all;
}

.nav-dropdown.is-active .nav-dropdown__item {
  opacity: 1;
  transform: translateY(0);
}

.nav-dropdown-mobile {
  position: fixed;
  inset: 0;
  background: #ffffff;
  z-index: 103;
  clip-path: inset(0 0 100% 0);
  transition: clip-path 0.8s cubic-bezier(0.6, 0, 0.2, 1);
  pointer-events: none;
}

.nav-dropdown-mobile.is-active,
.nav-dropdown-mobile[aria-hidden="false"] {
  clip-path: inset(0 0 0 0);
  pointer-events: all;
}

.nav-dropdown-mobile.is-active .nav-dropdown-mobile__item {
  opacity: 1;
  transform: translateY(0);
}

/* ==========================================================================
   HERO TITLE & HEADLINE ANIMATIONS
   ========================================================================== */
.hero {
  position: relative;
  min-height: 100vh;
  min-height: 100dvh;
  display: flex;
  align-items: flex-end;
  padding-block: calc(var(--header-height) + 2rem) clamp(3rem, 6vw, 6rem);
  overflow: hidden;
  background-color: #ffffff;
  isolation: isolate;
  width: 100%;
}

.hero__landscape {
  position: absolute;
  inset: 0;
  z-index: -2;
  pointer-events: none;
}

.hero__landscape img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.hero__landscape::after {
  content: "";
  position: absolute;
  inset: 0;
  background: radial-gradient(ellipse at center, rgba(255, 255, 255, 0.45) 15%, rgba(255, 255, 255, 0.75) 55%, #ffffff 88%);
}

.hero__spring {
  flex-shrink: 0;
  width: clamp(140px, 14vw, 240px);
  margin-left: var(--edge-padding);
  z-index: 3;
  position: relative;
}

.hero__content {
  padding-inline: var(--edge-padding);
  width: 100%;
  color: #202020;
  position: static;
}

.hero-title__heading {
  font-family: var(--display);
  font-size: clamp(2.5rem, 5.7vw, 8.5rem);
  font-weight: 700;
  letter-spacing: -0.065em;
  line-height: 0.88;
  text-transform: uppercase;
  margin: 0;
}

@media (max-width: 767px) {
  .hero-title__heading {
    font-size: 13vw;
  }
}

.hero-title__line {
  display: block;
  white-space: nowrap;
}

.hero-title__line--rotating {
  position: relative;
}

.hero-title__prefix {
  display: inline-block;
}

.hero-title__word-mask {
  clip-path: inset(-0.5em -0.3em 0 -0.3em);
  display: inline-block;
}

.hero-title__word {
  display: inline-block;
  transition: transform 0.55s var(--ease-rise);
}

.hero-title__accent {
  color: var(--sakura);
  font-family: var(--display-italic);
  font-size: 1.12em;
  font-style: italic;
  font-weight: 700;
  letter-spacing: -0.045em;
  line-height: 0.7;
  position: relative;
  text-transform: none;
  white-space: nowrap;
}

.hero-title__accent-text {
  display: inline-block;
  margin: -0.3em;
  padding: 0.3em;
}

.hero__description {
  color: var(--ink-soft);
  font-size: calc(clamp(0.95rem, 1.15vw, 1.15rem) * 1.15);
  line-height: 1.5;
  margin-top: 2rem;
  max-width: 32rem;
}

/* ==========================================================================
   CLIENTS / TECH STACK SECTION
   ========================================================================== */
.home-clients {
  padding: clamp(4.5rem, 9vw, 8.5rem) var(--edge-padding);
  position: relative;
  overflow-x: clip;
  background: #ffffff;
}

.home-clients__head {
  display: grid;
  grid-template-columns: minmax(0, 1fr);
  align-items: start;
  margin-bottom: clamp(2.5rem, 5vw, 5rem);
}

.home-clients__haiku {
  font-family: var(--font-kanji);
  font-size: clamp(1.4rem, 2.5vw, 2.2rem);
  font-weight: 600;
  writing-mode: vertical-rl;
  letter-spacing: 0.15em;
  line-height: 1.5;
  color: #202020;
  grid-area: 1 / 1;
  justify-self: start;
  margin: 0;
  z-index: 2;
}

.home-clients__reel {
  grid-area: 1 / 1;
  justify-self: start;
  margin-left: clamp(80px, 12vw, 180px);
  width: clamp(280px, 32vw, 440px);
  aspect-ratio: 16 / 9;
  position: relative;
  background: #121212;
  border-radius: 4px;
  overflow: hidden;
}

.home-clients__title {
  font-family: var(--display);
  font-size: clamp(2.2rem, 4.4vw, 5rem);
  font-weight: 700;
  grid-area: 1 / 1;
  justify-self: end;
  letter-spacing: -0.06em;
  line-height: 1.05;
  margin: 0;
  text-align: left;
  text-transform: uppercase;
  width: 58%;
}

@media (max-width: 900px) {
  .home-clients__head {
    display: flex;
    flex-direction: column;
    gap: 2rem;
  }
  .home-clients__haiku {
    writing-mode: horizontal-tb;
    position: static;
  }
  .home-clients__reel {
    margin-left: 0;
    width: 100%;
  }
  .home-clients__title {
    width: 100%;
    font-size: clamp(1.8rem, 6.5vw, 3.2rem);
  }
}

.home-clients__layout {
  display: grid;
  grid-template-columns: minmax(0, 2fr) minmax(0, 3fr);
  align-items: center;
  gap: 2rem;
  margin-top: 3.5rem;
  position: relative;
  isolation: isolate;
}

@media (max-width: 768px) {
  .home-clients__layout {
    grid-template-columns: 1fr;
  }
}

.home-clients__background {
  position: absolute;
  inset: 0;
  width: 100%;
  height: 100%;
  object-fit: cover;
  opacity: 0.35;
  pointer-events: none;
  z-index: -1;
  mask-image: linear-gradient(180deg, transparent, #000 10%, #000 90%, transparent);
  -webkit-mask-image: linear-gradient(180deg, transparent, #000 10%, #000 90%, transparent);
}

.home-clients__logos {
  position: relative;
  z-index: 2;
  width: min(100%, 420px);
  margin: 0 auto;
}

.home-clients__grid {
  display: grid;
  grid-template-columns: repeat(2, minmax(0, 1fr));
  list-style: none;
  padding: 0;
  margin: 0;
  gap: 1rem;
}

.home-clients__cell {
  aspect-ratio: 2;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 10px;
}

.home-clients__mark {
  height: clamp(36px, 3vw, 54px);
  width: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
}

.home-clients__mark img {
  max-width: min(80%, 140px);
  max-height: 100%;
  object-fit: contain;
  filter: brightness(0.15);
  transition: filter 0.25s ease;
}

.home-clients__mark:hover img {
  filter: brightness(0);
}

.home-clients__figure {
  position: relative;
  width: 100%;
  max-width: 440px;
  margin: 0 auto;
}

.client-dancer {
  aspect-ratio: 2 / 3;
  position: relative;
  width: 100%;
}

.client-dancer__pose {
  position: absolute;
  inset: 0;
  width: 100%;
  height: 100%;
  object-fit: contain;
  transition: opacity 0.5s ease;
}

/* ==========================================================================
   PORTFOLIO SELECTED WORK SECTION
   ========================================================================== */
.home-work {
  padding-block: var(--p-section-y);
  position: relative;
  background-color: var(--color-paper-warm);
}

.home-work__head {
  margin-bottom: 3rem;
  max-width: 700px;
}

.home-work__eyebrow {
  font-family: var(--font-kanji);
  font-size: 0.9rem;
  font-weight: 700;
  letter-spacing: 0.15em;
  color: var(--red);
  display: block;
  margin-bottom: 0.6rem;
}

.home-work__description {
  font-size: 1.15rem;
  color: var(--color-ink-soft);
  margin-top: 0.8rem;
}

.home-work__filters {
  display: flex;
  flex-wrap: wrap;
  gap: 0.8rem;
  margin-bottom: 3.5rem;
}

.work-filter {
  font-family: var(--font-title);
  font-size: 0.85rem;
  font-weight: 700;
  letter-spacing: 0.05em;
  text-transform: uppercase;
  padding: 0.55rem 1.4rem;
  border: 1px solid rgba(39, 39, 39, 0.2);
  border-radius: 99px;
  background: transparent;
  color: var(--color-ink);
  cursor: pointer;
  transition: all 0.25s ease;
}

.work-filter:hover {
  border-color: var(--sakura);
  color: var(--sakura);
}

.work-filter--active {
  background: #121212;
  border-color: #121212;
  color: #ffffff;
}

.work-filter--active:hover {
  background: var(--sakura);
  border-color: var(--sakura);
  color: #ffffff;
}

.home-work__grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(360px, 1fr));
  gap: 2.5rem;
  list-style: none;
  padding: 0;
  margin: 0;
}

@media (max-width: 768px) {
  .home-work__grid {
    grid-template-columns: 1fr;
  }
}

.work-card {
  background: #ffffff;
  border: 1px solid rgba(39, 39, 39, 0.16);
  border-radius: 4px;
  overflow: hidden;
  transition: transform 0.35s ease, box-shadow 0.35s ease;
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
  aspect-ratio: 16 / 10;
  overflow: hidden;
  background: #1a1a1a;
  position: relative;
}

.work-card__image img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  transition: transform 0.6s ease;
}

.work-card:hover .work-card__image img {
  transform: scale(1.06);
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
  letter-spacing: 0.08em;
  text-transform: uppercase;
  padding: 3px 8px;
  background: rgba(219, 91, 127, 0.12);
  color: var(--sakura);
  border-radius: 3px;
}

.work-card__title {
  font-family: var(--font-title);
  font-size: 1.4rem;
  font-weight: 700;
  letter-spacing: -0.03em;
  color: var(--color-ink);
  margin-bottom: 0.5rem;
}

.work-card__subtitle {
  font-size: 0.95rem;
  color: var(--color-ink-soft);
  line-height: 1.55;
  margin-bottom: 1.5rem;
  flex: 1;
}

.work-card__result {
  display: flex;
  align-items: baseline;
  gap: 0.5rem;
  padding-top: 1rem;
  border-top: 1px solid rgba(39, 39, 39, 0.1);
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
  padding-block: var(--p-section-y);
  background-color: var(--color-paper-warm);
  border-top: 1px solid rgba(39, 39, 39, 0.08);
}

.home-team__head {
  margin-bottom: 3.5rem;
  max-width: 700px;
}

.home-team__eyebrow {
  font-family: var(--font-kanji);
  font-size: 0.9rem;
  font-weight: 700;
  letter-spacing: 0.15em;
  color: var(--red);
  display: block;
  margin-bottom: 0.6rem;
}

.home-team__grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
  gap: 2rem;
}

.team-card {
  background: #ffffff;
  border: 1px solid rgba(39, 39, 39, 0.14);
  border-radius: 4px;
  padding: 2.2rem;
  display: flex;
  flex-direction: column;
  transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.team-card:hover {
  transform: translateY(-6px);
  box-shadow: 0 15px 35px rgba(0, 0, 0, 0.08);
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
   FAQ SECTION (With Omamori Amulet, Woodcut Flowers & Ribbon)
   ========================================================================== */
.service-faq {
  display: grid;
  grid-template-columns: minmax(0, 4fr) minmax(0, 7fr);
  gap: clamp(2rem, 5vw, 6rem);
  padding-block: var(--p-section-y);
  position: relative;
  isolation: isolate;
  background: #ffffff;
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
  width: min(100%, 340px);
  aspect-ratio: 2 / 3;
  margin-top: 2rem;
  position: relative;
}

.service-faq__omamori img {
  width: 100%;
  height: 100%;
  object-fit: contain;
  filter: drop-shadow(0 15px 30px rgba(0, 0, 0, 0.12));
}

.home__faq-flowers {
  position: absolute;
  inset: 0;
  pointer-events: none;
  z-index: -1;
  opacity: 0.2;
}

.home__faq-flowers img {
  position: absolute;
  object-fit: cover;
}

.home__faq-flowers--upper {
  top: -10%;
  left: -20%;
  width: 90%;
  height: 60%;
}

.home__faq-flowers--middle {
  top: 30%;
  left: -10%;
  width: 100%;
  height: 60%;
}

.home__faq-flowers--lower {
  bottom: -10%;
  left: 0;
  width: 110%;
  height: 60%;
}

.service-faq__list {
  display: flex;
  flex-direction: column;
  gap: 1.2rem;
  list-style: none;
  padding: 0;
  margin: 0;
}

.faq__item {
  position: relative;
  background: #ffffff;
  border: 1px solid rgba(39, 39, 39, 0.18);
  border-radius: 3px;
  padding: 1.5rem 2rem;
  transition: border-color 0.3s ease, box-shadow 0.3s ease;
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
  font-size: clamp(1.1rem, 1.8vw, 1.35rem);
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
  transition: transform 0.3s ease;
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
  font-size: 0.96rem;
  line-height: 1.7;
}

.faq__item.is-open .faq__answer {
  display: block;
}

/* ==========================================================================
   CONTACT / POSTCARD SECTION
   ========================================================================== */
.home-contact {
  padding-block: var(--p-section-y);
  background-color: var(--color-paper-warm);
}

.home-contact__inner {
  max-width: 820px;
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

.postcard {
  background: #ffffff;
  border: 1px solid rgba(39, 39, 39, 0.18);
  border-radius: 6px;
  padding: 2.5rem;
  margin-bottom: 2.5rem;
  box-shadow: 0 15px 40px rgba(0, 0, 0, 0.08);
  position: relative;
}

.postcard__header {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  border-bottom: 1px solid rgba(39, 39, 39, 0.12);
  padding-bottom: 1.5rem;
  margin-bottom: 1.8rem;
}

.postcard__stamp {
  width: 54px;
  height: 62px;
  border: 2px dashed var(--red);
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 3px;
}

.postcard__stamp-kanji {
  font-family: var(--font-kanji);
  font-size: 26px;
  font-weight: 800;
  color: var(--red);
}

.postcard__from {
  font-family: var(--font-title);
  font-size: 0.85rem;
  font-weight: 700;
  letter-spacing: 0.08em;
  color: #666666;
  text-transform: uppercase;
  text-align: right;
  line-height: 1.4;
}

.postcard__to {
  font-family: var(--font-title);
  font-size: 1.25rem;
  font-weight: 700;
  color: var(--color-ink);
  margin-bottom: 0.8rem;
}

.postcard__greeting {
  font-size: 1.05rem;
  color: var(--color-ink-soft);
  line-height: 1.6;
  margin-bottom: 1.8rem;
}

.postcard__links {
  display: flex;
  flex-wrap: wrap;
  gap: 1.2rem;
}

.postcard__link {
  font-family: var(--font-title);
  font-size: 0.9rem;
  font-weight: 700;
  letter-spacing: 0.04em;
  color: var(--sakura);
  text-decoration: underline;
  text-underline-offset: 4px;
}

.contact-form {
  background: #ffffff;
  border: 1px solid rgba(39, 39, 39, 0.18);
  border-radius: 6px;
  padding: 2.5rem;
  display: flex;
  flex-direction: column;
  gap: 1.6rem;
  box-shadow: 0 15px 40px rgba(0, 0, 0, 0.08);
}

.contact-form__group {
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
}

.contact-form__label {
  font-family: var(--font-title);
  font-size: 0.82rem;
  font-weight: 700;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  color: #444444;
}

.contact-form__input,
.contact-form__textarea {
  width: 100%;
  padding: 0.9rem 1.2rem;
  border: 1px solid rgba(39, 39, 39, 0.2);
  border-radius: 3px;
  font-family: var(--font-body);
  font-size: 0.96rem;
  color: var(--color-ink);
  background: #fbf9f6;
  transition: border-color 0.25s ease, background 0.25s ease;
  box-sizing: border-box;
}

.contact-form__input:focus,
.contact-form__textarea:focus {
  outline: none;
  border-color: var(--sakura);
  background: #ffffff;
}

.contact-form__submit {
  align-self: flex-start;
  cursor: pointer;
}

/* ==========================================================================
   SITE FOOTER SECTION
   ========================================================================== */
.site-footer {
  padding: 4.5rem var(--edge-padding) 2.5rem;
  background: #111111;
  color: #f6f6f6;
  border-top: 1px solid rgba(255, 255, 255, 0.08);
}

.site-footer__inner {
  display: grid;
  grid-template-columns: 1.2fr 2fr;
  gap: 3.5rem;
  margin-bottom: 3.5rem;
}

@media (max-width: 800px) {
  .site-footer__inner {
    grid-template-columns: 1fr;
  }
}

.site-footer__tagline {
  font-family: var(--font-title);
  font-size: 1.1rem;
  font-weight: 600;
  color: #dddddd;
  margin: 0.8rem 0 0.4rem;
}

.site-footer__location {
  font-size: 0.88rem;
  color: #888888;
}

.site-footer__nav {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(140px, 1fr));
  gap: 2rem;
}

.site-footer__nav-group {
  display: flex;
  flex-direction: column;
  gap: 0.6rem;
}

.site-footer__nav-label {
  font-family: var(--font-title);
  font-size: 0.78rem;
  font-weight: 800;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  color: var(--sakura);
  margin-bottom: 0.4rem;
}

.site-footer__link {
  font-size: 0.9rem;
  color: #aaaaaa;
  transition: color 0.2s ease;
  text-decoration: none;
}

.site-footer__link:hover {
  color: #ffffff;
}

.site-footer__bottom {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding-top: 2rem;
  border-top: 1px solid rgba(255, 255, 255, 0.08);
}

.site-footer__copy {
  font-size: 0.85rem;
  color: #666666;
}

.site-footer__kanji {
  font-family: var(--font-kanji);
  font-size: 1.1rem;
  color: var(--red);
  letter-spacing: 0.1em;
}

/* ==========================================================================
   CANVAS, CURSOR, SCROLLBAR & WHATSAPP
   ========================================================================== */
.sakura-canvas {
  position: fixed;
  inset: 0;
  width: 100vw;
  height: 100vh;
  pointer-events: none;
  z-index: 100;
}

#customCursor {
  position: fixed;
  pointer-events: none;
  z-index: 9999;
  width: 46px;
  height: 46px;
  border-radius: 50%;
  transform: translate(-50%, -50%);
  display: flex;
  align-items: center;
  justify-content: center;
  transition: width 0.2s ease, height 0.2s ease, background 0.2s ease;
  border: 1px solid rgba(32, 32, 32, 0.35);
  background: rgba(255, 255, 255, 0.25);
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

#scrollbar-container {
  position: fixed;
  right: 1.5%;
  top: 50%;
  transform: translateY(-50%);
  width: 5px;
  height: 140px;
  background: rgba(0, 0, 0, 0.1);
  border-radius: 4px;
  z-index: 1000;
  pointer-events: none;
}

#scrollbar-thumb {
  position: absolute;
  top: 0;
  width: 5px;
  height: 20%;
  background: rgba(0, 0, 0, 0.45);
  border-radius: 4px;
  transition: top 0.1s ease-out;
}

.whatsapp-icon {
  position: fixed;
  bottom: 2rem;
  right: var(--edge-padding);
  width: 52px;
  height: 52px;
  border-radius: 14px;
  z-index: 800;
  box-shadow: 0 8px 24px rgba(37, 211, 102, 0.35);
  transition: transform 0.3s var(--ease-spring);
  display: block;
}

.whatsapp-icon:hover {
  transform: scale(1.1) translateY(-2px);
}

.whatsapp-icon svg {
  width: 100%;
  height: 100%;
  display: block;
}
"""

master_css = preamble + "\n\n" + kigo_core + "\n\n" + portfolio_sections

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(master_css)

print(f"Master style.css written successfully: {len(master_css)} bytes")
