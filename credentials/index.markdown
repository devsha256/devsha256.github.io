---
layout: default
title: Credentials
permalink: /credentials/
---

<div class="credentials-index-page">
  <h1 style="text-align: center; color: #333; margin-bottom: 2em;">Credentials</h1>
  <p style="text-align: center; color: #555; margin-bottom: 3em;">Explore my certifications and what others have to say.</p>
  <div style="display: flex; justify-content: center; gap: 30px;">
    <div class="credential-box" style="padding: 20px; border-radius: 8px; box-shadow: 0 4px 8px rgba(0, 0, 0, 0.08); transition: transform 0.3s ease-in-out;">
      <h2 style="color: #333; margin-bottom: 1em; text-align: center;">
        <a href="{{ '/credentials/certifications/' | relative_url }}" style="text-decoration: none; color: inherit;">Certifications</a>
      </h2>
      <p style="color: #555; text-align: center;">View my earned certifications.</p>
      <a href="{{ '/credentials/certifications/' | relative_url }}" style="display: block; text-align: center; margin-top: 1.5em; color: #007bff; text-decoration: none; transition: color 0.3s ease;">Learn More</a>
    </div>
    <div class="credential-box" style="padding: 20px; border-radius: 8px; box-shadow: 0 4px 8px rgba(0, 0, 0, 0.08); transition: transform 0.3s ease-in-out;">
      <h2 style="color: #333; margin-bottom: 1em; text-align: center;">
        <a href="{{ '/credentials/feedbacks/' | relative_url }}" style="text-decoration: none; color: inherit;">Feedbacks</a>
      </h2>
      <p style="color: #555; text-align: center;">Read what others have to say.</p>
      <a href="{{ '/credentials/feedbacks/' | relative_url }}" style="display: block; text-align: center; margin-top: 1.5em; color: #007bff; text-decoration: none; transition: color 0.3s ease;">See Feedbacks</a>
    </div>
    <div class="credential-box" style="padding: 20px; border-radius: 8px; box-shadow: 0 4px 8px rgba(0, 0, 0, 0.08); transition: transform 0.3s ease-in-out;">
      <h2 style="color: #333; margin-bottom: 1em; text-align: center;">
        <a href="{{ '/credentials/archives/' | relative_url }}" style="text-decoration: none; color: inherit;">History of Learning</a>
      </h2>
      <p style="color: #555; text-align: center;">Glance at my history of learning.</p>
      <a href="{{ '/credentials/archives/' | relative_url }}" style="display: block; text-align: center; margin-top: 1.5em; color: #007bff; text-decoration: none; transition: color 0.3s ease;">Learn More</a>
    </div>
  </div>
</div>

<style>
  .credential-box:hover {
    transform: translateY(-5px);
    box-shadow: 0 6px 12px rgba(0, 0, 0, 0.12);
  }
  .credential-box a:hover {
    color: #0056b3;
  }
</style>