---
layout: default
permalink: /
---

<div class="home-hero">
  <div class="hero-eyebrow">
    <span class="hero-badge">MuleSoft · Integration · Architecture</span>
  </div>
  <h1 class="hero-heading">Hi there! <span class="wave" aria-label="waving hand">👋</span></h1>
  <div class="hero-summary" id="summary"></div>
  <div class="hero-actions">
    <a href="/projects" class="md-btn md-btn-filled" id="btn-projects">
      <span>💡</span> Projects
    </a>
    <a href="/credentials" class="md-btn md-btn-outlined" id="btn-credentials">
      <span>🎓</span> Credentials
    </a>
    <a href="/repositories" class="md-btn md-btn-outlined" id="btn-repos">
      <span>💻</span> GitHub Repos
    </a>
  </div>
</div>

<script>
function calculateExperience() {
  var startDate = new Date("2020-02-24");
  var now = new Date();
  var months = (now.getFullYear() - startDate.getFullYear()) * 12 + now.getMonth() - startDate.getMonth();
  var years = Math.floor(months / 12);
  var remMonths = months % 12;
  
  var yearText = years === 1 ? "Year" : "Years";
  var monthText = remMonths === 1 ? "Month" : "Months";
  
  if (remMonths === 0) {
    return years + " " + yearText;
  }
  return years + " " + yearText + " " + remMonths + " " + monthText;
}

document.addEventListener("DOMContentLoaded", function () {
  var experience = calculateExperience();
  var summaries = {{ site.data.summaries | jsonify }};
  var randomIndex = Math.floor(Math.random() * summaries.length);
  var summary = summaries[randomIndex];
  summary = summary.replaceAll('{years}', experience);

  var lines = summary.split('\n');
  var formatted = "";
  lines.forEach(function(line) {
    if (line.trim()) {
      formatted += '<p>' + line.trim() + '</p>';
    }
  });

  document.getElementById("summary").innerHTML = formatted;
});
</script>

<style>
.home-hero {
  padding: 3rem 0 4rem;
  display: flex;
  flex-direction: column;
  gap: 1.25rem;
}

.hero-eyebrow {
  display: flex;
  gap: 0.5rem;
  flex-wrap: wrap;
}

.hero-badge {
  display: inline-flex;
  align-items: center;
  gap: 0.4rem;
  padding: 0.3rem 0.85rem;
  border-radius: var(--md-shape-full);
  font-size: 0.775rem;
  font-weight: 600;
  letter-spacing: 0.04em;
  text-transform: uppercase;
  background: var(--md-primary-container);
  color: var(--md-on-primary-container);
  border: 1px solid var(--md-outline-variant);
}

.hero-heading {
  font-size: clamp(2.2rem, 6vw, 3.5rem);
  font-weight: 800;
  background: linear-gradient(135deg, var(--md-on-surface) 0%, var(--md-primary) 60%, var(--md-secondary) 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
  letter-spacing: -0.03em;
  line-height: 1.15;
}

.wave {
  display: inline-block;
  animation: wave 2.2s infinite;
  transform-origin: 70% 70%;
}

@keyframes wave {
  0%   { transform: rotate(0deg); }
  10%  { transform: rotate(14deg); }
  20%  { transform: rotate(-8deg); }
  30%  { transform: rotate(14deg); }
  40%  { transform: rotate(-4deg); }
  50%  { transform: rotate(10deg); }
  60%  { transform: rotate(0deg); }
  100% { transform: rotate(0deg); }
}

.hero-summary {
  max-width: 680px;
}
.hero-summary p {
  color: var(--md-on-surface-variant);
  font-size: 1.05rem;
  line-height: 1.75;
  margin-bottom: 0.75rem;
}
.hero-summary p:last-child { margin-bottom: 0; }

.hero-actions {
  display: flex;
  gap: 0.75rem;
  flex-wrap: wrap;
  padding-top: 0.5rem;
}

@media (max-width: 480px) {
  .hero-actions { flex-direction: column; }
  .hero-actions .md-btn { justify-content: center; }
  .home-hero { padding: 2rem 0 3rem; }
}
</style>
