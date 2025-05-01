---
layout: default
title: Certifications
permalink: /certifications/
---

<div class="certifications">

  <div class="pagination">
    <button id="prev-button" disabled>Previous</button>
    <span id="current-page">1</span> / <span id="total-pages">{{ site.data.certifications | size }}</span>
    <button id="next-button">Next</button>
  </div>

  <ul class="certification-list">
    {% for cert in site.data.certifications %}
    <li class="certification-item" id="cert-{{ forloop.index }}">
    <a href="{{cert.cred_link}}">
      <img src="/assets/img/certifications/{{ cert.image }}" alt="{{ cert.name }}" class="cert-logo" />
    </a>
      <h2 class="cert-name">{{ cert.name }}</h2>
      <p><strong>Authority:</strong> {{ cert.authority }}</p>
      <p><strong>Date:</strong> {{ cert.date }}</p>
      <p><strong>Credential ID:</strong> {{ cert.credential_id }}</p>
    </li>
    {% endfor %}
  </ul>
</div>

<style>
  .certifications {
    font-family: Arial, sans-serif;
    margin: 20px;
  }

  .certification-list {
    list-style: none;
    padding: 0;
  }

  .certification-item {
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

  .cert-name {
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
</style>

<script>
  document.addEventListener("DOMContentLoaded", function () {
    const items = document.querySelectorAll(".certification-item");
    const prevButton = document.getElementById("prev-button");
    const nextButton = document.getElementById("next-button");
    const currentPageSpan = document.getElementById("current-page");
    const totalPagesSpan = document.getElementById("total-pages");

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
  });
</script>
