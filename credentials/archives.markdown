---
layout: default
title: Credentials - Archives
permalink: /credentials/archives/
nav_include: no
---

<div id="archive-root"></div>

<script crossorigin src="https://unpkg.com/react@18/umd/react.development.js"></script>
<script crossorigin src="https://unpkg.com/react-dom@18/umd/react-dom.development.js"></script>

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

  function ArchiveApp() {
    const PAGE_SIZE = 6;
    const [search, setSearch] = useState("");
    const [page, setPage] = useState(1);

    const filtered = useMemo(() => {
      const query = search.trim().toLowerCase();
      return !query || query.length < 3
        ? archives
        : archives.filter(a => a.name.toLowerCase().includes(query));
    }, [search]);

    const pageCount = Math.ceil(filtered.length / PAGE_SIZE);
    const currentItems = useMemo(
      () => filtered.slice((page - 1) * PAGE_SIZE, page * PAGE_SIZE),
      [filtered, page]
    );

    useEffect(() => {
      if (page > pageCount) setPage(1);
    }, [pageCount]);

    return e("div", { className: "archives" },
      e("div", { className: "search-container" },
        e("input", {
          type: "text",
          placeholder: "Search by name...",
          value: search,
          onChange: e => setSearch(e.target.value),
          style: { width: "60%", padding: "10px", fontSize: "16px" }
        })
      ),

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

      e("div", { className: "instruction", style: { position: "fixed", bottom: 0, left: 0, width: "100%", backgroundColor: "#f8f8f8", color: "#555", padding: "10px", textAlign: "center", zIndex: 1000 } },
        "Click on the verify star to see a live document."
      )
    );
  }

  ReactDOM.createRoot(document.getElementById("archive-root")).render(e(ArchiveApp));
</script>

<style>
  .search-container {
    text-align: center;
    margin-bottom: 20px;
  }

  .search-container input {
    width: 60%;
    padding: 10px;
    font-size: 16px;
    border: 1px solid #ddd;
    border-radius: 5px;
    outline: none;
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
</style>