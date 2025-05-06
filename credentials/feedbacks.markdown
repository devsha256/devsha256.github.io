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
  const searchParams = new URLSearchParams(window.location.search);
  const uuid = searchParams.get("id");
  const page = parseInt(searchParams.get("page")) || PAGE_NUMBER;
  const size = parseInt(searchParams.get("size")) || PAGE_SIZE;
  return { uuid, page, size };
}

function FeedbackApp() {
  const { uuid, page, size } = getParams();
  const [pageSize, setPageSize] = useState(size);
  const [currentPage, setCurrentPage] = useState(1);

  useEffect(() => {
    let index = 0;

    if (uuid) {
      const matchIndex = sortedFeedbacks.findIndex(feedback => feedback.id === uuid);
      if (matchIndex !== -1) {
        index = matchIndex;
      }
    } else if (page) {
      const pageIndex = (page - 1) * pageSize;
      if (pageIndex >= 0 && pageIndex < sortedFeedbacks.length) {
        index = pageIndex;
      }
    }

    const newPage = Math.floor(index / pageSize) + 1;
    setCurrentPage(newPage);

    if (pageSize === 1) {
      updateURL(sortedFeedbacks[index]?.id, newPage, pageSize);
    } else {
      updateURL(null, newPage, pageSize);
    }
  }, []);

  function updateURL(id, page, size) {
    const searchParams = new URLSearchParams();
    if (id && size === 1) {
      searchParams.set("id", id);
    } else {
      searchParams.set("size", size);
    }
    searchParams.set("page", page);
    const newUrl = `/credentials/feedbacks/?${searchParams.toString()}`;
    history.replaceState(null, '', newUrl);
  }

  const startIndex = (currentPage - 1) * pageSize;
  const endIndex = startIndex + pageSize;
  const visibleFeedbacks = sortedFeedbacks.slice(startIndex, endIndex);

  const handleNext = () => {
    const newPage = currentPage + 1;
    setCurrentPage(newPage);
    const index = (newPage - 1) * pageSize;
    if (pageSize === 1) {
      updateURL(sortedFeedbacks[index]?.id, newPage, pageSize);
    } else {
      updateURL(null, newPage, pageSize);
    }
  };

  const handlePrev = () => {
    const newPage = currentPage - 1;
    setCurrentPage(newPage);
    const index = (newPage - 1) * pageSize;
    if (pageSize === 1) {
      updateURL(sortedFeedbacks[index]?.id, newPage, pageSize);
    } else {
      updateURL(null, newPage, pageSize);
    }
  };

  return React.createElement('div', { className: 'feedbacks' },
    React.createElement('div', { className: 'pagination' },
      React.createElement('button', { onClick: handlePrev, disabled: currentPage === 1 }, 'Previous'),
      ` Page ${currentPage} / ${Math.ceil(sortedFeedbacks.length / pageSize)} `,
      React.createElement('button', { onClick: handleNext, disabled: currentPage === Math.ceil(sortedFeedbacks.length / pageSize) }, 'Next')
    ),
    React.createElement('ul', { className: 'feedback-list' },
      visibleFeedbacks.map(feedback =>
        React.createElement('li', { key: feedback.id, className: 'feedback-item' },
          React.createElement('a', { href: feedback.cred_link, target: '_blank' },
            React.createElement('img', { src: `/assets/img/logos/${feedback.image}`, alt: feedback.name, className: 'feed-logo' })
          ),
          React.createElement('h2', { className: 'feed-name' }, feedback.name),
          React.createElement('p', null, React.createElement('strong', null, 'Authority: '), feedback.authority),
          React.createElement('p', null, React.createElement('strong', null, 'Date: '), feedback.date),
          React.createElement('blockquote', null, feedback.comment),
          React.createElement('p', { className: 'verify-row' },
            React.createElement('strong', null, 'Verify it live: '),
            feedback.drive_link && React.createElement('a', { href: feedback.drive_link, target: '_blank', className: 'stars-container', title: 'View Original' },
              React.createElement('span', { className: 'stars' },
                Array.from({ length: 5 }, (_, i) =>
                  React.createElement('svg', {
                    key: i,
                    className: 'star',
                    viewBox: '0 0 24 24',
                    width: 26,
                    height: 26,
                    xmlns: 'http://www.w3.org/2000/svg'
                  },
                    React.createElement('path', { d: 'M12 .587l3.668 7.57L24 9.748l-6 5.848 1.415 8.258L12 19.771l-7.415 4.083L6 15.596 0 9.748l8.332-1.591z' })
                  )
                )
              )
            ),
            !feedback.drive_link && React.createElement('span', null, 'Not Available')
          )
        )
      )
    ),
    React.createElement('div', { className: 'instruction' }, 'Click on the verify star to see the original feedback (if available).')
  );
}

document.addEventListener('DOMContentLoaded', () => {
  const { uuid, page, size } = getParams();
  if (!uuid && !page && sortedFeedbacks.length > 0) {
    const firstId = sortedFeedbacks[0].id;
    const newUrl = `/credentials/feedbacks/?id=${firstId}&page=1`;
    history.replaceState(null, '', newUrl);
  }
  ReactDOM.render(
    React.createElement(FeedbackApp),
    document.getElementById('feedbacks-root')
  );
});
</script>

<style>
.feedbacks {
  font-family: Arial, sans-serif;
  margin: 20px;
}

.feedback-list {
  list-style: none;
  padding: 0;
}

.feedback-item {
  border-bottom: 2px solid #ddd;
  padding: 15px;
  margin-bottom: 20px;
}

.feed-name {
  margin-top: 0;
}

.feed-logo {
    margin-top: 20px;
    max-width: 100px;
    height: auto;
    float: right;
  }

.pagination {
  text-align: center;
  margin: 20px 0;
}

.pagination button {
  padding: 8px 15px;
  margin: 0 5px;
  cursor: pointer;
}

.verify-row {
  margin-top: 10px;
  font-size: 1rem;
}

.stars-container {
  display: inline-block;
  position: relative;
  overflow: hidden;
  text-decoration: none;
  height: 20px;
}

.stars {
  display: flex;
  width: 100px;
  height: 20px;
}

.star {
  fill: #ccc;
  transition: fill 0.3s ease;
  margin: 0 2px;
}

.stars-container:hover .star {
  fill: gold;
}

.instruction {
  position: fixed;
  bottom: 0;
  left: 0;
  width: 100%;
  background-color: #f8f8f8;
  color: #555;
  padding: 10px;
  text-align: center;
  z-index: 1000;
  animation: ziggle 0.5s infinite alternate;
}

@keyframes ziggle {
  0% {
    transform: translateX(-5px);
  }
  100% {
    transform: translateX(5px);
  }
}
</style>