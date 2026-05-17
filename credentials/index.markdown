---
layout: default
title: Credentials
permalink: /credentials/
---

<div class="credentials-page">
  <div class="credentials-header">
    <h1 class="credentials-title">Credentials</h1>
    <p class="credentials-subtitle">Explore my certifications, peer feedback, and learning history.</p>
  </div>

  <div class="credentials-grid">
    <a href="{{ '/credentials/certifications/' | relative_url }}" class="cred-hub-card" id="card-certifications">
      <div class="cred-hub-icon">🏅</div>
      <h2 class="cred-hub-title">Certifications</h2>
      <p class="cred-hub-desc">Industry-recognized credentials in MuleSoft, AWS, and more.</p>
      <span class="cred-hub-cta">View Certifications →</span>
    </a>

    <a href="{{ '/credentials/feedbacks/' | relative_url }}" class="cred-hub-card" id="card-feedbacks">
      <div class="cred-hub-icon">💬</div>
      <h2 class="cred-hub-title">Feedbacks</h2>
      <p class="cred-hub-desc">Recognition and appreciation from colleagues and supervisors.</p>
      <span class="cred-hub-cta">See Feedbacks →</span>
    </a>

    <a href="{{ '/credentials/archives/' | relative_url }}" class="cred-hub-card" id="card-archives">
      <div class="cred-hub-icon">📚</div>
      <h2 class="cred-hub-title">Learning History</h2>
      <p class="cred-hub-desc">A searchable archive of courses and achievements over time.</p>
      <span class="cred-hub-cta">Browse Archives →</span>
    </a>
  </div>
</div>

<style>
.credentials-page { padding: 1.5rem 0 4rem; }
.credentials-header { margin-bottom: 2.5rem; }
.credentials-title  { margin-bottom: 0.4rem; }
.credentials-subtitle { font-size: 0.95rem; color: var(--md-on-surface-variant); }

.credentials-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
  gap: 1.25rem;
}

.cred-hub-card {
  display: flex;
  flex-direction: column;
  gap: 0.6rem;
  background: var(--md-surface-container);
  border: 1px solid var(--md-outline-variant);
  border-radius: var(--md-shape-xl);
  padding: 2rem 1.75rem;
  text-decoration: none;
  color: inherit;
  transition: transform var(--md-motion-standard), box-shadow var(--md-motion-standard),
              border-color var(--md-motion-standard), background var(--md-motion-standard);
}

.cred-hub-card:hover {
  transform: translateY(-4px);
  box-shadow: 0 8px 28px rgba(124,111,205,0.2);
  border-color: var(--md-primary);
  background: var(--md-surface-container-high);
  color: inherit;
}

.cred-hub-icon {
  font-size: 2.2rem;
  line-height: 1;
  margin-bottom: 0.25rem;
}

.cred-hub-title {
  font-size: 1.15rem;
  font-weight: 700;
  color: var(--md-on-surface);
  margin: 0;
}

.cred-hub-desc {
  font-size: 0.88rem;
  color: var(--md-on-surface-variant);
  line-height: 1.55;
  flex: 1;
  margin: 0;
}

.cred-hub-cta {
  font-size: 0.82rem;
  font-weight: 600;
  color: var(--md-primary);
  margin-top: 0.25rem;
}

@media (max-width: 600px) {
  .credentials-grid { grid-template-columns: 1fr; }
}
</style>