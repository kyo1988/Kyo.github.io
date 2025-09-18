---
layout: page
title: "Case Studies"
permalink: /case-studies/
description: "CoreML optimization, RAG audits, finance-grade pipelines. Real-world implementations with measurable results."
---

<div class="case-studies-intro">
  <p>Real-world implementations with measurable results. Each case study includes technical details, performance metrics, and live demonstrations.</p>
  <div class="case-studies-cta">
    <a href="https://www.visageaiconsulting.com/en?utm_source=blog&utm_medium=case_studies&utm_campaign=web_app" target="_blank" rel="noopener" class="btn btn-primary">Try Live Demos</a>
    <a href="https://apps.apple.com/app/visage-ai-skin-advisor/id6748892785?utm_source=blog&utm_medium=case_studies&utm_campaign=mobile_app" target="_blank" rel="noopener" class="btn btn-outline">Download iOS App</a>
  </div>
</div>

<div class="case-studies-grid">
{% assign cases = site.posts | where_exp:"p","p.tags contains 'Case-Study'" %}
{% for p in cases %}
  <div class="case-study-card">
    <h3><a href="{{ p.url | relative_url }}">{{ p.title }}</a></h3>
    <p class="case-description">{{ p.description }}</p>
    <div class="case-study-actions">
      <a href="{{ p.url | relative_url }}" class="btn btn-secondary">Read Case Study</a>
      <a href="https://www.visageaiconsulting.com/en?utm_source=blog&utm_medium=case_study&utm_campaign={{ p.title | slugify }}" target="_blank" rel="noopener" class="btn btn-outline">Live Demo</a>
    </div>
  </div>
{% endfor %}
</div>

{% if cases.size == 0 %}
<div class="no-cases">
  <p>Case studies are being prepared. Check back soon for detailed technical implementations and performance metrics.</p>
  <a href="https://www.visageaiconsulting.com/en?utm_source=blog&utm_medium=case_studies_empty&utm_campaign=web_app" target="_blank" rel="noopener" class="btn btn-primary">Explore Web App</a>
</div>
{% endif %}
