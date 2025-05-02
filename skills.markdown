---
layout: default
title: Skills & Tools
permalink: /skills/
nav_order: 3
---

<div class="skills-page">
  <div class="skills-container">
    {% assign all_skills = "" | split: "" %}
    {% for project in site.data.projects %}
      {% assign skills_array = project.skills | split: "," %}
      {% for skill in skills_array %}
        {% assign clean_skill = skill | strip %}
        {% unless all_skills contains clean_skill %}
          {% assign all_skills = all_skills | push: clean_skill %}
        {% endunless %}
      {% endfor %}
    {% endfor %}
    {% assign all_skills = all_skills | sort %}

    <div>
      {% for skill in all_skills %}
        <span class="link-container">
          <a href="/projects?skill={{ skill | slugify }}" class="skill-link">#&nbsp;{{ skill }}</a>
        </span>
      {% endfor %}
    </div>
  </div>
</div>

<div class="circle" id="circleEffect"></div>

<style>
  .skills-page {
    font-family: Arial, sans-serif;
    margin: 20px;
    text-align: center;
    overflow: hidden; /* To contain the expanding circle */
    position: relative; /* For z-index context */
  }

  .skills-container {
    display: flex;
    justify-content: center;
    align-items: center;
    min-height: 300px;
    flex-wrap: wrap;
    gap: 10px;
    position: relative; /* To be above the circle */
    z-index: 2;
  }

  .skill-link {
    display: inline-block;
    padding: 8px 15px;
    margin: 5px;
    text-decoration: none;
    color: #003cff;
    font-size: 1.2em;
    position: relative;
    z-index: 3; /* Ensure text is above the circle */
    transition: color 0.3s ease;
  }

  .skill-link:hover {
    color: #003cff; /* Keep the link color the same */
    background-color: transparent;
  }

  .circle {
    position: fixed;
    background-color: var(--hover-color);
    border-radius: 50%;
    width: 95; /* Use vmax to cover both width and height */
    height: 95vmax; /* Use vmax to cover both width and height */
    transform: translate(-50%, -50%) scale(0); /* Center the circle */
    transition: transform 0.8s ease-out, background-color 0.3s ease, opacity 0.8s ease-out 5s; /* Add opacity transition with delay */
    z-index: 1; /* Below the skill links */
    top: var(--circle-y);
    left: var(--circle-x);
    opacity: 0; /* Start with 0 opacity */
    pointer-events: none;
  }

  .circle.active {
    opacity: 0.5; /* Fade in to 50% opacity */
    transform: translate(-50%, -50%) scale(1); /* Scale to cover the page */
    transition: transform 0.8s ease-out, background-color 0.3s ease, opacity 0.8s ease-in; /* Fade in animation */
  }
</style>

<script>
  function getRandomBrightColor() {
    const letters = '89ABCDEF';
    let color = '#';
    for (let i = 0; i < 6; i++) {
      color += letters[Math.floor(Math.random() * letters.length)];
    }
    return color;
  }

  document.querySelectorAll('.skill-link').forEach(link => {
    link.addEventListener('mouseenter', (e) => {
      const randomColor = getRandomBrightColor();
      document.documentElement.style.setProperty('--hover-color', randomColor);

      const circle = document.getElementById('circleEffect');
      const rect = e.target.getBoundingClientRect();
      const x = rect.left + rect.width / 2;
      const y = rect.top + rect.height / 2;

      // Set the starting position of the circle
      circle.style.setProperty('--circle-x', `${x}px`);
      circle.style.setProperty('--circle-y', `${y}px`);

      circle.classList.add('active');

      // Remove the active class after 5 seconds to trigger fade out
      setTimeout(() => {
        circle.classList.remove('active');
      }, 1500);
    });

link.addEventListener('mouseleave', () => {
      const circle = document.getElementById('circleEffect');
      // If the mouse leaves before the 5-second timer, remove the active class immediately
      circle.classList.remove('active');
    });
  });
</script>