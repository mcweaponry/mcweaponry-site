<script>
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
    padding: 1rem 2rem;
    transition: top 0.3s;
  }

  .logo {
    font-family: 'Anton', sans-serif;
    font-size: 1.5rem;
    color: #f5f5f5;
    text-decoration: none;
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

  .hamburger {
    display: none;
    cursor: pointer;
    z-index: 1001;
  }

  .hamburger div {
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
    z-index: 1000;
  }

  .mobile-nav a {
    font-size: 2rem;
    margin: 1.5rem 0;
  }

  @media (max-width: 768px) {
    nav {
      display: none;
    }

    .hamburger {
      display: block;
      position: fixed;
      top: 1rem;
      right: 2rem;
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
</style>

<header>
  <a href="/" class="logo">MC Weaponry</a>

  <nav>
    <a href="#home">Home</a>
    <a href="#intro">Introduction</a>
    <a href="#gallery">Gallery</a>
    <a href="#team">Team</a>
    <a href="#contact">Contact Us</a>
  </nav>

  <div class="hamburger" on:click={toggleMenu} class:open={isOpen}>
    <div class="line1"></div>
    <div class="line2"></div>
    <div class="line3"></div>
  </div>
</header>

{#if isOpen}
  <div class="mobile-nav" class:open={isOpen}>
    <a href="#home" on:click={toggleMenu}>Home</a>
    <a href="#intro" on:click={toggleMenu}>Introduction</a>
    <a href="#gallery" on:click={toggleMenu}>Gallery</a>
    <a href="#team" on:click={toggleMenu}>Team</a>
    <a href="#contact" on:click={toggleMenu}>Contact Us</a>
  </div>
{/if}
