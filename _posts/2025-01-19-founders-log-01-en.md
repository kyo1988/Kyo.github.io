---
layout: post
title: "Founder's Log #01 — Weekly Update"
description: "This week's Built / Learned / One-chart / One-link. Jekyll 3 compatibility patch application and build stabilization achievements."
tags: [Log, Founder, Jekyll, GitHub-Pages]
og_image: /images/log-01.png
last_modified_at: 2025-01-19
lang: en
---

{% include tldr.html text="This week's decisions: Jekyll 3 compatibility patch for build stabilization. Numbers: 20 consecutive failures → success. Next week: gradual feature restoration." %}

## Built

- **Jekyll 3 Compatibility Patch**: Changed array parameter includes to delimiter-based approach
- **Build Stabilization**: Resolved 20 consecutive failures, normal operation on GitHub Pages
- **Liquid Syntax Optimization**: Removed absolute_url and strip_newlines filters
- **JSON-LD Implementation**: Jekyll 3.10.0 compatible structured data

## Learned

- **Jekyll 3.10.0 Limitations**: Importance of pre-investigating GitHub Pages constraints
- **Incremental Approach**: Order of minimal configuration → feature restoration is crucial
- **Liquid Compatibility**: Array parameters are unstable, delimiters are reliable

## One-chart

<figure>
  {% include img-cloudinary.html path="/charts/build-success.png" w="1200" alt="Build success progression" %}
  <figcaption>Improvement from 20 consecutive failures to stable builds. Effect of Jekyll 3 compatibility patch.</figcaption>
</figure>

## Q&A

{% include qa.html items="What was the goal?::Resolve the root cause of 20 consecutive build failures||How was it evaluated?::Local build success + GitHub Pages automatic build success||What's the next step?::Gradual restoration of new features and content expansion" %}

## Sources

- [Jekyll 3.10.0 Documentation](https://jekyllrb.com/docs/3.10.0/)
- [GitHub Pages Jekyll Version](https://pages.github.com/versions/)
- [Liquid Template Language](https://shopify.github.io/liquid/)

{% include cta.html %}
{% include related-by-tags.html %}
