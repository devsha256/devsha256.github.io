---
layout: default
title: Credentials - Certifications
permalink: /credentials/certifications/
nav_include: no
---

<div id="certifications-root"></div>

<script crossorigin src="https://unpkg.com/react@18/umd/react.production.min.js"></script>
<script crossorigin src="https://unpkg.com/react-dom@18/umd/react-dom.production.min.js"></script>

<script>
  const PAGE_NUMBER = 1;
  const PAGE_SIZE = 1;
  const { useState, useEffect } = React;

  const certifications = {{ site.data.certifications | jsonify }};
  const sortedCerts = certifications.slice().sort((a, b) => new Date(b.date) - new Date(a.date));

  function getParams() {
    const searchParams = new URLSearchParams(window.location.search);
    const uuid = searchParams.get("id");
    const page = parseInt(searchParams.get("page")) || PAGE_NUMBER;
    const size = parseInt(searchParams.get("size")) || PAGE_SIZE;
    return { uuid, page, size };
  }

  function CertificationApp() {
    const { uuid, page, size } = getParams();
    const [pageSize, setPageSize] = useState(size);
    const [currentPage, setCurrentPage] = useState(1);

    useEffect(() => {
      let index = 0;

      if (uuid) {
        const matchIndex = sortedCerts.findIndex(cert => cert.id === uuid);
        if (matchIndex !== -1) {
          index = matchIndex;
        }
      } else if (page) {
        const pageIndex = (page - 1) * pageSize;
        if (pageIndex >= 0 && pageIndex < sortedCerts.length) {
          index = pageIndex;
        }
      }

      const newPage = Math.floor(index / pageSize) + 1;
      setCurrentPage(newPage);

      if (pageSize === 1) {
        updateURL(sortedCerts[index]?.id, newPage, pageSize);
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
      const newUrl = `/credentials/certifications/?${searchParams.toString()}`;
      history.replaceState(null, '', newUrl);
    }

    const startIndex = (currentPage - 1) * pageSize;
    const endIndex = startIndex + pageSize;
    const visibleCerts = sortedCerts.slice(startIndex, endIndex);

    const handleNext = () => {
      const newPage = currentPage + 1;
      setCurrentPage(newPage);
      const index = (newPage - 1) * pageSize;
      if (pageSize === 1) {
        updateURL(sortedCerts[index]?.id, newPage, pageSize);
      } else {
        updateURL(null, newPage, pageSize);
      }
    };

    const handlePrev = () => {
      const newPage = currentPage - 1;
      setCurrentPage(newPage);
      const index = (newPage - 1) * pageSize;
      if (pageSize === 1) {
        updateURL(sortedCerts[index]?.id, newPage, pageSize);
      } else {
        updateURL(null, newPage, pageSize);
      }
    };

    return React.createElement('div', { className: 'certifications' },
      React.createElement('div', { className: 'pagination' },
        React.createElement('button', { onClick: handlePrev, disabled: currentPage === 1 }, 'Previous'),
        ` Page ${currentPage} / ${Math.ceil(sortedCerts.length / pageSize)} `,
        React.createElement('button', { onClick: handleNext, disabled: currentPage === Math.ceil(sortedCerts.length / pageSize) }, 'Next')
      ),
      React.createElement('ul', { className: 'certification-list' },
        visibleCerts.map(cert =>
          React.createElement('li', { key: cert.id, className: 'certification-item' },
            React.createElement('a', { href: cert.cred_link, target: '_blank' },
              React.createElement('img', { src: `/assets/img/certifications/${cert.image}`, alt: cert.name, className: 'cert-logo' })
            ),
            React.createElement('h2', { className: 'cert-name' }, cert.name),
            React.createElement('p', null, React.createElement('strong', null, 'Authority: '), cert.authority),
            React.createElement('p', null, React.createElement('strong', null, 'Date: '), cert.date),
            React.createElement('p', null, React.createElement('strong', null, 'Credential ID: '), cert.credential_id),
            React.createElement('p', { className: 'verify-row' },
              React.createElement('strong', null, 'Verify it live: '),
              React.createElement('a', { href: cert.drive_link, target: '_blank', className: 'stars-container', title: 'View Credential' },
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
              )
            )
          )
        )
      ),
      React.createElement('div', { className: 'instruction' }, 'Click on the verify star to see a live document.')
    );
  }

  document.addEventListener('DOMContentLoaded', () => {
    const { uuid, page, size } = getParams();
    if (!uuid && !page && sortedCerts.length > 0) {
      const firstId = sortedCerts[0].id;
      const newUrl = `/credentials/certifications/?id=${firstId}&page=1`;
      history.replaceState(null, '', newUrl);
    }
    ReactDOM.render(
      React.createElement(CertificationApp),
      document.getElementById('certifications-root')
    );
  });
</script>

<style>

  .certification-list {
    list-style: none;
    padding: 0;
  }

  .certification-item {
    border-bottom: 2px solid #ddd;
    padding-right: 15px;
    margin-bottom: 20px;
  }

  .cert-logo {
    margin-top: 20px;
    max-width: 100px;
    height: auto;
    float: right;
  }

  .cert-name {
    margin-top: 0;
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
