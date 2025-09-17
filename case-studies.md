---
layout: page
title: "Case Studies"
permalink: /case-studies/
description: "CoreML optimization, RAG audits, finance-grade pipelines."
---

<ul>
{% assign cases = site.posts | where_exp:"p","p.tags contains 'Case-Study'" %}
{% for p in cases %}
  <li><a href="{{ p.url | relative_url }}">{{ p.title }}</a> — {{ p.description }}</li>
{% endfor %}
</ul>
