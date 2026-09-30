<script>
  import { onMount } from 'svelte';
  import { gsap } from 'gsap';
  import { ScrollTrigger } from 'gsap/ScrollTrigger';

  // ---------------------------------------------------------------------------
  // SWAPPING THE SVG
  // Drop a new export over src/assets/mcw-logo.svg (or change this import path).
  // Vite's `?raw` suffix imports the file as a string so it can be inlined and
  // each group animated individually.
  //
  // The file must keep these top-level groups (IDs are case-sensitive and must
  // match the SEL map below):
  //   #letter-m, #letter-c, #text-weaponry   -> class="logo-dark-element"
  //   #Crown, #spark, #eyes-xx               -> pink accents
  // ---------------------------------------------------------------------------
  import rawLogo from '../assets/mcw-logo.svg?raw';

  // Colours baked into the exported SVG. They're swapped for CSS hooks below so
  // the black linework can morph to white and the accent pink is set in one
  // place. If a new export uses different hex values, update these two.
  const SVG_INK = /#030404/gi; // linework black
  const SVG_ACCENT = /#cc3493/gi; // pink accents

  const logoMarkup = rawLogo
    .replace(SVG_INK, 'currentColor') // follows the CSS `color` of each group
    .replace(SVG_ACCENT, 'var(--logo-accent)')
    .replace('<svg ', '<svg class="logo-svg" aria-hidden="true" focusable="false" ');

  // Group selectors. These match the IDs in the current file ("Crown" is
  // capitalised and "spark" is singular there). Change them here if a future
  // export renames anything.
  const SEL = {
    m: '#letter-m',
    c: '#letter-c',
    crown: '#Crown',
    eyes: '#eyes-xx',
    spark: '#spark',
    text: '#text-weaponry',
    dark: '.logo-dark-element'
  };

  let root;
  let bleed;

  // Stretch the wrapper edge to edge. #app (src/app.css) is a centred
  // max-width box with padding, so measure where the wrapper actually lands and
  // pull it back to the viewport's left edge. Runs before every ScrollTrigger
  // refresh (load, resize) so the pin always measures the full-bleed size.
  function fitBleed() {
    bleed.style.marginLeft = '0px';
    bleed.style.width = 'auto';
    const left = bleed.getBoundingClientRect().left + window.scrollX;
    bleed.style.marginLeft = `${-left}px`;
    bleed.style.width = `${document.documentElement.clientWidth}px`;
  }

  onMount(() => {
    gsap.registerPlugin(ScrollTrigger);

    fitBleed();

    // Honour reduced motion: skip the sequence and show the finished hero.
    if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
      root.classList.add('is-static');
      window.addEventListener('resize', fitBleed);
      return () => window.removeEventListener('resize', fitBleed);
    }

    ScrollTrigger.addEventListener('refreshInit', fitBleed);

    // gsap.context scopes every selector to this component and lets us revert
    // all tweens + the pin when the component is destroyed (HMR included).
    const ctx = gsap.context(() => {
      // ---- Deconstructed start state -------------------------------------
      gsap.set(SEL.m, { xPercent: -60, opacity: 0 });
      gsap.set(SEL.c, { xPercent: 60, opacity: 0 });
      gsap.set(SEL.crown, { yPercent: -220, rotation: -18, opacity: 0, transformOrigin: '50% 100%' });
      gsap.set(SEL.eyes, { scale: 3, opacity: 0, transformOrigin: '50% 50%' });
      gsap.set(SEL.spark, { scale: 0, transformOrigin: '0% 100%' }); // bottom-left
      gsap.set(SEL.text, { yPercent: 120, opacity: 0 });
      gsap.set(SEL.dark, { color: '#000000' });

      const tl = gsap.timeline({
        defaults: { ease: 'power3.out' },
        scrollTrigger: {
          trigger: root,
          start: 'top top',
          end: '+=225%', // scroll distance while pinned (~225vh)
          pin: true,
          scrub: 1, // 1s of smoothing between scroll position and playhead
          anticipatePin: 1
        }
      });

      // ---- Phase 1: assembly on the light surface -------------------------
      // Timeline positions are arbitrary units; with scrub they're mapped
      // proportionally across the pinned scroll distance.
      tl.to('.scroll-cue', { opacity: 0, duration: 0.3, ease: 'none' }, 0)
        .to(SEL.m, { xPercent: 0, opacity: 1, duration: 1 }, 0)
        .to(SEL.c, { xPercent: 0, opacity: 1, duration: 1 }, 0.15)
        .to(SEL.crown, { yPercent: 0, rotation: 0, opacity: 1, duration: 1, ease: 'back.out(1.6)' }, 0.7)
        // Stamp: drop from 3x, overshoot below 1, settle. The opacity snaps in
        // quickly so it reads as an impact rather than a fade.
        .to(SEL.eyes, { opacity: 1, duration: 0.1, ease: 'none' }, 1.35)
        .to(SEL.eyes, { scale: 1, duration: 0.6, ease: 'back.out(4)' }, 1.35)
        .to(SEL.spark, { scale: 1, duration: 0.5, ease: 'back.out(2.5)' }, 1.7)
        .to(SEL.text, { yPercent: 0, opacity: 1, duration: 0.8 }, 1.6);

      // ---- Phase 2: morph + reveal ---------------------------------------
      // Background crossfades to the photo while the linework goes black ->
      // white. Pink accents aren't touched, so they stay pink throughout.
      tl.to('.stage-dark', { opacity: 1, duration: 1, ease: 'power1.inOut' }, 2.6)
        .to(SEL.dark, { color: '#ffffff', duration: 1, ease: 'power1.inOut' }, 2.6)
        .to('.hero-card', { '--card-alpha': 0.4, duration: 1, ease: 'power1.inOut' }, 2.8);

      // ---- Phase 3: hand-off to the live hero ----------------------------
      tl.to('.hero-copy', { opacity: 1, y: 0, duration: 0.6, stagger: 0.2 }, 3.5)
        // Short hold so the finished hero rests before the pin releases.
        .to({}, { duration: 0.5 });
    }, root);

    return () => {
      ScrollTrigger.removeEventListener('refreshInit', fitBleed);
      ctx.revert();
    };
  });
