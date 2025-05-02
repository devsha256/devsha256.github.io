---
layout: default
title: Credentials - Archives
permalink: /credentials/archives/
nav_include: no
---

<div class="archives">
<div class="search-container">
  <input type="text" id="search-input" placeholder="Search by name..." />
  <button id="filter-button" onclick="filterArchives()">Filter</button>
</div>


  <div class="pagination">
    <button id="prev-button" disabled>Previous</button>
    <span id="current-page">1</span> / <span id="total-pages"></span> <button id="next-button">Next</button>
  </div>

  <ul class="archive-grid">
    {% assign sorted_archives = site.data.archives | sort: 'date' | reverse %}
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
.search-container {
  text-align: center;
  margin-bottom: 20px;
}

#search-input {
  width: 60%;
  padding: 10px;
  font-size: 16px;
  border: 1px solid #ddd;
  border-radius: 5px;
  outline: none;
}

#search-input:focus {
  border-color: #0073e6;
}

#filter-button {
  padding: 10px 15px;
  margin-left: 10px;
  font-size: 16px;
  border: none;
  background-color: #0073e6;
  color: white;
  border-radius: 5px;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

#filter-button:hover {
  background-color: #005bb5;
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
    const searchInput = document.getElementById("search-input");
    const filterButton = document.getElementById("filter-button");
    const instructionBanner = document.querySelector(".instruction");

    const PAGE_SIZE = 6;
    let currentPage = 1;

    function getVisibleItems() {
      return Array.from(items).filter(item => item.style.display !== "none");
    }

    function paginateItems(visibleItems, pageNumber) {
      currentPage = pageNumber;
      const totalPages = Math.ceil(visibleItems.length / PAGE_SIZE);

      items.forEach(item => item.style.display = "none");
      visibleItems.slice((pageNumber - 1) * PAGE_SIZE, pageNumber * PAGE_SIZE).forEach(item => item.style.display = "block");

      currentPageSpan.textContent = pageNumber;
      totalPagesSpan.textContent = totalPages;

      prevButton.disabled = pageNumber === 1;
      nextButton.disabled = pageNumber >= totalPages;
    }

    function filterArchives() {
      const searchValue = searchInput.value.trim().toLowerCase();

      if (searchValue.length > 0 && searchValue.length < 3) {
        instructionBanner.textContent = "Search term must be at least 3 characters.";
        instructionBanner.style.color = "red";
        return;
      } else {
        instructionBanner.textContent = "Click on the verify star to see a live document.";
        instructionBanner.style.color = "#555";
      }

      let visibleItems = [];

      items.forEach(item => {
        const name = item.querySelector(".arch-name").textContent.toLowerCase();
        if (!searchValue || name.includes(searchValue)) {
          visibleItems.push(item);
        } else {
          item.style.display = "none";
        }
      });

      updateQueryParam(searchValue);
      paginateItems(visibleItems, 1);
    }

    function updateQueryParam(query) {
      const newUrl = query ? `${window.location.pathname}?search=${encodeURIComponent(query)}` : window.location.pathname;
      window.history.pushState({ path: newUrl }, "", newUrl);
    }

    function loadFromQueryParam() {
      const params = new URLSearchParams(window.location.search);
      const query = params.get("search");
      if (query) {
        searchInput.value = query;
      }
      filterArchives();
    }

    filterButton.addEventListener("click", filterArchives);
    
    nextButton.addEventListener("click", function () {
      const visibleItems = getVisibleItems();
      if (currentPage < Math.ceil(visibleItems.length / PAGE_SIZE)) {
        paginateItems(visibleItems, currentPage + 1);
      }
    });

    prevButton.addEventListener("click", function () {
      const visibleItems = getVisibleItems();
      if (currentPage > 1) {
        paginateItems(visibleItems, currentPage - 1);
      }
    });

    loadFromQueryParam();
  });
</script>
