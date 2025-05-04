---
layout: default
title: Credentials
permalink: /credentials/
---

<div class="credentials-index-page">
  <p style="text-align: center; color: #555; margin-bottom: 3em;">Explore my certifications and what others have to say.</p>

  <div class="credentials-grid">
    <div class="credential-box">
      <h2>
        <a href="{{ '/credentials/certifications/' | relative_url }}">Certifications</a>
      </h2>
      <p>View my earned certifications.</p>
      <a href="{{ '/credentials/certifications/' | relative_url }}">Learn More</a>
    </div>

    <div class="credential-box">
      <h2>
        <a href="{{ '/credentials/feedbacks/' | relative_url }}">Feedbacks</a>
      </h2>
      <p>Read what others have to say.</p>
      <a href="{{ '/credentials/feedbacks/' | relative_url }}">See Feedbacks</a>
    </div>

    <div class="credential-box">
      <h2>
        <a href="{{ '/credentials/archives/' | relative_url }}">History of Learning</a>
      </h2>
      <p>Glance at my history of learning.</p>
      <a href="{{ '/credentials/archives/' | relative_url }}">Learn More</a>
    </div>
  </div>
</div>

<style>
  .credentials-grid {
    display: flex;
    justify-content: center;
    gap: 30px;
    flex-wrap: wrap;
  }

  .credential-box {
    flex: 1 1 250px;
    max-width: 300px;
    padding: 20px;
    margin-bottom: 20px;
    border-radius: 8px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.08);
    transition: transform 0.3s ease-in-out;
    text-align: center;
  }

  .credential-box h2 {
    color: #333;
    margin-bottom: 1em;
  }

  .credential-box a {
    color: #007bff;
    text-decoration: none;
    transition: color 0.3s ease;
  }

  .credential-box a:hover {
    color: #0056b3;
  }

  .credential-box:hover {
    transform: translateY(-5px);
    box-shadow: 0 6px 12px rgba(0, 0, 0, 0.12);
  }

  @media (max-width: 768px) {
    .credentials-grid {
      flex-direction: column;
      align-items: center;
    }

    .credential-box {
      width: 90%;
      max-width: none;
    }
  }
</style>