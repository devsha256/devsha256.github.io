---
layout: default
title: Credentials - Archives
permalink: /credentials/archives/
nav_include: no
---

<div class="archives">

  <div class="pagination">
    <button id="prev-button" disabled>Previous</button>
    <span id="current-page">1</span> / <span id="total-pages"></span> <button id="next-button">Next</button>
  </div>

  <ul class="archive-grid">
    {% assign sorted_archives = site.data.archives | sort: 'date' %}
    {% for arch in sorted_archives %}
    <li class="archive-item" id="arch-{{ forloop.index }}">
      <a href="{{arch.cred_link}}" target="_blank">
        <img src="/assets/img/logos/{{ arch.image }}" alt="{{ arch.name }}" class="arch-logo" />
      </a>
      <h2 class="arch-name">{{ arch.name }}</h2>
      <p><strong>Authority:</strong> {{ arch.authority }}</p>
      <p><strong>Date:</strong> {{ arch.date }}</p>
      <p><strong>Credential ID:</strong> {{ arch.credential_id }}</p>
      <p class="verify-row">
        <strong>Verify it live:</strong>
        <a href="{{ arch.drive_link }}" target="_blank" class="stars-container" title="View Credential">
          <span class="stars">
            {% for i in (1..5) %}
            <svg class="star" viewBox="0 0 24 24" width="20" height="20" xmlns="http://www.w3.org/2000/svg">
              <path d="M12 .587l3.668 7.57L24 9.748l-6 5.848 1.415 8.258L12 19.771l-7.415 4.083L6 15.596 0 9.748l8.332-1.591z" />
            </svg>
            
            {% endfor %}
          </span>
        </a>
      </p>
    </li>
    {% endfor %}
  </ul>
    <div class="instruction" style="position: fixed; bottom: 0; left: 0; width: 100%; background-color: #f8f8f8; color: #555; padding: 10px; text-align: center; z-index: 1000; animation: ziggle 0.5s infinite alternate;">Click on the verify star to see a live document.</div>
</div>

<style>
  body{
    max-width: 100vmax;
  }
  .archives {
    font-family: Arial, sans-serif;
    margin: 20px;
  }

  .archive-grid {
    list-style: none;
    padding: 0;
    display: grid;
    grid-template-columns: repeat(3, 1fr); /* 3 columns */
    grid-gap: 20px;
  }

  .archive-item {
    display: none;
    border: 1px solid #ddd;
    border-radius: 8px;
    padding: 15px;
    margin-bottom: 0; /* Remove bottom margin */
    position: relative; /* For logo positioning */
    min-height: 200px; /* Minimum height to ensure consistent layout */
  }

  .arch-logo {
    max-width: 80px;
    height: auto;
    position: absolute;
    bottom: 10px;
    right: 10px;
  }

  .arch-name {
    margin-top: 0;
  }

  .pagination {
    text-align: center;
    margin: 20px 0;
  }

  .pagination button {
    padding: 8px 15px;
    margin: 0 5px;
    cursor: pointer;
  }

  .verify-row {
    margin-top: 10px;
    font-size: 1rem;
  }

  .stars-container {
    display: inline-block;
    position: relative;
    overflow: hidden;
    text-decoration: none;
    height: 20px;
    margin-left: 5px;
  }

  .stars {
    display: flex;
    width: 100px;
    height: 20px;
  }

  .star {
    fill: #ccc;
    transition: fill 0.3s ease;
    margin: 0 2px;
  }

  .stars-container:hover .star {
    fill: gold;
  }
  @keyframes ziggle {
    0% {
      transform: translateX(-5px);
    }
    100% {
      transform: translateX(5px);
    }
  }

  .star-animated {
    animation: ziggle 0.5s infinite alternate;
  }

  .star-paused {
    animation-play-state: paused;
  }
</style>

<script>
  document.addEventListener("DOMContentLoaded", function () {
    const items = document.querySelectorAll(".archive-item");
    const prevButton = document.getElementById("prev-button");
    const nextButton = document.getElementById("next-button");
    const currentPageSpan = document.getElementById("current-page");
    const totalPagesSpan = document.getElementById("total-pages");
    const starElements = document.querySelectorAll('.stars svg'); // Select all star SVGs

    starElements.forEach(star => {
      star.addEventListener('mouseenter', () => {
        instructionDiv.style.animationPlayState = 'paused';
      });

      star.addEventListener('mouseleave', () => {
        instructionDiv.style.animationPlayState = 'running';
      });
    });

    const PAGE_SIZE = 6; // 6 items per page
    const ITEMS_PER_ROW = 3;

    let currentPage = 1;
    const totalPages = Math.ceil(items.length / PAGE_SIZE);

    function showPage(pageNumber) {
      const startIndex = (pageNumber - 1) * PAGE_SIZE;
      const endIndex = Math.min(startIndex + PAGE_SIZE, items.length);

      items.forEach((item, i) => {
        item.style.display = i >= startIndex && i < endIndex ? "block" : "none";
      });

      currentPageSpan.textContent = pageNumber;
      totalPagesSpan.textContent = totalPages;
      prevButton.disabled = pageNumber === 1;
      nextButton.disabled = pageNumber === totalPages;
    }

    function nextPage() {
      if (currentPage < totalPages) {
        currentPage++;
        showPage(currentPage);
      }
    }

    function prevPage() {
      if (currentPage > 1) {
        currentPage--;
        showPage(currentPage);
      }
    }

    nextButton.addEventListener("click", nextPage);
    prevButton.addEventListener("click", prevPage);

    // Initialize the totalPagesSpan with the correct value
    totalPagesSpan.textContent = totalPages;

    if (totalPages > 0) showPage(1);
  });
</script>