<script>
  import { fade } from 'svelte/transition';
  const galleryImages = [
    'top_left_gun.webp',
    'top_center_gun.webp',
    'top_right_gun.webp',
    'bottom_left_gun.webp',
    'bottom_center_gun.webp',
    'bottom_right_gun.webp'
  ];
</script>

<style>
  /* Global Typography */
  :global(body) {
    margin: 0;
    font-family: 'Inter', sans-serif;
    font-weight: 400;
    background-color: #0e0e0e;
    color: #f5f5f5;
    line-height: 1.6;
    font-size: 16px;
  }

  :global(h1),
  :global(h2),
  :global(h3),
  :global(h4) {
    margin: 0;
    font-family: 'Anton', sans-serif;
    font-weight: normal;
    text-transform: uppercase;
    letter-spacing: 1px;
  }

  :global(h1) {
    font-size: 3.5rem;
    line-height: 1.2;
    margin-bottom: 1rem;
  }

  :global(h2) {
    font-size: 2.5rem;
    margin-bottom: 1.5rem;
    position: relative;
  }

  :global(h2)::after {
    content: '';
    display: block;
    width: 80px;
    height: 3px;
    background: #e63946;
    margin: 0.5rem auto 0;
  }

  :global(h3) {
    font-size: 1.75rem;
    margin-bottom: 1rem;
  }

  :global(p) {
    font-family: 'Inter', sans-serif;
    font-size: 1.125rem;
    margin-bottom: 1.25rem;
    color: #ddd;
  }

  :global(a) {
    color: #e63946;
    text-decoration: none;
  }

  :global(a:hover) {
    text-decoration: underline;
  }

  /* Hero Section */
  .hero {
    position: relative;
    background-image: url('/images/gunhands.webp');
    background-size: cover;
    background-position: center;
    color: white;
    height: 60vh;
    display: flex;
    align-items: center;
    justify-content: center;
    text-align: center;
  }

  .hero .overlay {
    position: absolute;
    inset: 0;
    background: rgba(0, 0, 0, 0.4);
    z-index: 1;
  }

  .hero-content {
    background: rgba(0, 0, 0, 0.4);
    backdrop-filter: blur(6px);
    border-radius: 8px;
    padding: 1.5rem;
    z-index: 2;
  }

  .hero h1 {
    font-size: 3.5rem;
    letter-spacing: 2px;
  }

  /* Gallery Section */
  .gallery {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 1rem;
    margin: 4rem auto;
    width: 90%;
    max-width: 1200px;
  }

  .gallery img {
    width: 100%;
    height: 300px;
    object-fit: cover;
    border-radius: 8px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    transition: transform 0.3s ease;
  }

  .gallery img:hover {
    transform: scale(1.03);
  }

  @media (max-width: 1024px) {
    .gallery {
      grid-template-columns: repeat(2, 1fr);
    }
  }

  @media (max-width: 768px) {
    .gallery {
      grid-template-columns: 1fr;
    }
  }

  /* Sections */
  section {
    padding: 4rem 2rem;
  }

  .contact-section {
    background-color: #000;
    color: #f5f5f5;
    text-align: center;
    padding: 4rem 2rem;
  }

  .contact-section p {
    font-size: 1.2rem;
    line-height: 1.6;
  }

  /* Footer */
  footer {
    text-align: center;
    padding: 2rem 1rem;
    font-size: 0.85rem;
    color: #666;
    background-color: #111;
    margin-top: 4rem;
  }

  footer a {
    color: #999;
    margin: 0 0.5rem;
  }
</style>

<!-- Hero Section -->
<section class="hero">
  <div class="overlay"></div>
  <div class="hero-content">
    <h1>MC Weaponry</h1>
    <p>07/02FFL • Founded by ACGG Master Engraver Madeline Crumling</p>
    <p>We produce the finest in hand engraved firearms</p>
  </div>
</section>

<!-- Gallery Section -->
<section class="gallery">
  {#each galleryImages as image (image)}
    <img src={`/images/${image}`} alt="{image}" class="gallery-image" />
  {/each}
</section>

<!-- Contact Section -->
<section class="contact-section">
  <h2>Contact Us</h2>
  <p>Email <a href="mailto:scarlett@mcweaponry.com">scarlett@mcweaponry.com</a> for inquiries.</p>
</section>

<!-- Footer -->
<footer>
  <div>
    <a href="https://x.com/mcweaponry" target="_blank">@mcweaponry</a> |
    <a href="https://x.com/scarlettactual" target="_blank">@scarlettactual</a>
  </div>
  <div>© 2025 MC Weaponry</div>
</footer>
