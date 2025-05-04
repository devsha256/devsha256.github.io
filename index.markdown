---
layout: default
permalink: /
---

<h1>Hi there! 👋</h1>

<p>
  I am Saddam. With over <strong><span id="yearsOfExperience"></span></strong> years of experience specializing in API integration, particularly with technologies like MuleSoft, I have developed strong skills in software development. Along the way, I've earned industry-recognized certifications, including those in MuleSoft Development and Anypoint Platform Architecture. While MuleSoft has been central to my career, my experience extends beyond it. In my current organization, I am also an "Elevated Wings1 Certified - Full-Stack JavaScript Developer (MERN)," a program that deepened my expertise in integration patterns using JavaScript.
</p>
<p>
    Automation has been key to my success, especially in testing, whether it’s unit or integration testing. I'm familiar with various architectural patterns, including ETL, real-time, and asynchronous Pub/Sub models. If you know of any projects or teams that could benefit from my skills, please feel free to connect!
</p>

---

<div style="font-size: 1.5em; line-height: 1.5em;">
  <p><a href="/projects">#[ Check My Projects ]</a></p>
  <p><a href="/credentials">#[ View My Credentials ]</a></p>
  <p><a href="/repositories">#[ Browse My GitHub Repos ]</a></p>
  <p>
    <a href="/assets/resume.pdf" download>#[ ⬇️ Download </a>/
    <a  target="_blank" href="https://drive.google.com/file/d/1HqgHimaWWq0d6bTVEAHOlKftVPfpmwsI/view?usp=sharing">
     View 🌎 My Resume ]
    </a> 
  </p>
</div>

---

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
