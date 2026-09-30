<script>
  // Same file as the intro logo (see LogoIntro.svelte), recoloured for the
  // dark header: white linework, site pink accents. An <img> rather than
  // inline markup so its IDs don't clash with the intro's animated copy.
  import rawLogo from '../assets/mcw-logo.svg?raw';

  const logoSrc = `data:image/svg+xml,${encodeURIComponent(
    rawLogo.replace(/#030404/gi, '#f5f5f5').replace(/#cc3493/gi, '#e1007a')
  )}`;

  let isOpen = false;

  function toggleMenu() {
    isOpen = !isOpen;
  }
</script>

<style>
  header {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    background: rgba(14, 14, 14, 0.8);
    backdrop-filter: blur(10px);
    z-index: 999;
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 2rem 2rem;
    transition: top 0.3s;
    box-sizing: border-box;
  }

  .logo {
    display: block;
    line-height: 0;
  }

  .logo img {
    display: block;
    height: 3rem;
    width: auto;
  }

  nav a {
    color: #f5f5f5;
    text-decoration: none;
    margin: 0 1rem;
    font-size: 1rem;
    transition: color 0.3s;
  }

  nav a:hover {
    color: #e63946;
  }

  /* A real <button> for keyboard and screen-reader users; the resets undo
     the global button styles in app.css. */
  .hamburger {
    display: none;
    cursor: pointer;
    z-index: 1001;
    padding: 0;
    border: 0;
    border-radius: 0;
    background: none;
  }

  /* Keep the focus ring for keyboard users, not after a tap or click. */
  .hamburger:focus:not(:focus-visible) {
    outline: none;
  }

  .hamburger span {
    display: block;
    width: 25px;
    height: 3px;
    background-color: #f5f5f5;
    margin: 5px 0;
    transition: 0.4s;
  }

  .mobile-nav {
    display: none;
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: #0e0e0e;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    /* Just under the header (999) so its close button stays on top. */
    z-index: 998;
  }

  .mobile-nav a {
    font-size: 2rem;
    margin: 1.5rem 0;
  }

  @media (max-width: 768px) {
    nav {
      display: none;
    }

    /* Stays in the header's flex row so it lines up with the logo; the
       header (z-index 999) already sits above the open menu. */
    .hamburger {
      display: block;
    }

    .mobile-nav.open {
      display: flex;
    }

    .hamburger.open .line1 {
      transform: rotate(-45deg) translate(-5px, 6px);
    }

    .hamburger.open .line2 {
      opacity: 0;
    }

    .hamburger.open .line3 {
      transform: rotate(45deg) translate(-5px, -6px);
    }
  }

  /* Short landscape screens (phones held sideways): 7rem of header is a
     third of the screen. LogoIntro.svelte offsets the hero card by this
     height (3.75rem). */
  @media (orientation: landscape) and (max-height: 500px) {
    header {
      padding: 0.75rem 2rem;
    }

    .logo img {
      height: 2.25rem;
    }

    /* At full size the five links need ~480px, so Home and Contact Us fell
       off the top and bottom of the (unscrollable) overlay. */
    .mobile-nav {
      box-sizing: border-box;
      padding-top: 3.75rem;
    }

    .mobile-nav a {
      font-size: 1.5rem;
      margin: 0.4rem 0;
    }
  }
</style>

<!-- .site-header is the hook LogoIntro uses to fade the header in with the
     hero copy. -->
<header class="site-header">
  <a href="/" class="logo"><img src={logoSrc} alt="MC Weaponry" /></a>

  <nav>
    <a href="#home">Home</a>
    <a href="#intro">Introduction</a>
    <a href="#gallery">Gallery</a>
    <a href="#team">Team</a>
    <a href="#contact">Contact Us</a>
  </nav>

  <button
    type="button"
    class="hamburger"
    class:open={isOpen}
    on:click={toggleMenu}
    aria-label={isOpen ? 'Close menu' : 'Open menu'}
    aria-expanded={isOpen}
    aria-controls="mobile-nav"
  >
    <span class="line1"></span>
    <span class="line2"></span>
    <span class="line3"></span>
  </button>
</header>

{#if isOpen}
  <div class="mobile-nav" id="mobile-nav" class:open={isOpen}>
    <a href="#home" on:click={toggleMenu}>Home</a>
    <a href="#intro" on:click={toggleMenu}>Introduction</a>
    <a href="#gallery" on:click={toggleMenu}>Gallery</a>
    <a href="#team" on:click={toggleMenu}>Team</a>
    <a href="#contact" on:click={toggleMenu}>Contact Us</a>
  </div>
{/if}
