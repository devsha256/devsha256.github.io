---
layout: default
title: Projects
---

<div class="projects">
  <h1>Projects</h1>

  <div class="pagination" id="pagination-top">
    <button id="prev-button" disabled>Previous</button>
    <span id="current-page">1</span> / <span id="total-pages">1</span>
    <button id="next-button">Next</button>
  </div>

  <ul class="project-list">
    {% for project in site.data.projects %}
    <li class="project-item" data-skills="{{ project.slugified_skills }}">
      <h2 class="project-title">{{ project.title }}</h2>
      <p class="project-date">{{ project.date }}</p>
      <p class="project-company">
        <strong>Company:</strong> {{ project.company }}
      </p>
      <p class="project-description">{{ project.description }}</p>
      <p class="project-skills">
        <strong>Skills:</strong> {{ project.skills }}
      </p>
    </li>
    {% endfor %}
  </ul>
</div>

<style>
  .projects {
    font-family: Arial, sans-serif;
    margin: 20px;
  }

  .project-list {
    list-style: none;
    padding: 0;
  }

  .project-item {
    border: 1px solid #ddd;
    margin-bottom: 20px;
    padding: 10px;
    display: none;
  }

  .project-title {
    font-size: 1.5em;
    margin-bottom: 5px;
  }

  .project-date {
    font-size: 0.9em;
    color: #777;
    margin-bottom: 10px;
  }

  .project-company {
    font-weight: bold;
    margin-bottom: 5px;
  }

  .project-description {
    margin-bottom: 10px;
  }

  .project-skills {
    font-style: italic;
  }

  .pagination {
    margin: 20px 0;
    text-align: center;
  }

  .pagination button {
    padding: 8px 15px;
    margin: 0 5px;
    cursor: pointer;
  }
</style>

<script>
  document.addEventListener('DOMContentLoaded', function () {
    const allItems = Array.from(document.querySelectorAll('.project-item'));
    const prevButton = document.getElementById('prev-button');
    const nextButton = document.getElementById('next-button');
    const currentPageSpan = document.getElementById('current-page');
    const totalPagesSpan = document.getElementById('total-pages');

    const urlParams = new URLSearchParams(window.location.search);
    const skillParam = urlParams.get('skill')?.toLowerCase();

    let filteredItems = allItems;

    if (skillParam) {
      filteredItems = allItems.filter(item => {
        const skills = item.dataset.skills.toLowerCase().split(',');
        return skills.includes(skillParam);
      });
    }

    let currentPage = 1;
    const itemsPerPage = 1;
    let totalPages = Math.ceil(filteredItems.length / itemsPerPage);

    function showPage(page) {
      filteredItems.forEach((item, i) => {
        item.style.display = (i >= (page - 1) * itemsPerPage && i < page * itemsPerPage) ? 'block' : 'none';
      });

      currentPage = page;
      currentPageSpan.textContent = currentPage;
      totalPagesSpan.textContent = totalPages;

      prevButton.disabled = currentPage === 1;
      nextButton.disabled = currentPage === totalPages;
    }

    prevButton.addEventListener('click', () => {
      if (currentPage > 1) showPage(currentPage - 1);
    });

    nextButton.addEventListener('click', () => {
      if (currentPage < totalPages) showPage(currentPage + 1);
    });

    if (filteredItems.length > 0) {
      showPage(1);
    } else {
      currentPageSpan.textContent = 0;
      totalPagesSpan.textContent = 0;
    }
  });
</script>
