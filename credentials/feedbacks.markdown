---
layout: default
title: Credentials - Feedbacks
permalink: /credentials/feedbacks/
---
<div class="feedbacks">

  <div class="pagination">
    <button id="prev-button" disabled>Previous</button>
    <span id="current-page">1</span> / <span id="total-pages">{{ site.data.feedbacks | size }}</span>
    <button id="next-button">Next</button>
  </div>

  <ul class="feedback-list">
    {% assign sorted_feedbacks = site.data.feedbacks | sort: 'date' | reverse %}
    {% for cert in sorted_feedbacks %}
    <li class="feedback-item" id="cert-{{ forloop.index }}">
      <a href="{{cert.cred_link}}" target="_blank">
        <img src="/assets/img/logos/{{ cert.image }}" alt="{{ cert.name }}" class="cert-logo" />
      </a>
      <h2 class="cert-name">{{ cert.name }}</h2>
      <p><strong>Authority:</strong> {{ cert.authority }}</p>
      <p><strong>Date:</strong> {{ cert.date }}</p>
      <p><strong>Credential ID:</strong> {{ cert.credential_id }}</p>
      <p class="verify-row">
        <strong>Verify it live:</strong>
        <a href="{{ cert.drive_link }}" target="_blank" class="stars-container" title="View Credential">
          <span class="stars">
            {% for i in (1..5) %}
            <svg class="star" viewBox="0 0 24 24" width="26" height="26" xmlns="http://www.w3.org/2000/svg">
              <path d="M12 .587l3.668 7.57L24 9.748l-6 5.848 1.415 8.258L12 19.771l-7.415 4.083L6 15.596 0 9.748l8.332-1.591z" />
            </svg>
            
            {% endfor %}
          </span>
        </a>
      </p>
    </li>
    {% endfor %}
  </ul>
    <div class="instruction" style="position: fixed; bottom: 0; left: 0; width: 100%; background-color: #f8f8f8; color: #555; padding: 10px; text-align: center; z-index: 1000; animation: ziggle 0.5s infinite alternate;">Click on the verify star to see a live document</div>
</div>

<style>
  .feedbacks {
    font-family: Arial, sans-serif;
    margin: 20px;
  }

  .feedback-list {
    list-style: none;
    padding: 0;
  }

  .feedback-item {
    display: none;
    border-bottom: 2px solid #ddd;
    padding: 15px;
    margin-bottom: 20px;
  }

  .cert-logo {
    margin-top: 20px;
    max-width: 100px;
    height: auto;
    float: right;
  }

  .feed-name{
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
    const items = document.querySelectorAll(".feedback-item");
    const prevButton = document.getElementById("prev-button");
    const nextButton = document.getElementById("next-button");
    const currentPageSpan = document.getElementById("current-page");
    const totalPagesSpan = document.getElementById("total-pages");
    const starElements = document.querySelectorAll('.stars svg'); // Select all star SVGs

    let currentPage = 1;
    const totalPages = items.length;

    function showPage(index) {
      items.forEach((item, i) => {
        item.style.display = i === index ? "block" : "none";
      });

      currentPageSpan.textContent = currentPage;
      totalPagesSpan.textContent = totalPages;
      prevButton.disabled = currentPage === 1;
      nextButton.disabled = currentPage === totalPages;
    }

    function nextPage() {
      if (currentPage < totalPages) {
        currentPage++;
        showPage(currentPage - 1);
      }
    }

    function prevPage() {
      if (currentPage > 1) {
        currentPage--;
        showPage(currentPage - 1);
      }
    }

    nextButton.addEventListener("click", nextPage);
    prevButton.addEventListener("click", prevPage);

    if (totalPages > 0) showPage(0);

      starElements.forEach(star => {
        star.addEventListener('mouseenter', () => {
          instructionDiv.style.animationPlayState = 'paused';
        });

        star.addEventListener('mouseleave', () => {
          instructionDiv.style.animationPlayState = 'running';
        });
    });
  });
</script>