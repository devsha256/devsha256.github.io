---
layout: default
title: Repos
permalink: /repos
---

<div class="github-repos">
  <h2>Public Github Repositories</h2>
  <div class="pagination">
    <button id="prev-button" disabled>Previous</button>
    <span id="current-page">1</span> / <span id="total-pages">1</span>
    <button id="next-button">Next</button>
  </div>

  <ul id="repoList" class="repo-list">
    <li>Loading repositories...</li>
  </ul>
</div>

<style>
  h2{
    text-align: center
  }
  .github-repos {
    font-family: Arial, sans-serif;
    margin: 20px;
  }

  .repo-list {
    list-style: none;
    padding: 0;
  }

  .repo-card {
    display: none;
    border: 1px solid #ccc;
    border-radius: 12px;
    padding: 15px;
    margin-bottom: 20px;
    box-shadow: 0 2px 6px rgba(0, 0, 0, 0.1);
  }

  .repo-card h3 {
    margin: 0 0 10px;
  }

  .repo-card p {
    margin: 5px 0;
  }

  .pagination {
    text-align: center;
    margin-bottom: 20px;
  }

  .pagination button {
    padding: 8px 15px;
    margin: 0 5px;
    cursor: pointer;
  }

  .repo-meta {
    font-size: 0.9em;
    color: #555;
  }
</style>

<script>
  async function fetchGitHubRepos(username, listId) {
    try {
      let response = await fetch(`https://api.github.com/users/${username}/repos`);
      let repos = await response.json();
      if (Array.isArray(repos)) {
        const repoList = document.getElementById(listId);
        repoList.innerHTML = '';

        repos.forEach((repo, index) => {
          const li = document.createElement('li');
          li.classList.add('repo-card');
          li.id = `repo-${index + 1}`;

          li.innerHTML = `
            <h3><a href="${repo.html_url}" target="_blank">${repo.name}</a></h3>
            <p>${repo.description || 'No description provided.'}</p>
            <div class="repo-meta">
              <p><strong>Owner:</strong> ${repo.owner.login}</p>
              <p><strong>Last Updated:</strong> ${new Date(repo.updated_at).toLocaleDateString()}</p>
              <p><strong>Forks:</strong> ${repo.forks}</p>
            </div>
          `;

          repoList.appendChild(li);
        });

        setupPagination(repos.length);
      }
    } catch (error) {
      console.error("Error fetching GitHub repos:", error);
      document.getElementById(listId).innerHTML = "<li>Failed to load repositories</li>";
    }
  }

  function setupPagination(totalRepos) {
    const repoItems = document.querySelectorAll('.repo-card');
    const prevButton = document.getElementById('prev-button');
    const nextButton = document.getElementById('next-button');
    const currentPageSpan = document.getElementById('current-page');
    const totalPagesSpan = document.getElementById('total-pages');

    let currentPage = 1;
    const totalPages = totalRepos;

    function showPage(index) {
      repoItems.forEach((item, i) => {
        item.style.display = i === index ? 'block' : 'none';
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

    nextButton.onclick = nextPage;
    prevButton.onclick = prevPage;

    if (totalRepos > 0) showPage(0);
  }

  document.addEventListener("DOMContentLoaded", () => {
    fetchGitHubRepos("devsha256", "repoList");
  });
</script>
