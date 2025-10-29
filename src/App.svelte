<script>
  import Header from './lib/Header.svelte';
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
  :global(html) {
    scroll-behavior: smooth;
  }
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
    margin-top: 70px;
  }

  .hero .overlay {
    position: absolute;
    inset: 0;
    background: rgba(0, 0, 0, 0.4);
    z-index: 1;
  }

  .hero-content {
    background: rgba(0, 0, 0, 0.4);
    backdrop-filter: blur(2px);
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
    padding-top: 0rem;
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

    .hero {
      height: 30vh;
    }
  }

  @media (max-width: 1024px) {
    .gallery {
      grid-template-columns: 1fr;
    }

    .hero {
      height: 15vh;
    }

    .team-cards {
      flex-direction: column;
    }

    .team-card {
      flex-basis: 100%;
    }
    .team-card-madeline {
      order: 1;
    }
    .team-card-scarlett {
      order: 2;
    }
    .team-card-jasmine {
      order: 3;
    }
  }

  /* Sections */
  section {
    padding: 0rem 2rem;
    padding-top: 8rem;
    text-align: center;
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

  /* Team Section */
  .team-cards {
    display: flex;
    justify-content: space-around;
    gap: 2rem;
    margin-top: 2rem;
  }

  .team-card {
    background: #1a1a1a;
    padding: 2rem;
    border-radius: 8px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
    flex-basis: 30%;
  }

  @media (min-width: 1025px) {
    .team-card-scarlett {
      order: 1;
    }
    .team-card-madeline {
      order: 2;
    }
    .team-card-jasmine {
      order: 3;
    }
  }

  .team-card h3 {
    color: #e63946;
  }

  .team-card img {
    width: 100%;
    height: 300px;
    object-fit: contain;
    border-radius: 8px 8px 0 0;
    margin-bottom: 1.5rem;
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

<Header />

<!-- Hero Section -->
<section class="hero" id="home">
  <div class="overlay"></div>
  <div class="hero-content">
    <h1>MC Weaponry</h1>
    <p>07/02FFL • Founded by ACGG Master Engraver Madeline Crumling</p>
    <p>We produce the finest in hand engraved firearms</p>
  </div>
</section>

<!-- Introduction Section -->
<section id="intro">
  <h2>Introduction</h2>
  <p>
    For almost a decade, M.C. Weaponry has been serving the York/Lancaster area with top notch engraving and gunsmithing services. Founded in 2017 by ACGG Master Hand Engraver and Gunsmith Madeline Crumling, we pride ourselves on producing the finest custom firearms on the market.
  </p>
  <p>
    Have an idea for a project you want to make a reality? Send an email to <a href="mailto:scarlett@mcweaponry.com">scarlett@mcweaponry.com</a> for a consultation, and we’d love to try and make your dreams a reality.
  </p>
</section>

<!-- Gallery Section -->
<section id="gallery">
<h2>Gallery</h2>
  <section class="gallery">
    {#each galleryImages as image (image)}
      <img src={`/images/${image}`} alt="{image}" class="gallery-image" />
    {/each}
  </section>
</section>

<!-- Team Section -->
<section id="team">
  <h2>Our Team</h2>
  <div class="team-cards">
    <div class="team-card team-card-madeline">
      <img src="/images/madeline-photo.webp" alt="Madeline Crumling" />
      <h3>Madeline Crumling - Owner, Master Hand Engraver and Gunsmith</h3>
      <p>Contact: <a href="mailto:madeline@mcweaponry.com">madeline@mcweaponry.com</a></p>
      <p>For her entire life, Madeline has had a strong passion for firearms and took the leap in 2017 to start what we know today as M.C. Weaponry. Over the years she has served clients all around the world with her expert craftsmanship and acute attention to detail. In 2023, her immense talent earned her a seat in the American Custom Gunmakers Guild as a Professional Member for her outstanding hand engraving.</p>
      <p><em>Fun fact: Madeline was once featured on an episode of “Master of Arms” on the Discovery Channel!</em></p>
    </div>
    <div class="team-card team-card-scarlett">
      <img src="/images/scarlett-photo.webp" alt="Scarlett C." />
      <h3>Scarlett C. - Office Manager</h3>
      <p>Contact: <a href="mailto:scarlett@mcweaponry.com">scarlett@mcweaponry.com</a></p>
      <p>The backbone of the operation, Scarlett can usually be found on her laptop emailing clients or in the workshop as a spare pair of hands. If you’ve ever had the pleasure of working with us then you know just how kind and professional she is when it comes to customer relations. In her free time, Scarlett likes to shoot local 2-Gun and USPSA matches, as well as routinely experience heartbreak and despair as a diehard fan of the Philadelphia Phillies.</p>
      <p><em>Fun fact: Scarlett used to play Magic: the Gathering professionally!</em></p>
    </div>
    <div class="team-card team-card-jasmine">
      <img src="/images/jasmine-photo.webp" alt="Jasmine C." />
      <h3>Jasmine C. - Apprentice Hand Engraver and Gunsmith</h3>
      <p>Contact: <a href="mailto:jasmine@mcweaponry.com">jasmine@mcweaponry.com</a></p>
      <p>Starting her Apprenticeship in March of 2025, Jasmine has quickly proven herself as an extremely valuable member of the team. In Madeline’s own words, “She’s taken to the craft of custom weapon making faster than anyone I’ve ever mentored in my career.”</p>
      <p>If you see her, be sure to ask her about her opinions on various lever action rifles or the exact specifications of an Acro footprint and she’ll be sure to talk your ear off.</p>
      <p><em>Fun fact: Jasmine used to be a professional astrophotographer!</em></p>
    </div>
  </div>
</section>

<!-- Contact Section -->
<section class="contact-section" id="contact">
  <h2>Contact Us</h2>
  <p>Address: 854 Country Ln York PA 17406</p>
  <p>Business Hours: By Appointment Only</p>
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
