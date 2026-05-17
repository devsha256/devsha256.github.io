---
layout: default
title: Projects
permalink: /projects/
---

<div class="projects-page">
  <div class="projects-header">
    <h1 class="projects-title">Projects</h1>
    <p class="projects-subtitle" id="projects-subtitle">Professional engagements & integrations I've led or contributed to.</p>
  </div>

  <div class="md-pagination" id="pagination-top">
    <button class="md-btn md-btn-outlined" id="prev-button" disabled>← Prev</button>
    <span class="page-info">
      <span id="current-page">1</span> / <span id="total-pages">1</span>
    </span>
    <button class="md-btn md-btn-outlined" id="next-button">Next →</button>
  </div>

  <ul class="project-list" id="project-list">
    {% for project in site.data.projects %}
    <li class="project-card" data-skills="{{ project.slugified_skills }}">
      <div class="project-card-header">
        <div class="project-meta">
          <span class="project-company-badge">{{ project.company }}</span>
          <span class="project-date">{{ project.date }}</span>
        </div>
        <h2 class="project-title">{{ project.title }}</h2>
      </div>
      <hr class="md-divider">
      <p class="project-description">{{ project.description }}</p>
      <div class="project-skills-row">
        {% assign skill_list = project.skills | split: "," %}
        {% assign slug_list  = project.slugified_skills | split: "," %}
        {% for skill in skill_list %}
          <a href="/projects?skill={{ slug_list[forloop.index0] }}"
             class="md-chip skill-ref-chip">{{ skill | strip }}</a>
        {% endfor %}
      </div>
    </li>
    {% endfor %}
  </ul>
</div>

<style>
.projects-page { padding: 1.5rem 0 4rem; }

.projects-header { margin-bottom: 2rem; }
.projects-title  { margin-bottom: 0.4rem; }
.projects-subtitle { font-size: 0.95rem; color: var(--md-on-surface-variant); }

/* Card */
.project-list { list-style: none; padding: 0; }

.project-card {
  display: none;
  background: var(--md-surface-container);
  border: 1px solid var(--md-outline-variant);
  border-radius: var(--md-shape-xl);
  padding: 1.75rem;
  margin-bottom: 1.5rem;
  animation: card-enter 0.35s var(--md-motion-emphasize);
}

@keyframes card-enter {
  from { opacity: 0; transform: translateY(12px); }
  to   { opacity: 1; transform: translateY(0); }
}

.project-card-header { margin-bottom: 0.75rem; }

.project-meta {
  display: flex;
  align-items: center;
  gap: 0.75rem;
  margin-bottom: 0.6rem;
  flex-wrap: wrap;
}

.project-company-badge {
  display: inline-flex;
  align-items: center;
  padding: 0.25rem 0.75rem;
  background: var(--md-primary-container);
  color: var(--md-on-primary-container);
  border-radius: var(--md-shape-full);
  font-size: 0.78rem;
  font-weight: 600;
}

.project-date {
  font-size: 0.8rem;
  color: var(--md-on-surface-variant);
}

.project-title {
  font-size: 1.2rem;
  font-weight: 700;
  color: var(--md-on-surface);
  margin: 0;
}

.project-description {
  color: var(--md-on-surface-variant);
  font-size: 0.93rem;
  line-height: 1.75;
  margin-bottom: 1.25rem;
}

.project-skills-row {
  display: flex;
  flex-wrap: wrap;
  gap: 0.4rem;
}

.skill-ref-chip {
  font-size: 0.75rem;
  padding: 0.25rem 0.7rem;
}

@media (max-width: 600px) {
  .project-card { padding: 1.25rem; }
}
</style>

<script>
document.addEventListener('DOMContentLoaded', function () {
  var allItems    = Array.from(document.querySelectorAll('.project-card'));
  var prevBtn     = document.getElementById('prev-button');
  var nextBtn     = document.getElementById('next-button');
  var currentSpan = document.getElementById('current-page');
  var totalSpan   = document.getElementById('total-pages');
  var subtitle    = document.getElementById('projects-subtitle');

  var urlParams  = new URLSearchParams(window.location.search);
  var skillParam = (urlParams.get('skill') || '').toLowerCase();

  var filtered = skillParam
    ? allItems.filter(function(item) {
        return item.dataset.skills.toLowerCase().split(',').includes(skillParam);
      })
    : allItems;

  if (skillParam && subtitle) {
    subtitle.innerHTML = 'Filtered by skill: <strong style="color:var(--md-primary)">' + skillParam.replace(/-/g,' ') + '</strong>';
  }

  var currentPage  = 1;
  var itemsPerPage = 1;
  var totalPages   = Math.max(1, Math.ceil(filtered.length / itemsPerPage));

  function showPage(page) {
    allItems.forEach(function(item) { item.style.display = 'none'; });
    filtered.forEach(function(item, i) {
      if (i >= (page - 1) * itemsPerPage && i < page * itemsPerPage) {
        item.style.display = 'block';
      }
    });
    currentPage = page;
    currentSpan.textContent = currentPage;
    totalSpan.textContent   = totalPages;
    prevBtn.disabled = currentPage === 1;
    nextBtn.disabled = currentPage === totalPages;
    window.scrollTo({ top: 0, behavior: 'smooth' });
  }

  prevBtn.addEventListener('click', function() { if (currentPage > 1) showPage(currentPage - 1); });
  nextBtn.addEventListener('click', function() { if (currentPage < totalPages) showPage(currentPage + 1); });

  if (filtered.length > 0) {
    showPage(1);
  } else {
    currentSpan.textContent = '0';
    totalSpan.textContent   = '0';
  }
});
</script>
