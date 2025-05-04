---
layout: default
title: Credentials - Archives
permalink: /credentials/archives/
nav_include: no
---
<link rel="stylesheet" href="/assets/css/archive.css">
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
      const params = query.split(",").map(param => param.trim());

      let nameTerms = [];
      let authorityTerms = [];
      let dateValues = [];

      params.forEach(param => {
        const nameMatch = param.match(/^name:(.*)$/);
        const dateMatch = param.match(/^date:(\d{4}-\d{2}-\d{2})$/);
        const authorityMatch = param.match(/^authority:(.*)$/);

        if (nameMatch) {
          nameTerms.push(nameMatch[1].trim());
        } else if (authorityMatch) {
          authorityTerms.push(authorityMatch[1].trim());
        } else if (dateMatch) {
          dateValues.push(new Date(dateMatch[1])); // Properly convert date
        }
      });

      let fromDate = null;
      let toDate = null;

      if (dateValues.length === 1) {
        fromDate = dateValues[0];
        toDate = new Date(); // Default to today
      } else if (dateValues.length === 2) {
        fromDate = new Date(Math.min(...dateValues.map(d => d.getTime()))); // Older date
        toDate = new Date(Math.max(...dateValues.map(d => d.getTime()))); // Newer date
      }

      // Apply filters
      if (nameTerms.length) {
        result = result.filter(a => nameTerms.some(term => a.name.toLowerCase().includes(term)));
      }

      if (authorityTerms.length) {
        result = result.filter(a => authorityTerms.some(term => a.authority.toLowerCase().includes(term)));
      }

      if (fromDate && toDate) {
        result = result.filter(a => {
          const archiveDate = new Date(a.date);
          return archiveDate >= fromDate && archiveDate <= toDate;
        });
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
            e("div", null, "Search keys: (separated by comma)"),
            e("div", null, 'Available Options'),
            e("div", null, '- name:java'),
            e("div", null, '- authority:udemy'),
            e("div", null, "- date:2023-01-30")
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