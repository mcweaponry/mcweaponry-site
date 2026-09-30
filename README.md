# M.C. Weaponry — mcweaponry.com

Landing page for M.C. Weaponry, hand engraving and gunsmithing in York, PA.
A single-page Svelte 5 + Vite site, hosted on GitHub Pages at
[mcweaponry.com](https://mcweaponry.com).

## Local development

```sh
npm install
npm run dev        # http://localhost:5173
npm run build      # production build into dist/
npm run preview    # serve dist/ locally to check the build
```

## Deploying

The live site is served from the **`gh-pages` branch**, not `main`. Merging a
PR does not update the site; someone has to deploy from their machine:

```sh
git checkout main && git pull
npm run build && npm run deploy
```

Things to know:

- **Always build first.** `npm run deploy` only runs `gh-pages -d dist`, so it
  publishes whatever `dist/` is on disk, stale or not.
- **The whole `gh-pages` branch is replaced by `dist/` on every deploy.** The
  custom domain survives only because `public/CNAME` is copied into `dist/`.
  Don't move or delete it, or mcweaponry.com stops resolving to the site
  until it's re-added under repo Settings → Pages.
- **Everything in `public/` on your machine ships**, including files that are
  gitignored (such as `public/images/deprecated/`).
- GitHub Pages usually picks up a deploy within a minute or two.

## Project layout

```
index.html               Page shell, fonts, SEO + link-preview meta tags
public/                  Served as-is from the site root
  CNAME                  Custom domain (must stay here, see Deploying)
  og-image.png           Link-preview image (1200×630)
  images/                Hero, gallery and team photos (.webp)
src/
  App.svelte             Page sections and most styles
  app.css                Global base styles (leftover Vite template CSS)
  lib/Header.svelte      Fixed nav bar + mobile menu
  lib/LogoIntro.svelte   Scroll-driven logo intro / hero
  assets/mcw-logo.svg    Logo used by the intro
```

## Logo intro (`src/lib/LogoIntro.svelte`)

The hero is a pinned [GSAP ScrollTrigger](https://gsap.com/docs/v3/Plugins/ScrollTrigger/)
sequence. The logo assembles on a white surface, then crossfades into the dark
photo hero while the black linework turns white, and finally the subtitle and
tagline fade in and the page unpins into the Introduction section.

- **Swapping the logo:** replace `src/assets/mcw-logo.svg`. The file must keep
  the top-level groups `#letter-m`, `#letter-c`, `#text-weaponry` (class
  `logo-dark-element`), `#Crown`, `#spark` and `#eyes-xx`. IDs are
  case-sensitive and are mapped in the `SEL` object near the top of the
  script.
- **Colours:** the SVG's baked-in black (`#030404`) and pink (`#cc3493`) are
  swapped at import time for `currentColor` and `--logo-accent`. If a new
  export uses different hex values, update `SVG_INK` / `SVG_ACCENT`. The
  on-site pink is set by `--logo-accent` (currently `#e1007a`).
- **Background photo:** the `url()` in `.stage-dark`.
- **Timing:** `end: '+=200%'` is the pinned scroll distance. Timeline
  positions are relative units spread across that distance; the logo finishes
  assembling around the first 75vh.
- Visitors with *reduce motion* enabled get the finished hero with no pin.

## Link previews

The Open Graph / Twitter tags in `index.html` control what appears when the
URL is pasted into iMessage, Slack, WhatsApp, Discord, X, etc. Preview
crawlers don't run JavaScript, so these tags must stay in `index.html`.

- The image is `public/og-image.png`: 1200×630 PNG, logo kept inside the
  centre square because some apps crop to a square thumbnail. Keep it under
  ~300 KB (WhatsApp's limit).
- Apps cache previews for days. After changing them, refresh via the
  [Facebook Sharing Debugger](https://developers.facebook.com/tools/debug/) or
  [LinkedIn Post Inspector](https://www.linkedin.com/post-inspector/);
  others update on their own schedule.

## Known issues

- `src/app.css` is mostly unused Vite starter CSS; `#app` still applies a
  1280px max-width and padding, which `LogoIntro` works around.