</script>

<!-- id="home" keeps the nav's "Home" link working. -->
<div class="logo-intro-bleed" bind:this={bleed}>
<section class="logo-intro" id="home" bind:this={root}>
  <!-- Phase 1 surface: plain light background for maximum contrast. -->
  <div class="stage-light"></div>

  <!-- Phase 2 surface: the original dark hero photo + overlay.
       SWAPPING THE BACKGROUND: change the url() in .stage-dark below
       (files in /public are served from the site root). -->
  <div class="stage-dark">
    <div class="overlay"></div>
  </div>

  <div class="hero-card">
    <!-- The logo replaces the old <h1> visually; the h1 stays for SEO and
         screen readers. -->
    <h1 class="sr-only">MC Weaponry</h1>
    <div class="logo">{@html logoMarkup}</div>
    <p class="hero-copy">07/02FFL • Founded by ACGG Master Engraver Madeline Crumling</p>
    <p class="hero-copy">We produce the finest in hand engraved firearms</p>
  </div>

  <div class="scroll-cue" aria-hidden="true">Scroll</div>
</section>
</div>

<style>
  .logo-intro {
    --logo-accent: #e1007a;
    position: relative;
    height: 100vh;
    height: 100svh;
    /* Overrides the global `section` padding in App.svelte. */
    padding: 0;
    overflow: hidden;
    display: flex;
    align-items: center;
    justify-content: center;
    text-align: center;
  }

  /* Horizontal breakout is set in fitBleed(); this cancels #app's top
     padding so the stage starts at the very top of the page. */
  .logo-intro-bleed {
    margin-top: -2rem;
  }

  .stage-light,
  .stage-dark {
    position: absolute;
    inset: 0;
  }

  .stage-light {
    background: #ffffff;
  }

  .stage-dark {
    background: #0e0e0e url('/images/gunhands.webp') center / cover no-repeat;
    opacity: 0;
  }

  .overlay {
    position: absolute;
    inset: 0;
    background: rgba(0, 0, 0, 0.4);
  }

  .hero-card {
    --card-alpha: 0; /* transparent on white, animated to 0.4 over the photo */
    position: relative;
    z-index: 2;
    width: min(90vw, 720px);
    box-sizing: border-box;
    padding: 1.5rem;
    border-radius: 8px;
    background: rgba(0, 0, 0, var(--card-alpha));
    backdrop-filter: blur(2px);
  }

  .logo {
    width: min(100%, 560px);
    margin: 0 auto 1rem;
  }

  /* The SVG is injected with {@html}, so it needs :global() to be styled. */
  .logo :global(.logo-svg) {
    display: block;
    width: 100%;
    height: auto;
    overflow: visible; /* lets the crown/letters travel in from outside */
  }

  /* Linework starts black (paths use currentColor; body text is light). */
  .logo :global(.logo-dark-element) {
    color: #000000;
  }

  .hero-copy {
    opacity: 0;
    transform: translateY(12px);
  }

  .hero-copy:last-child {
    margin-bottom: 0;
  }

  /* Reduced-motion end state (no pin, no scrub). .is-static is added at
     runtime, so it's wrapped in :global() to stop Svelte pruning it. */
  :global(.is-static) .stage-dark {
    opacity: 1;
  }
  :global(.is-static) .hero-card {
    --card-alpha: 0.4;
  }
  :global(.is-static) .hero-copy {
    opacity: 1;
    transform: none;
  }
  :global(.is-static) .logo :global(.logo-dark-element) {
    color: #ffffff;
  }

  .scroll-cue {
    position: absolute;
    bottom: 2rem;
    left: 50%;
    transform: translateX(-50%);
    z-index: 2;
    font-size: 0.75rem;
    letter-spacing: 0.3em;
    text-transform: uppercase;
    color: #555;
  }

  .scroll-cue::after {
    content: '';
    display: block;
    width: 1px;
    height: 2.5rem;
    margin: 0.75rem auto 0;
    background: currentColor;
    animation: cue 1.8s ease-in-out infinite;
    transform-origin: top;
  }

  @keyframes cue {
    0% { transform: scaleY(0); }
    50% { transform: scaleY(1); }
    100% { transform: scaleY(1); opacity: 0; }
  }

  :global(.is-static) .scroll-cue {
    display: none;
  }

  .sr-only {
    position: absolute;
    width: 1px;
    height: 1px;
    padding: 0;
    margin: -1px;
    overflow: hidden;
    clip: rect(0, 0, 0, 0);
    white-space: nowrap;
    border: 0;
  }

  @media (max-width: 768px) {
    .hero-card {
      padding: 1rem;
    }
    .hero-copy {
      font-size: 0.95rem;
    }
  }
</style>
