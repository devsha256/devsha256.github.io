---
layout: page
title: About
permalink: /about/
nav_order: 4
---

<h1> Hi there! 👋 </h1>

<section>
    With over <span id="yearsOfExperience"></span> years of experience specializing in API integration, particularly with technologies like MuleSoft, I have developed strong skills in software development. Along the way, I've earned industry-recognized certifications, including those in MuleSoft Development and Anypoint Platform Architecture. While MuleSoft has been central to my career, my experience extends beyond it. In my current organization, I am also an "Elevated Wings1 Certified - Full-Stack JavaScript Developer (MERN)," a program that deepened my expertise in integration patterns using JavaScript.

    Automation has been key to my success, especially in testing, whether it’s unit or integration testing. I'm familiar with various architectural patterns, including ETL, real-time, and asynchronous Pub/Sub models. If you know of any projects or teams that could benefit from my skills, please feel free to connect!
</section>
<br/>

- 🔭 I’m currently working as MuleSoft Integraiton developer to help customer solve their business problems using MuleSoft Technologies.
- 💬 Ask me about: MuleSoft, Dataweave, JavaScript and Snowflake.
- 📫 How to reach me: Find me on LinkedIn.com [LinkedIn](https://www.linkedin.com/in/hsaddam/)
- 😄 Pronouns: He/Him


<script>
function calculateExperience() {
    let startDate = new Date("2020-02-24");
    let currentDate = new Date();
    
    let totalMonths = (currentDate.getFullYear() - startDate.getFullYear()) * 12 + (currentDate.getMonth() - startDate.getMonth());
    let years = Math.floor(totalMonths / 12);
    let months = totalMonths % 12;
    
    let experience = `${years}.${months.toString().padStart(2, '0')}`;
    document.getElementById("yearsOfExperience").innerText = experience;
}

calculateExperience();
</script>
