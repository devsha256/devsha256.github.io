---
layout: default
title: Repositories
permalink: /repositories
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
  }

  .repo-list {
    list-style: none;
    padding: 0;
  }

  .repo-card {
    display: none;
    border-bottom: 2px solid #ddd;
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
      repos = repos.filter((repo, idx) => !repo.fork)
      if (Array.isArray(repos)) {
        const repoList = document.getElementById(listId);
        repoList.innerHTML = '';

        repos.forEach((repo, index) => {
          const li = document.createElement('li');
          li.classList.add('repo-card');
          li.id = `repo-${index + 1}`;

          li.innerHTML = `
            <h3>
    <svg xmlns="http://www.w3.org/2000/svg" x="0px" y="0px" width="18" height="18" viewBox="0 0 16 16">
      <path d="M 7.5 1 C 3.910156 1 1 3.90625 1 7.488281 C 1 10.355469 2.863281 12.789063 5.445313 13.648438 C 5.769531 13.707031 6 13.375 6 13.125 C 6 12.972656 6.003906 12.789063 6 12.25 C 4.191406 12.640625 3.625 11.375 3.625 11.375 C 3.328125 10.625 2.96875 10.410156 2.96875 10.410156 C 2.378906 10.007813 3.011719 10.019531 3.011719 10.019531 C 3.664063 10.0625 4 10.625 4 10.625 C 4.5 11.5 5.628906 11.414063 6 11.25 C 6 10.851563 6.042969 10.5625 6.152344 10.378906 C 4.109375 10.019531 2.996094 8.839844 3 7.207031 C 3.003906 6.242188 3.335938 5.492188 3.875 4.9375 C 3.640625 4.640625 3.480469 3.625 3.960938 3 C 5.167969 3 5.886719 3.871094 5.886719 3.871094 C 5.886719 3.871094 6.453125 3.625 7.496094 3.625 C 8.542969 3.625 9.105469 3.859375 9.105469 3.859375 C 9.105469 3.859375 9.828125 3 11.035156 3 C 11.515625 3.625 11.355469 4.640625 11.167969 4.917969 C 11.683594 5.460938 12 6.210938 12 7.207031 C 12 8.839844 10.890625 10.019531 8.851563 10.375 C 8.980469 10.570313 9 10.84375 9 11.25 C 9 12.117188 9 12.910156 9 13.125 C 9 13.375 9.226563 13.710938 9.558594 13.648438 C 12.140625 12.785156 14 10.355469 14 7.488281 C 14 3.90625 11.089844 1 7.5 1 Z"></path>
    </svg>
    <a href="${repo.html_url}" target="_blank">
      ${repo.name}
    </a>
</h3>
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
    fetchGitHubRepos("{{site.github_username}}", "repoList");
  });
</script>
