---
layout: default
permalink: /
---

<h1>
  Hi there! 👋
  <!-- <span class="inline-notice">
    (I am <a href="https://www.linkedin.com/in/{{site.linkedin_username }}/"
      target="_blank">#OpenToWork</a> & 
    <a href="/notice-period.html">Serving Notice Period</a>)
  </span> -->
</h1>

<p id="summary"></p>

<div class="index-links">
  <a href="/projects" class="index-link">💡 Check My Projects</a>
  <a href="/credentials" class="index-link">🎓 View My Credentials</a>
  <a href="/repositories" class="index-link">💻 Browse My GitHub Repos</a>
  <!-- <div class="resume-links">
    📄 
    <a href="/assets/resume.pdf" download class="resume-link">Download</a> /
    <a href="{{ site.resume_drive_link }}" target="_blank" class="resume-link">View 🌍 My Resume</a>
  </div> -->
</div>

<script>
function calculateExperience() {
  const startDate = new Date("2020-02-24");
  const now = new Date();
  const months = (now.getFullYear() - startDate.getFullYear()) * 12 + now.getMonth() - startDate.getMonth();
  const years = Math.floor(months / 12);
  const remMonths = months % 12;
  return `${years}.${remMonths.toString().padStart(2, '0')}`;
}

document.addEventListener("DOMContentLoaded", function () {
  const experience = calculateExperience();
  const summaries = {{ site.data.summaries | jsonify }};
  const randomIndex = Math.floor(Math.random() * summaries.length);
  let summary = summaries[randomIndex];
  summary = summary.replaceAll('{years}', experience);

  // Parse multiline YAML block and inject into a paragraph tag
  const lines = summary.split('\n');
  let formatted = "";
  lines.forEach(line => {
    if (line.trim()) {
      formatted += `<p>${line.trim()}</p>`;
    }
  });

  document.getElementById("summary").innerHTML = formatted;
});
</script>

<style>
  .inline-notice {
    font-size: 0.6em;
    font-weight: bold;
    color: #b30000;
    margin-left: 10px;
    animation: pulse-inline 1.5s infinite;
  }

  .inline-notice a {
    color: #d32f2f;
    text-decoration: none;
    border-bottom: 1px dashed #d32f2f;
  }

  .inline-notice a:hover {
    color: #800000;
    border-bottom-style: solid;
  }

  @keyframes pulse-inline {
    0% { opacity: 0.6; }
    50% { opacity: 1; }
    100% { opacity: 0.6; }
  }

  .index-links {
    position: sticky;
    bottom: 0; /* Stick directly to the bottom of the viewport */
    background: #ffffff;
    padding: 0.8rem 1rem;
    margin-top: 2rem; /* Optional: separate from summary above */
    z-index: 10;
    box-shadow: 0 -2px 6px rgba(0, 0, 0, 0.05);
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    gap: 0.4rem;
    font-size: 1.1em;
    line-height: 1.3em;
  }

  .index-link,
  .resume-link {
    text-decoration: none;
    color: #2c3e50;
    font-weight: 500;
    transition: transform 0.2s ease, color 0.3s ease;
    border-bottom: 1px solid transparent;
  }

  .index-link:hover,
  .resume-link:hover {
    text-decoration: none;
    color: #007acc;
    transform: translateX(4px);
    border-bottom: 1px solid #007acc;
  }

  .resume-links {
    text-decoration: none;
    font-weight: 500;
    display: flex;
    align-items: center;
    gap: 0.3rem;
    flex-wrap: wrap;
    margin-top: 0.3rem;
  }
</style>
