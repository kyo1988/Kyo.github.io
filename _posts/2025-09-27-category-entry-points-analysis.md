---
layout: post
title: "Category Entry Points: Language-Bias Claim Withdrawn"
date: 2025-09-27 11:00:00 +0900
last_modified_at: 2026-08-05 00:00:00 +0900
categories: [Marketing Science, Data Analysis]
tags: [Category Entry Points, Marketing Analytics, Replication Audit, Research Integrity]
permalink: /marketing/2025/09/27/category-entry-points-analysis.html
description: "August 2026 correction: the CEP run retained one language, used ASINs as brands, and did not measure multilingual language bias or a coverage improvement."
suppress_default_cta: true
---

> **Correction — August 2026**
>
> The original article described a completed multilingual Category Entry Points analysis, inferred English-centric bias, and recommended localization changes. Those claims and recommendations are withdrawn. The audited pipeline retained one language, treated ASINs as brand identifiers, and parsed the CEP configuration under the wrong schema.

Read the [corrected EBM-2025 v0.2 report](https://www.visageaiconsulting.com/en/whitepaper/ebm-2025) or the [v0.2 PDF](https://www.visageaiconsulting.com/whitepapers/ebm-2025-v0.2.pdf). The [original v0.1 PDF](https://www.visageaiconsulting.com/whitepapers/ebm-2025-v0.1.pdf) is archived and superseded.

## Series navigation

- [Duplication of Purchase analysis]({{ site.baseurl }}/marketing/2025/09/27/duplication-of-purchase-near-miss.html)
- [Double Jeopardy analysis]({{ site.baseurl }}/marketing/2025/09/27/double-jeopardy-analysis-fail.html)
- [Buyer-frequency and NBD analysis]({{ site.baseurl }}/marketing/2025/09/27/moderation-dirichlet-analysis.html)
- [Corrected analysis status]({{ site.baseurl }}/marketing/2025/09/27/marketing-science-analysis-status.html)

## TL;DR

The archived pipeline processed one million Amazon review rows and returned lexical-coverage aggregates. It did not complete the multilingual brand-level Category Entry Points analysis described in the original article.

The mismatch is specific. The parser read the lexicon under a schema different from the configuration, retained one language, and passed ASIN product identifiers through a brand-normalization path that expected brand names. The output is still useful for diagnosing the pipeline, but r=-0.280 cannot be interpreted as language bias or a penetration-coverage trade-off.

## Intended measurement

Category Entry Points are situations, needs, motives, or contexts that buyers associate with a category or brand. The archived project attempted a lexical proxy: search review text for terms grouped into dimensions such as quality, value, innovation, sustainability, and convenience, then compare coverage across languages and brands.

That proxy already narrows the construct. A substring hit in a review is not direct evidence that a CEP was available in memory at purchase. At minimum, the pipeline still needed to preserve the intended dimension, language, and normalized-brand axes. The implementation did not do so.

## Archived pipeline

The script:

- read up to 1,000,000 Amazon review rows in 100,000-row chunks;
- detected a language code for each review;
- required at least 20 rows per ASIN-language cell;
- searched configured substrings in review text;
- calculated Wilson intervals for lexical hit proportions;
- aggregated hit rates by the identifiers it labelled as brands;
- correlated total review count with mean lexical coverage.

Wilson intervals can be calculated correctly while the variables entering them represent the wrong construct. The audit therefore separates arithmetic validity from measurement validity.

## What the archived run produced

The Amazon pipeline processed 1,000,000 review rows and wrote 256 aggregate rows covering 58 ASINs. It reported Pearson r=-0.280 between total review count per ASIN and mean lexical hit rate.

That coefficient is not a test of multilingual language bias. The audit log shows one retained language (`en`) and 27 excluded language codes. A one-language output cannot support a comparison across languages.

## Schema failures

Two mismatches changed the construct measured by the pipeline.

1. The configuration was organized as `language → dimension → terms`, while the parser expected `dimension → language → terms`. The output consequently recorded `en` as the sole CEP category instead of the intended dimensions: quality, value, innovation, sustainability, and convenience.
2. The parser passed ASIN values into a nested normalization dictionary that expected brand-name keys. The retained “brands” were product identifiers.

The variable labelled penetration was total review count, not buyer penetration. The value r=-0.280 is a correlation between ASIN review volume and malformed lexical coverage. It cannot confirm a penetration-coverage trade-off.

![Archived CEP coverage output. The visualization reflects the parser's malformed category and identifier structure, not a validated multilingual brand comparison.](https://res.cloudinary.com/dgqphttst/image/upload/v1758994484/cep_coverage_complete_fk9rhy.png)

*Figure 1. Archived lexical-coverage output. The figure is retained to document the pipeline result; it should not be read as evidence of English dominance or multilingual brand coverage.*

## Logged counts

The run wrote 256 aggregate rows covering 58 ASINs and reported 618,066 excluded cells below its minimum threshold. The log recorded one retained language (`en`) and 27 excluded language codes.

Those counts describe filtering behavior, not multilingual coverage. “Detected,” “retained,” and “compared” are different states: detecting language codes upstream does not create a 27-language analysis when only one language survives into the output.

## Withdrawn coverage claim

No archived log or output contains a before/after test in which bottom-five CEP coverage increased from 38% to 52%. No intervention was recorded. The claimed increase and its associated accuracy statement are withdrawn.

The archived CEP-stratified Duplication of Purchase demo also reported zero users after mapping. Its unweighted result is not evidence of a passed replication.

## CEP-stratified DoP demo

The original article presented an unweighted MAD from a CEP-stratified demonstration as a PASS. The same artifact reported zero users because the brand mapping did not produce an analyzable cohort. A metric emitted after the population has collapsed cannot validate the stratification logic. This demo remains a test fixture for repairing mappings, not a positive result.

## Reproduction record

The archived command was:

```bash
poetry run python scripts/stp/compute_cep_coverage.py \
  --input $AMAZON_RAW_DIR/amazon_reviews.tsv \
  --chunk_size 100000
```

The associated log retained an input SHA prefix. Replaying the command against the same file would reproduce the schema mismatch unless the parser or configuration is changed. A corrected implementation should receive a new version and output path rather than silently replacing the archived result.

## Claim boundary

This run is a failed measurement prototype. It does not establish English-centric bias, compare 27 languages, identify localization opportunities, or justify localization spending. A new implementation must align the lexicon and parser schemas, normalize actual brands, define buyer penetration from buyer records, and specify the language comparison before examining outcomes.

## Reimplementation requirements

1. Validate the lexicon schema before processing data and fail on an unexpected axis order.
2. Normalize verified brand names before aggregation; keep ASIN as a separate product identifier.
3. Define penetration from unique buyers in a specified market and window, not from review volume.
4. Report detected, excluded, and retained languages separately.
5. Pre-specify the minimum cell size and how sparse languages will be handled.
6. Treat lexical review coverage as a text proxy unless it is validated against an independent CEP measure.

## Data references

- Ni, J., Li, J., & McAuley, J. (2019). “Justifying Recommendations using Distantly-Labeled Reviews and Fine-Grained Aspects.” *Proceedings of EMNLP-IJCNLP 2019*, 188–197. [https://doi.org/10.18653/v1/D19-1018](https://doi.org/10.18653/v1/D19-1018)
- McAuley Lab, UC San Diego. [Amazon Review Data (2018)](https://cseweb.ucsd.edu/~jmcauley/datasets/amazon_v2/).

---

{% include cta-whitepaper.html %}
