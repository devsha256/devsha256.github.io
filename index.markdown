---
layout: page
---
<h2>My Public GitHub Repositories</h2>
<ul id="repoList">
  <li>Loading repositories...</li>
</ul>

<script>
    async function fetchGitHubRepos(username, id) {
        try {
            let response = await fetch(`https://api.github.com/users/${username}/repos`);
            let repos = await response.json();
            if (Array.isArray(repos)) {
                let repoListHTML = repos.map(repo => `<li><a href="${repo.html_url}" target="_blank">${repo.name}</a></li>`).join('');
                document.getElementById(id).innerHTML = repoListHTML;
            }
        } catch (error) {
            console.error("Error fetching GitHub repos:", error);
            document.getElementById(id).innerHTML = "<li>Failed to load repositories</li>";
        }
    }

    document.addEventListener("DOMContentLoaded", () => {
        fetchGitHubRepos("devsha256", "repoList");
    });
</script>