---
layout: default
title: Repositories
permalink: /repositories
---

<div class="repos-page">
  <div class="repos-header">
    <h1 class="repos-title">GitHub Repositories</h1>
    <p class="repos-subtitle">My public, non-forked repositories.</p>
  </div>

  <div class="md-pagination" id="pagination-top">
    <button class="md-btn md-btn-outlined" id="prev-button" disabled>← Prev</button>
    <span class="page-info">
      <span id="current-page">1</span> / <span id="total-pages">—</span>
    </span>
    <button class="md-btn md-btn-outlined" id="next-button">Next →</button>
  </div>

  <ul id="repoList" class="repo-list">
    <li class="repo-loading">
      <div class="loading-spinner"></div>
      <span>Loading repositories…</span>
    </li>
  </ul>
</div>

<style>
.repos-page { padding: 1.5rem 0 4rem; }
.repos-header { margin-bottom: 2rem; }
.repos-title  { margin-bottom: 0.4rem; }
.repos-subtitle { font-size: 0.95rem; color: var(--md-on-surface-variant); }

.repo-list { list-style: none; padding: 0; }

/* Loading state */
.repo-loading {
  display: flex;
  align-items: center;
  gap: 1rem;
  padding: 2rem;
  color: var(--md-on-surface-variant);
  font-size: 0.9rem;
}
.loading-spinner {
  width: 20px; height: 20px;
  border: 2px solid var(--md-outline);
  border-top-color: var(--md-primary);
  border-radius: 50%;
  animation: spin 0.8s linear infinite;
}
@keyframes spin { to { transform: rotate(360deg); } }

/* Repo card */
.repo-card {
  display: none;
  background: var(--md-surface-container);
  border: 1px solid var(--md-outline-variant);
  border-radius: var(--md-shape-xl);
  padding: 1.5rem 1.75rem;
  margin-bottom: 1.25rem;
  animation: card-enter 0.35s ease-out;
  transition: border-color var(--md-motion-standard), transform var(--md-motion-standard),
              box-shadow var(--md-motion-standard);
}
.repo-card:hover {
  border-color: var(--md-primary);
  transform: translateY(-2px);
  box-shadow: 0 6px 20px rgba(124,111,205,0.15);
}

@keyframes card-enter {
  from { opacity: 0; transform: translateY(10px); }
  to   { opacity: 1; transform: translateY(0); }
}

.repo-card-name {
  display: flex;
  align-items: center;
  gap: 0.6rem;
  margin-bottom: 0.5rem;
}
.repo-card-name .github-icon { color: var(--md-on-surface-variant); flex-shrink: 0; }
.repo-card-name a {
  font-size: 1.15rem;
  font-weight: 700;
  color: var(--md-primary);
}
.repo-card-name a:hover { color: var(--md-secondary); }

.repo-description {
  color: var(--md-on-surface-variant);
  font-size: 0.9rem;
  line-height: 1.6;
  margin-bottom: 1rem;
}

.repo-meta {
  display: flex;
  flex-wrap: wrap;
  gap: 0.5rem 1.25rem;
}
.repo-meta-item {
  font-size: 0.8rem;
  color: var(--md-on-surface-variant);
  display: flex;
  align-items: center;
  gap: 0.3rem;
}
.repo-meta-item strong { color: var(--md-on-surface); font-weight: 500; }

@media (max-width: 600px) {
  .repo-card { padding: 1.25rem; }
}
</style>

<script>
async function fetchGitHubRepos(username) {
  var list = document.getElementById('repoList');
  try {
    var res   = await fetch('https://api.github.com/users/' + username + '/repos?per_page=100');
    var repos = await res.json();
    repos = repos.filter(function(r) { return !r.fork; });
    repos.sort(function(a, b) { return new Date(b.updated_at) - new Date(a.updated_at); });

    list.innerHTML = '';

    repos.forEach(function(repo, idx) {
      var li = document.createElement('li');
      li.className = 'repo-card';
      li.id = 'repo-' + (idx + 1);
      li.innerHTML = [
        '<div class="repo-card-name">',
          '<svg class="github-icon" xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 16 16" fill="currentColor">',
            '<path d="M7.5 1C3.91 1 1 3.906 1 7.488c0 2.867 1.863 5.301 4.445 6.16.325.06.555-.272.555-.522 0-.153.004-.336 0-.875C4.191 12.64 3.625 11.375 3.625 11.375c-.297-.75-.656-.965-.656-.965-.59-.403.043-.391.043-.391.652.043.988.605.988.605.5.875 1.629.789 2 .625 0-.399.042-.688.152-.872C4.11 10.02 3 8.84 3 7.207c0-.965.332-1.715.872-2.27-.14-.297-.48-1.312 0-1.937 1.207 0 1.926.871 1.926.871S6.453 3.625 7.5 3.625s2.105.246 2.105.246S10.328 3 11.535 3c.48.625.32 1.64.133 1.917.516.543.832 1.293.832 2.29 0 1.632-1.11 2.812-3.148 3.168.129.195.148.469.148.875 0 .867 0 1.66 0 1.875 0 .25.227.586.559.523C12.14 12.786 14 10.356 14 7.488 14 3.906 11.09 1 7.5 1z"/>',
          '</svg>',
          '<a href="' + repo.html_url + '" target="_blank" rel="noopener">' + escapeHtml(repo.name) + '</a>',
        '</div>',
        '<p class="repo-description">' + escapeHtml(repo.description || 'No description provided.') + '</p>',
        '<div class="repo-meta">',
          '<span class="repo-meta-item"><strong>Owner:</strong> ' + escapeHtml(repo.owner.login) + '</span>',
          '<span class="repo-meta-item"><strong>Updated:</strong> ' + new Date(repo.updated_at).toLocaleDateString() + '</span>',
          '<span class="repo-meta-item"><strong>Forks:</strong> ' + repo.forks + '</span>',
          repo.language ? '<span class="repo-meta-item"><strong>Lang:</strong> ' + escapeHtml(repo.language) + '</span>' : '',
          '<span class="repo-meta-item">⭐ ' + (repo.stargazers_count || 0) + '</span>',
        '</div>'
      ].join('');
      list.appendChild(li);
    });

    setupPagination(repos.length);
  } catch (err) {
    list.innerHTML = '<li style="color:var(--md-error);padding:1rem;">Failed to load repositories.</li>';
  }
}

function escapeHtml(str) {
  if (!str) return '';
  return String(str).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;');
}

function setupPagination(total) {
  var items    = document.querySelectorAll('.repo-card');
  var prevBtn  = document.getElementById('prev-button');
  var nextBtn  = document.getElementById('next-button');
  var curSpan  = document.getElementById('current-page');
  var totSpan  = document.getElementById('total-pages');
  var current  = 1;
  totSpan.textContent = total;

  function show(idx) {
    items.forEach(function(item, i) { item.style.display = (i === idx) ? 'block' : 'none'; });
    curSpan.textContent = current;
    prevBtn.disabled = current === 1;
    nextBtn.disabled = current === total;
  }

  prevBtn.onclick = function() { if (current > 1) { current--; show(current - 1); } };
  nextBtn.onclick = function() { if (current < total) { current++; show(current - 1); } };

  if (total > 0) show(0);
}

document.addEventListener('DOMContentLoaded', function() {
  fetchGitHubRepos('{{site.github_username}}');
});
</script>
