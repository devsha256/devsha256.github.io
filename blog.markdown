---
layout: default
title: Blog
permalink: /blog/
---
<link rel="stylesheet" href="/assets/css/blog.css">

{%- assign all_posts = site.posts | sort: 'date' | reverse -%}
{%- assign featured_posts = all_posts | where: 'featured', true -%}

{%- comment -%} Collect all unique tags across all posts {%- endcomment -%}
{%- assign all_tags = "" | split: "" -%}
{%- for post in all_posts -%}
  {%- for tag in post.tags -%}
    {%- unless all_tags contains tag -%}
      {%- assign all_tags = all_tags | push: tag -%}
    {%- endunless -%}
  {%- endfor -%}
{%- endfor -%}
{%- assign all_tags = all_tags | sort -%}

<div class="blog-page">

  <div class="blog-page-header">
    <h1 class="blog-page-title">Blog</h1>
    <p class="blog-page-subtitle">Thoughts on integration, architecture, and the craft of building software.</p>
  </div>

  {%- if featured_posts.size > 0 -%}
  <!-- ── Featured Posts ── -->
  <section class="featured-section" aria-label="Featured posts">
    <div class="section-label">✦ Featured</div>
    <div class="featured-grid">
      {%- for post in featured_posts -%}
      <a href="{{ post.url | relative_url }}" class="featured-card"
         data-tags="{{ post.tags | join: ',' | downcase }}">
        <div class="featured-card-tag-row">
          {%- for tag in post.tags -%}
          <span class="card-tag">{{ tag }}</span>
          {%- endfor -%}
        </div>
        <h2 class="featured-card-title">{{ post.title | escape }}</h2>
        <p class="featured-card-excerpt">{{ post.excerpt | strip_html | truncatewords: 35 }}</p>
        <div class="featured-card-meta">
          <time datetime="{{ post.date | date_to_xmlschema }}">
            {{ post.date | date: "%b %-d, %Y" }}
          </time>
          <span class="card-read-more">Read →</span>
        </div>
      </a>
      {%- endfor -%}
    </div>
  </section>
  {%- endif -%}

  <!-- ── Tag Filter ── -->
  {%- if all_tags.size > 0 -%}
  <section class="tag-filter-section" aria-label="Filter by tag">
    <div class="tag-filter-label">Filter by tag</div>
    <div class="tag-filter-row" id="tag-filter-row">
      <button class="tag-filter-chip active" data-tag="all" id="chip-all">
        All <span class="chip-count">({{ all_posts.size }})</span>
      </button>
      {%- for tag in all_tags -%}
        {%- assign tag_count = 0 -%}
        {%- for post in all_posts -%}
          {%- if post.tags contains tag -%}
            {%- assign tag_count = tag_count | plus: 1 -%}
          {%- endif -%}
        {%- endfor -%}
        <button class="tag-filter-chip" data-tag="{{ tag | downcase }}"
                id="chip-{{ tag | slugify }}">
          {{ tag }} <span class="chip-count">({{ tag_count }})</span>
        </button>
      {%- endfor -%}
    </div>
  </section>
  {%- endif -%}

  <!-- ── All Posts List ── -->
  <section class="all-posts-section" aria-label="All posts">
    <div class="section-label">All Posts</div>

    {%- if all_posts.size > 0 -%}
    <ul class="post-list" id="post-list">
      {%- for post in all_posts -%}
      <li class="post-list-item" data-tags="{{ post.tags | join: ',' | downcase }}">
        <div class="post-list-date-col">
          <div class="post-list-date">
            {{ post.date | date: "%b %-d" }}
            <span class="date-year">{{ post.date | date: "%Y" }}</span>
          </div>
        </div>
        <div class="post-list-body">
          <h3 class="post-list-title">
            <a href="{{ post.url | relative_url }}">{{ post.title | escape }}</a>
          </h3>
          {%- if post.excerpt -%}
          <p class="post-list-excerpt">{{ post.excerpt | strip_html | truncatewords: 25 }}</p>
          {%- endif -%}
          {%- if post.tags.size > 0 -%}
          <div class="post-list-tags">
            {%- for tag in post.tags -%}
            <span class="card-tag">{{ tag }}</span>
            {%- endfor -%}
          </div>
          {%- endif -%}
        </div>
      </li>
      {%- endfor -%}
    </ul>
    <p class="no-posts-msg" id="no-posts-msg" style="display:none;">
      No posts found for this tag.
    </p>
    {%- else -%}
    <p class="no-posts-msg">No posts yet — check back soon!</p>
    {%- endif -%}
  </section>

</div>

<script>
(function () {
  var chips    = document.querySelectorAll('.tag-filter-chip');
  var items    = document.querySelectorAll('.post-list-item');
  var featured = document.querySelectorAll('.featured-card');
  var noMsg    = document.getElementById('no-posts-msg');
  var activeTag = 'all';

  // Read tag from URL param on load
  var urlTag = new URLSearchParams(window.location.search).get('tag');
  if (urlTag) { activeTag = urlTag.toLowerCase(); }

  function applyFilter(tag) {
    activeTag = tag;

    // Update chips
    chips.forEach(function (chip) {
      chip.classList.toggle('active', chip.dataset.tag === tag);
    });

    // Filter post list
    var visible = 0;
    items.forEach(function (item) {
      var tags = item.dataset.tags ? item.dataset.tags.split(',') : [];
      var show = tag === 'all' || tags.includes(tag);
      item.classList.toggle('hidden', !show);
      if (show) visible++;
    });

    // Filter featured cards
    featured.forEach(function (card) {
      var tags = card.dataset.tags ? card.dataset.tags.split(',') : [];
      var show = tag === 'all' || tags.includes(tag);
      card.style.display = show ? '' : 'none';
    });

    // No results message
    if (noMsg) noMsg.style.display = visible === 0 ? 'block' : 'none';

    // Sync URL without page reload
    var url = new URL(window.location);
    if (tag === 'all') { url.searchParams.delete('tag'); }
    else { url.searchParams.set('tag', tag); }
    history.replaceState({}, '', url);
  }

  // Attach chip listeners
  chips.forEach(function (chip) {
    chip.addEventListener('click', function () { applyFilter(chip.dataset.tag); });
  });

  // Apply initial state
  applyFilter(activeTag);
})();
</script>
