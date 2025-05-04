---
layout: default
title: Credentials - Archives
permalink: /credentials/archives/
nav_include: no
---

<div id="archive-root"></div>

<script crossorigin src="https://unpkg.com/react@18/umd/react.production.min.js"></script>
<script crossorigin src="https://unpkg.com/react-dom@18/umd/react-dom.production.min.js"></script>

<script>
  const e = React.createElement;
  const { useState, useMemo, useEffect } = React;

  const archives = [
    {% assign sorted_archives = site.data.archives | sort: 'date' | reverse %}
    {% for arch in sorted_archives %}
    {
      name: {{ arch.name | jsonify }},
      authority: {{ arch.authority | jsonify }},
      date: {{ arch.date | jsonify }},
      credential_id: {{ arch.credential_id | jsonify }},
      cred_link: {{ arch.cred_link | jsonify }},
      drive_link: {{ arch.drive_link | jsonify }},
      image: "/assets/img/logos/{{ arch.image }}"
    },
    {% endfor %}
  ];

  function parseQuery(queryString) {
    const params = new URLSearchParams(queryString);
    return {
      search: params.get("search") || "",
      page: parseInt(params.get("page") || "1", 10)
    };
  }

  function ArchiveApp() {
    const PAGE_SIZE = 6;
    const queryParams = parseQuery(window.location.search);
    const [search, setSearch] = useState(queryParams.search);
    const [page, setPage] = useState(isNaN(queryParams.page) || queryParams.page < 1 ? 1 : queryParams.page);

    const filtered = useMemo(() => {
      const query = search.trim().toLowerCase();

      if (!query || query.length < 3) return archives;

      let result = archives;

      const nameMatch = query.match(/^name:(.*)$/);
      const dateMatch = query.match(/^date:(\d{4}-\d{2}-\d{2})$/);
      const authMatch = query.match(/^authority:(.*)$/);

      if (nameMatch) {
        const term = nameMatch[1].trim();
        result = archives.filter(a => a.name.toLowerCase().includes(term));
      } else if (authMatch) {
        const term = authMatch[1].trim();
        result = archives.filter(a => a.authority.toLowerCase().includes(term));
      } else if (dateMatch) {
        const fromDate = new Date(dateMatch[1]);
        result = archives.filter(a => new Date(a.date) >= fromDate);
      } else {
        result = archives.filter(a => a.name.toLowerCase().includes(query));
      }
      return result;
    }, [search]);

    const pageCount = Math.ceil(filtered.length / PAGE_SIZE);
    const isPageValid = page >= 1 && page <= pageCount;

    const currentItems = useMemo(() => {
      if (!isPageValid) return [];
      return filtered.slice((page - 1) * PAGE_SIZE, page * PAGE_SIZE);
    }, [filtered, page, isPageValid]);

    useEffect(() => {
      const url = new URL(window.location);
      if (search) {
        url.searchParams.set("search", search);
      } else {
        url.searchParams.delete("search");
      }
      if (page > 1) {
        url.searchParams.set("page", page);
      } else {
        url.searchParams.delete("page");
      }
      window.history.replaceState({}, "", url);
    }, [search, page]);

    return e("div", { className: "archives" },
      e("div", { className: "search-container" },
        e("input", {
          type: "text",
          placeholder: "Search by name, date, authority...",
          value: search,
          onChange: e => setSearch(e.target.value),
          className: "search-input"
        }),
        e("div", { className: "tooltip" },
          e("span", { className: "tooltip-icon" }, "?"),
          e("div", { className: "tooltip-box" },
            e("div", null, "Search keys:"),
            e("div", null, 'name:java'),
            e("div", null, 'authority:udemy'),
            e("div", null, "date:2023-01-30")
          )
        )
      ),

      (filtered.length === 0 || !isPageValid) ?
        e("div", { className: "no-result" },
          filtered.length === 0 && e("p", null, `Searched : '${search}' has no result`),
          !isPageValid && e("p", null, `Page Number : ${page} not found`)
        ) :
        [
          e("div", { className: "pagination" },
            e("button", { onClick: () => setPage(p => Math.max(1, p - 1)), disabled: page === 1 }, "Previous"),
            ` ${page} / ${pageCount} `,
            e("button", { onClick: () => setPage(p => Math.min(pageCount, p + 1)), disabled: page >= pageCount }, "Next")
          ),
          e("ul", { className: "archive-grid" },
            currentItems.map((arch, i) =>
              e("li", { className: "archive-item", key: i },
                e("a", { href: arch.cred_link, target: "_blank" },
                  e("img", { src: arch.image, alt: arch.name, className: "arch-logo" })
                ),
                e("h2", { className: "arch-name" }, arch.name),
                e("p", null, e("strong", null, "Authority: "), arch.authority),
                e("p", null, e("strong", null, "Date: "), arch.date),
                e("p", null, e("strong", null, "Credential ID: "), arch.credential_id),
                e("p", { className: "verify-row" },
                  e("strong", null, "Verify it live: "),
                  e("a", { href: arch.drive_link, target: "_blank", className: "stars-container" },
                    e("span", { className: "stars" },
                      Array.from({ length: 5 }).map((_, idx) =>
                        e("svg", { className: "star", viewBox: "0 0 24 24", width: 20, height: 20, key: idx },
                          e("path", { d: "M12 .587l3.668 7.57L24 9.748l-6 5.848 1.415 8.258L12 19.771l-7.415 4.083L6 15.596 0 9.748l8.332-1.591z" })
                        )
                      )
                    )
                  )
                )
              )
            )
          ),
          e("div", { className: "total-label" }, `Total: ${filtered.length}`)
        ],

      e("div", { className: "instruction", style: { position: "fixed", bottom: 0, left: 0, width: "100%", backgroundColor: "#f8f8f8", color: "#555", padding: "10px", textAlign: "center", zIndex: 1000 } },
        "Click on the verify star to see a live document."
      )
    );
  }

  ReactDOM.createRoot(document.getElementById("archive-root")).render(e(ArchiveApp));
