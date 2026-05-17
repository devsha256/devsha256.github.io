---
layout: default
title: Credentials - Feedbacks
permalink: /credentials/feedbacks/
nav_include: no
---

<div id="feedbacks-root"></div>

<script crossorigin src="https://unpkg.com/react@18/umd/react.production.min.js"></script>
<script crossorigin src="https://unpkg.com/react-dom@18/umd/react-dom.production.min.js"></script>

<script>
const PAGE_NUMBER = 1;
const PAGE_SIZE = 1;
const { useState, useEffect } = React;

const feedbacks = {{ site.data.feedbacks | jsonify }};
const sortedFeedbacks = feedbacks.slice().sort((a, b) => new Date(b.date) - new Date(a.date));

function getParams() {
  const sp = new URLSearchParams(window.location.search);
  return {
    uuid: sp.get("id"),
    page: parseInt(sp.get("page")) || PAGE_NUMBER,
    size: parseInt(sp.get("size")) || PAGE_SIZE
  };
}

function StarVerify({ link }) {
  if (!link) return React.createElement('span', { style: { color: 'var(--md-on-surface-variant)', fontSize: '0.82rem' } }, 'Not Available');
  return React.createElement('a', {
    href: link, target: '_blank', rel: 'noopener',
    className: 'stars-container', title: 'View Original'
  },
    React.createElement('span', { className: 'stars' },
      Array.from({ length: 5 }, (_, i) =>
        React.createElement('svg', {
          key: i, className: 'star',
          viewBox: '0 0 24 24', width: 24, height: 24,
          xmlns: 'http://www.w3.org/2000/svg'
        },
          React.createElement('path', { d: 'M12 .587l3.668 7.57L24 9.748l-6 5.848 1.415 8.258L12 19.771l-7.415 4.083L6 15.596 0 9.748l8.332-1.591z' })
        )
      )
    )
  );
}

function FeedbackCard({ fb }) {
  return React.createElement('div', { className: 'cred-card feedback-card' },
    React.createElement('div', { className: 'cred-card-top' },
      React.createElement('a', { href: fb.cred_link, target: '_blank', rel: 'noopener', className: 'cred-logo-link' },
        React.createElement('img', {
          src: `/assets/img/logos/${fb.image}`,
          alt: fb.name, className: 'cred-logo'
        })
      ),
      React.createElement('div', { className: 'cred-info' },
        React.createElement('span', { className: 'cred-authority-badge' }, fb.authority),
        React.createElement('h2', { className: 'cred-name' }, fb.name),
        React.createElement('div', { className: 'cred-meta' },
          React.createElement('span', null, '📅 ', React.createElement('strong', null, 'Date: '), fb.date)
        )
      )
    ),
    fb.comment && React.createElement('blockquote', { className: 'feedback-quote' }, fb.comment),
    React.createElement('div', { className: 'cred-verify' },
      React.createElement('span', { className: 'verify-label' }, 'Verify live:'),
      React.createElement(StarVerify, { link: fb.drive_link })
    )
  );
}

function FeedbackApp() {
  const { uuid, page, size } = getParams();
  const [pageSize] = useState(size);
  const [currentPage, setCurrentPage] = useState(1);

  useEffect(() => {
    let index = 0;
    if (uuid) {
      const idx = sortedFeedbacks.findIndex(f => f.id === uuid);
      if (idx !== -1) index = idx;
    } else if (page) {
      const pi = (page - 1) * pageSize;
      if (pi >= 0 && pi < sortedFeedbacks.length) index = pi;
    }
    const newPage = Math.floor(index / pageSize) + 1;
    setCurrentPage(newPage);
    if (pageSize === 1) updateURL(sortedFeedbacks[index]?.id, newPage, pageSize);
    else updateURL(null, newPage, pageSize);
  }, []);

  function updateURL(id, pg, sz) {
    const sp = new URLSearchParams();
    if (id && sz === 1) sp.set("id", id); else sp.set("size", sz);
    sp.set("page", pg);
    history.replaceState(null, '', `/credentials/feedbacks/?${sp.toString()}`);
  }

  const totalPages = Math.ceil(sortedFeedbacks.length / pageSize);
  const visible    = sortedFeedbacks.slice((currentPage - 1) * pageSize, currentPage * pageSize);

  const handleNext = () => {
    const np = currentPage + 1; setCurrentPage(np);
    const i = (np - 1) * pageSize;
    if (pageSize === 1) updateURL(sortedFeedbacks[i]?.id, np, pageSize);
    else updateURL(null, np, pageSize);
  };
  const handlePrev = () => {
    const np = currentPage - 1; setCurrentPage(np);
    const i = (np - 1) * pageSize;
    if (pageSize === 1) updateURL(sortedFeedbacks[i]?.id, np, pageSize);
    else updateURL(null, np, pageSize);
  };

  return React.createElement('div', { className: 'certs-page' },
    React.createElement('div', { className: 'creds-page-header' },
      React.createElement('a', { href: '/credentials/', className: 'back-link' }, '← Credentials'),
      React.createElement('h1', null, 'Feedbacks & Recognition')
    ),
    React.createElement('div', { className: 'md-pagination' },
      React.createElement('button', { className: 'md-btn md-btn-outlined', onClick: handlePrev, disabled: currentPage === 1 }, '← Prev'),
      React.createElement('span', { className: 'page-info' }, `${currentPage} / ${totalPages}`),
      React.createElement('button', { className: 'md-btn md-btn-outlined', onClick: handleNext, disabled: currentPage === totalPages }, 'Next →')
    ),
    React.createElement('div', { className: 'cred-list' },
      visible.map(fb => React.createElement(FeedbackCard, { key: fb.id, fb }))
    ),
    React.createElement('div', { className: 'md-instruction' }, '✨ Click the stars to see the original feedback document (if available).')
  );
}

