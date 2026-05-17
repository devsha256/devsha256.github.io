---
layout: default
title: Skills & Tools
permalink: /skills/
nav_order: 3
---

<div class="skills-page">
  <div class="skills-header">
    <h1 class="skills-title">Skills & Tools</h1>
    <p class="skills-subtitle">Technologies I've used across projects. Click a tag to explore.</p>
  </div>

  <div class="skills-cloud" id="skills-cloud">
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

    {% for skill in all_skills %}
      <a href="/projects?skill={{ skill | slugify }}" class="md-chip skill-chip" data-skill="{{ skill | slugify }}">
        # {{ skill }}
      </a>
    {% endfor %}
  </div>
</div>

<div class="circle-effect" id="circleEffect"></div>

<style>
.skills-page {
  padding: 1.5rem 0 4rem;
}

.skills-header {
  margin-bottom: 2.5rem;
}

.skills-title {
  margin-bottom: 0.4rem;
}

.skills-subtitle {
  font-size: 0.95rem;
  color: var(--md-on-surface-variant);
}

.skills-cloud {
  display: flex;
  flex-wrap: wrap;
  gap: 0.6rem;
  align-items: flex-start;
}

.skill-chip {
  font-size: 0.875rem;
  padding: 0.4rem 1rem;
  font-family: var(--md-font-mono);
  transition: background var(--md-motion-quick), color var(--md-motion-quick),
              border-color var(--md-motion-quick), transform var(--md-motion-quick),
              box-shadow var(--md-motion-quick);
}

.skill-chip:hover {
  transform: translateY(-2px);
  box-shadow: 0 4px 14px rgba(124,111,205,0.3);
}

/* Ripple circle effect */
.circle-effect {
  position: fixed;
  border-radius: 50%;
  width: 90vmax;
  height: 90vmax;
  transform: translate(-50%, -50%) scale(0);
  transition: transform 0.8s ease-out, background-color 0.3s ease, opacity 0.8s ease-out 4s;
  z-index: -1;
  top: var(--circle-y, 50%);
  left: var(--circle-x, 50%);
  opacity: 0;
  pointer-events: none;
  background-color: var(--hover-color, transparent);
}

.circle-effect.active {
  opacity: 0.18;
  transform: translate(-50%, -50%) scale(1);
  transition: transform 0.8s ease-out, background-color 0.3s ease, opacity 0.4s ease-in;
}
</style>

<script>
  var BRIGHT_CHARS = '89ABCDEF';
  function getRandomBrightColor() {
    var color = '#';
    for (var i = 0; i < 6; i++) color += BRIGHT_CHARS[Math.floor(Math.random() * BRIGHT_CHARS.length)];
    return color;
  }

  document.querySelectorAll('.skill-chip').forEach(function(link) {
    link.addEventListener('mouseenter', function(e) {
      var color = getRandomBrightColor();
      document.documentElement.style.setProperty('--hover-color', color);

      var circle = document.getElementById('circleEffect');
      var rect = e.target.getBoundingClientRect();
      circle.style.setProperty('--circle-x', (rect.left + rect.width / 2) + 'px');
      circle.style.setProperty('--circle-y', (rect.top + rect.height / 2) + 'px');
      circle.classList.add('active');

      clearTimeout(circle._timer);
      circle._timer = setTimeout(function() { circle.classList.remove('active'); }, 4000);
    });

    link.addEventListener('mouseleave', function() {
      document.getElementById('circleEffect').classList.remove('active');
    });
  });
</script>