</script>

<style>
  body {
    font-family: Arial, sans-serif;
    margin: 0;
    padding: 0;
  }

  .archives-container {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    padding: 30px;
  }

  .search-container {
    display: flex;
    justify-content: center;
    align-items: center;
    gap: 10px;
    margin-bottom: 30px;
  }

  .search-input {
    width: 60%;
    padding: 12px;
    font-size: 18px;
    border: 1px solid #ccc;
    border-radius: 5px;
  }
  .tooltip {
    position: relative;
    display: inline-block;
    cursor: pointer;
  }

  .tooltip-icon {
    background-color: #000;
    color: #fff;
    border-radius: 50%;
    padding: 4px 8px;
    font-size: 14px;
    line-height: 1;
    user-select: none;
  }

  .tooltip-box {
    display: none;
    position: absolute;
    top: 120%;
    left: 0;
    background-color: #000;
    color: #fff;
    padding: 8px 12px;
    border-radius: 4px;
    white-space: nowrap;
    font-size: 13px;
    z-index: 1000;
  }

  .tooltip:hover .tooltip-box {
    display: block;
  }

  .no-result {
    color: #000;
    font-size: 20px;
    margin-top: 40px;
    border: 1px solid #ddd;
    border-radius: 8px;
    padding: 15px;
    text-align: center;
    font-family: sans-serif;
  }

  .archives {
    font-family: Arial, sans-serif;
    margin: 20px;
  }

  .archive-grid {
    list-style: none;
    padding: 0;
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    grid-gap: 20px;
  }

  .archive-item {
    border: 1px solid #ddd;
    border-radius: 8px;
    padding: 15px;
    position: relative;
    min-height: 200px;
  }

  .arch-logo {
    max-width: 80px;
    height: auto;
    position: absolute;
    bottom: 10px;
    right: 10px;
  }

  .arch-name {
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
    margin-left: 5px;
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
    0% { transform: translateX(-5px); }
    100% { transform: translateX(5px); }
  }

  .total-label {
    text-align: center;
    margin-top: 20px;
    font-size: 20px;
    color: #000;
  }
</style>