document.addEventListener('DOMContentLoaded', () => {
  const { uuid, page } = getParams();
  if (!uuid && !page && sortedFeedbacks.length > 0) {
    history.replaceState(null, '', `/credentials/feedbacks/?id=${sortedFeedbacks[0].id}&page=1`);
  }
  ReactDOM.render(React.createElement(FeedbackApp), document.getElementById('feedbacks-root'));
});
</script>

<style>
.certs-page { padding: 1.5rem 0 5rem; }

.creds-page-header { margin-bottom: 1.5rem; }
.back-link {
  font-size: 0.82rem;
  color: var(--md-on-surface-variant);
  text-decoration: none;
  display: inline-block;
  margin-bottom: 0.6rem;
  transition: color 150ms;
}
.back-link:hover { color: var(--md-primary); }
.creds-page-header h1 { margin: 0; }

.cred-list { display: flex; flex-direction: column; gap: 1.25rem; }

.cred-card {
  background: var(--md-surface-container);
  border: 1px solid var(--md-outline-variant);
  border-radius: var(--md-shape-xl);
  padding: 1.75rem;
  animation: card-enter 0.35s ease-out;
  transition: box-shadow 300ms, border-color 300ms;
}
.cred-card:hover {
  box-shadow: 0 6px 20px rgba(124,111,205,0.15);
  border-color: var(--md-outline);
}

@keyframes card-enter {
  from { opacity: 0; transform: translateY(10px); }
  to   { opacity: 1; transform: translateY(0); }
}

.cred-card-top {
  display: flex; gap: 1.5rem; align-items: flex-start; margin-bottom: 1.25rem;
}
.cred-logo-link { flex-shrink: 0; }
.cred-logo {
  width: 80px; height: auto; border-radius: var(--md-shape-sm);
  background: var(--md-surface-container-highest); padding: 6px; object-fit: contain;
}
.cred-info { flex: 1; }
.cred-authority-badge {
  display: inline-flex; padding: 0.2rem 0.65rem;
  background: var(--md-secondary-container); color: var(--md-on-secondary-container);
  border-radius: 9999px; font-size: 0.72rem; font-weight: 600; margin-bottom: 0.5rem;
}
.cred-name { font-size: 1.2rem; font-weight: 700; color: var(--md-on-surface); margin: 0 0 0.6rem; }
.cred-meta { display: flex; flex-direction: column; gap: 0.2rem; font-size: 0.84rem; color: var(--md-on-surface-variant); }
.cred-meta strong { color: var(--md-on-surface); }

/* Feedback blockquote */
.feedback-quote {
  margin: 0 0 1.25rem;
  padding: 1rem 1.25rem;
  background: var(--md-surface-container-high);
  border-left: 3px solid var(--md-primary);
  border-radius: 0 var(--md-shape-md) var(--md-shape-md) 0;
  color: var(--md-on-surface-variant);
  font-size: 0.92rem;
  line-height: 1.65;
  font-style: italic;
}

.cred-verify {
  display: flex; align-items: center; gap: 0.75rem;
  padding-top: 1rem; border-top: 1px solid var(--md-outline-variant);
}
.verify-label { font-size: 0.82rem; color: var(--md-on-surface-variant); }

.stars-container { display: inline-flex; align-items: center; text-decoration: none; gap: 2px; }
.star { fill: var(--md-outline); transition: fill 0.25s ease; }
.stars-container:hover .star { fill: #FBBF24; }

.md-pagination {
  display: flex; align-items: center; justify-content: center;
  gap: 0.75rem; margin: 1.25rem 0 1.75rem;
}
.page-info {
  font-size: 0.875rem; color: var(--md-on-surface-variant);
  min-width: 70px; text-align: center;
}

.md-btn {
  display: inline-flex; align-items: center; gap: 0.5rem;
  padding: 0.55rem 1.1rem; border-radius: 9999px;
  font-family: inherit; font-size: 0.85rem; font-weight: 500;
  cursor: pointer; border: none; text-decoration: none;
  transition: background 150ms, box-shadow 150ms, transform 150ms;
}
.md-btn-outlined {
  background: transparent; color: var(--md-primary); border: 1px solid var(--md-outline);
}
.md-btn-outlined:hover { background: var(--md-elevation-1); border-color: var(--md-primary); }
.md-btn:disabled { opacity: 0.38; cursor: not-allowed; }

@media (max-width: 600px) {
  .cred-card-top { flex-direction: column; }
  .cred-logo { width: 60px; }
}
</style>