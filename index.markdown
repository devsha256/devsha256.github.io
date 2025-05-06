---
layout: default
permalink: /
---

<h1>
  Hi there! 👋
  <span class="inline-notice">
    (I am <a href="https://www.linkedin.com/in/{{site.linkedin_username }}/"
      target="_blank">#OpenToWork</a> & 
    <a href="/notice-period.html">Serving Notice Period</a>)
  </span>
</h1>


<p>
   With over <strong><span id="yearsOfExperience"></span></strong> years of experience specializing in API integration, particularly with technologies like MuleSoft, I have developed strong skills in software development. Along the way, I've earned industry-recognized certifications, including those in MuleSoft Development and Anypoint Platform Architecture. While MuleSoft has been central to my career, my experience extends beyond it. In my current organization, I am also an "Elevated Wings1 Certified - Full-Stack JavaScript Developer (MERN)," a program that deepened my expertise in integration patterns using JavaScript.
</p>
<p>
    Automation has been key to my success, especially in testing, whether it’s unit or integration testing. I'm familiar with various architectural patterns, including ETL, real-time, and asynchronous Pub/Sub models. If you know of any projects or teams that could benefit from my skills, please feel free to connect!
</p>

---
<div class="index-links">
  <a href="/projects" class="index-link">💡 Check My Projects</a>
  <a href="/credentials" class="index-link">🎓 View My Credentials</a>
  <a href="/repositories" class="index-link">💻 Browse My GitHub Repos</a>
  <div class="resume-links">
    📄 
    <a href="/assets/resume.pdf" download class="resume-link">Download</a> /
    <a href="{{ site.resume_drive_link }}" target="_blank" class="resume-link">View 🌍 My Resume</a>
  </div>
</div>
---
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
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    gap: 0.4rem; /* tighter spacing */
    font-size: 1.1em;
    margin: 0.5rem 0; /* reduce top and bottom margin */
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
    color: #007acc;
    transform: translateX(4px);
    border-bottom: 1px solid #007acc;
  }

  .resume-links {
    font-weight: 500;
    display: flex;
    align-items: center;
    gap: 0.3rem;
    flex-wrap: wrap;
    margin-top: 0.3rem;
  }
</style>
<script>
function calculateExperience() {
  const startDate = new Date("2020-02-24");
  const now = new Date();
  const months = (now.getFullYear() - startDate.getFullYear()) * 12 + now.getMonth() - startDate.getMonth();
  const years = Math.floor(months / 12);
  const remMonths = months % 12;
  document.getElementById("yearsOfExperience").innerText = `${years}.${remMonths.toString().padStart(2, '0')}`;
}
document.addEventListener("DOMContentLoaded", calculateExperience);
</script>
