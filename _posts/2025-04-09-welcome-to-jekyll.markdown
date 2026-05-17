---
layout: post
title: "Getting Started with Jekyll on GitHub Pages"
date: 2025-04-09 00:35:31 +0530
tags: [jekyll, github-pages, web]
featured: true
excerpt: "A practical guide to setting up your own Jekyll-powered portfolio hosted on GitHub Pages — from zero to live in under an hour."
---

You'll find all posts in the `_posts` directory. Jekyll requires blog post files to be named according to this format:

```
YEAR-MONTH-DAY-title.MARKUP
```

Where `YEAR` is a four-digit number, `MONTH` and `DAY` are both two-digit numbers, and `MARKUP` is the file extension (`md` or `markdown`). After that, include the necessary front matter — a YAML block at the top of the file between triple-dashes.

## Why Jekyll?

Jekyll is a **static site generator** — it takes your Markdown files and transforms them into a complete, deployable website. Because the output is pure HTML/CSS/JS, it can be hosted for free on GitHub Pages.

Key advantages:
- **Zero server costs** — GitHub Pages hosts static files for free
- **Fast** — no database queries, no backend rendering
- **Version controlled** — your entire site, content and all, lives in Git
- **Markdown-first** — write content naturally, not in a CMS

## Front Matter

Every post starts with YAML front matter between `---` delimiters:

```yaml
---
layout: post
title: "My Post Title"
date: 2025-04-09 00:00:00 +0530
tags: [jekyll, web, tutorial]
featured: true
excerpt: "A short summary shown on the blog list page."
---
```

The `featured: true` flag causes the post to appear in the **Featured** section at the top of the blog list.

## Code Highlighting

Jekyll supports syntax highlighting out of the box using Liquid tags:

{% highlight ruby %}
def greet(name)
  puts "Hello, #{name}! Welcome to Jekyll."
end
greet('Saddam')
#=> Hello, Saddam! Welcome to Jekyll.
{% endhighlight %}

Or with standard Markdown fenced code blocks:

```javascript
const experience = (start) => {
  const months = (new Date() - new Date(start)) / (1000 * 60 * 60 * 24 * 30.44);
  return `${Math.floor(months / 12)}.${String(Math.round(months % 12)).padStart(2, '0')} years`;
};
console.log(experience('2020-02-24'));
```

## Next Steps

- Check out the [Jekyll docs](https://jekyllrb.com/docs/home) for full reference
- Browse [GitHub Pages documentation](https://docs.github.com/en/pages) for deployment
- Customise your `_config.yml` with your own site metadata
