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

  const PAGE_SIZE_OPTIONS = [3, 6, 12, 24];
  const DEFAULT_PAGE_SIZE = 6;

  function parseQuery(qs) {
    const params = new URLSearchParams(qs);
    const rawSize = parseInt(params.get("size") || String(DEFAULT_PAGE_SIZE), 10);
    return {
      search: params.get("search") || "",
      page: parseInt(params.get("page") || "1", 10),
      size: PAGE_SIZE_OPTIONS.includes(rawSize) ? rawSize : DEFAULT_PAGE_SIZE
    };
  }

  function ArchiveApp() {
    const qp = parseQuery(window.location.search);
    const [search, setSearch] = useState(qp.search);
    const [page, setPage] = useState(isNaN(qp.page) || qp.page < 1 ? 1 : qp.page);
    const [pageSize, setPageSize] = useState(qp.size);

    const filtered = useMemo(() => {
      const query = search.trim().toLowerCase();
      if (!query || query.length < 3) return archives;

      let result = archives;
      const params = query.split(",").map(p => p.trim());
      let nameTerms = [], authorityTerms = [], dateValues = [];

      params.forEach(param => {
        const nm = param.match(/^name:(.*)$/);
        const dt = param.match(/^date:(\d{4}-\d{2}-\d{2})$/);
        const au = param.match(/^authority:(.*)$/);
        if (nm) nameTerms.push(nm[1].trim());
        else if (au) authorityTerms.push(au[1].trim());
        else if (dt) dateValues.push(new Date(dt[1]));
      });

      let fromDate = null, toDate = null;
      if (dateValues.length === 1) { fromDate = dateValues[0]; toDate = new Date(); }
      else if (dateValues.length >= 2) {
        fromDate = new Date(Math.min(...dateValues.map(d => d.getTime())));
        toDate   = new Date(Math.max(...dateValues.map(d => d.getTime())));
      }

      if (nameTerms.length) result = result.filter(a => nameTerms.some(t => a.name.toLowerCase().includes(t)));
      if (authorityTerms.length) result = result.filter(a => authorityTerms.some(t => a.authority.toLowerCase().includes(t)));
      if (fromDate && toDate) result = result.filter(a => {
        const d = new Date(a.date); return d >= fromDate && d <= toDate;
      });
      return result;
    }, [search]);

    const pageCount = Math.ceil(filtered.length / pageSize);
    const isPageValid = page >= 1 && page <= pageCount;
    const currentItems = useMemo(() => {
      if (!isPageValid) return [];
      return filtered.slice((page - 1) * pageSize, page * pageSize);
    }, [filtered, page, pageSize, isPageValid]);

    function handlePageSizeChange(newSize) {
      setPageSize(newSize);
      setPage(1);
    }

    useEffect(() => {
      const url = new URL(window.location);
      search ? url.searchParams.set("search", search) : url.searchParams.delete("search");
      page > 1 ? url.searchParams.set("page", page) : url.searchParams.delete("page");
      pageSize !== DEFAULT_PAGE_SIZE ? url.searchParams.set("size", pageSize) : url.searchParams.delete("size");
      window.history.replaceState({}, "", url);
    }, [search, page, pageSize]);

    return e("div", { className: "archive-page" },
      e("div", { className: "creds-page-header" },
        e("a", { href: "/credentials/", className: "back-link" }, "← Credentials"),
        e("h1", null, "Learning History")
      ),

      e("div", { className: "search-container" },
        e("input", {
          type: "text",
          placeholder: "Search by name, date, authority…",
          value: search,
          onChange: ev => { setSearch(ev.target.value); setPage(1); },
          className: "search-input"
        }),
        e("div", { className: "tooltip" },
          e("span", { className: "tooltip-icon" }, "?"),
          e("div", { className: "tooltip-box" },
            e("div", null, "Search keys (comma-separated):"),
            e("div", null, "  name:java"),
            e("div", null, "  authority:udemy"),
            e("div", null, "  date:2023-01-30")
          )
        )
      ),

      (filtered.length === 0 || !isPageValid)
        ? e("div", { className: "no-result" },
            filtered.length === 0 && e("p", null, `No results for: "${search}"`),
            !isPageValid && filtered.length > 0 && e("p", null, `Page ${page} not found`)
          )
        : [
            e("div", { className: "md-pagination", key: "pag" },
              e("button", { className: "md-btn md-btn-outlined", onClick: () => setPage(p => Math.max(1, p - 1)), disabled: page === 1 }, "← Prev"),
              e("span", { className: "page-info" }, `${page} / ${pageCount}`),
              e("button", { className: "md-btn md-btn-outlined", onClick: () => setPage(p => Math.min(pageCount, p + 1)), disabled: page >= pageCount }, "Next →"),
              e("div", { className: "page-size-control" },
                e("label", { className: "page-size-label", htmlFor: "archive-page-size" }, "Per page:"),
                e("select", {
                  id: "archive-page-size",
                  className: "page-size-select",
                  value: pageSize,
                  onChange: ev => handlePageSizeChange(parseInt(ev.target.value, 10))
                },
                  PAGE_SIZE_OPTIONS.map(opt =>
                    e("option", { key: opt, value: opt }, opt)
                  )
                )
              )
            ),
            e("ul", { className: "archive-grid", key: "grid" },
              currentItems.map((arch, i) =>
                e("li", { className: "archive-item", key: i },
                  e("a", { href: arch.cred_link, target: "_blank", rel: "noopener" },
                    e("img", { src: arch.image, alt: arch.name, className: "arch-logo" })
                  ),
                  e("h2", { className: "arch-name" }, arch.name),
                  e("p", null, e("strong", null, "Authority: "), arch.authority),
                  e("p", null, e("strong", null, "Date: "), arch.date),
                  arch.credential_id && e("p", null, e("strong", null, "ID: "), arch.credential_id),
                  e("div", { className: "verify-row" },
                    e("strong", null, "Verify: "),
                    e("a", { href: arch.drive_link, target: "_blank", rel: "noopener", className: "stars-container" },
                      e("span", { className: "stars" },
                        Array.from({ length: 5 }).map((_, idx) =>
                          e("svg", { className: "star", viewBox: "0 0 24 24", width: 18, height: 18, key: idx },
                            e("path", { d: "M12 .587l3.668 7.57L24 9.748l-6 5.848 1.415 8.258L12 19.771l-7.415 4.083L6 15.596 0 9.748l8.332-1.591z" })
                          )
                        )
                      )
                    )
                  )
                )
              )
            ),
            e("div", { className: "total-label", key: "total" }, `Showing ${currentItems.length} of ${filtered.length} entries`)
          ],

      e("div", { className: "instruction", key: "hint" }, "✨ Click the stars to view a live document.")
    );
  }

  ReactDOM.createRoot(document.getElementById("archive-root")).render(e(ArchiveApp));
</script>