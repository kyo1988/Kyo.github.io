---
layout: post
title: "Duplication of Purchase: A Near-Miss That Did Not Pass"
date: 2025-09-27 11:00:00 +0900
last_modified_at: 2026-08-05 00:00:00 +0900
categories: [Marketing Science, Data Analysis]
tags: [Duplication of Purchase, Ehrenberg-Bass, Replication Audit, Research Integrity]
permalink: /marketing/2025/09/27/duplication-of-purchase-near-miss.html
description: "August 2026 correction: weighted MAD 0.015863 did not pass the 0.015 project gate, and implementation defects prevent confirmatory interpretation."
suppress_default_cta: true
---

> **Correction — August 2026**
>
> The original article treated a near-miss as practical validation for cross-sell investment and described the implementation as specification-compliant. Those interpretations are withdrawn. The archived weighted MAD did not pass its gate, and the audited estimator, interval, and negative-control paths require reimplementation.

Read the [corrected EBM-2025 v0.2 report](https://www.visageaiconsulting.com/en/whitepaper/ebm-2025) or the [v0.2 PDF](https://www.visageaiconsulting.com/whitepapers/ebm-2025-v0.2.pdf). The [original v0.1 PDF](https://www.visageaiconsulting.com/whitepapers/ebm-2025-v0.1.pdf) is archived and superseded.

## Series navigation

- [Double Jeopardy analysis]({{ site.baseurl }}/marketing/2025/09/27/double-jeopardy-analysis-fail.html)
- [Category Entry Points analysis]({{ site.baseurl }}/marketing/2025/09/27/category-entry-points-analysis.html)
- [Buyer-frequency and NBD analysis]({{ site.baseurl }}/marketing/2025/09/27/moderation-dirichlet-analysis.html)
- [Corrected analysis status]({{ site.baseurl }}/marketing/2025/09/27/marketing-science-analysis-status.html)

## TL;DR

The archived dunnhumby run returned weighted MAD=0.015863 against a pre-set 0.015 gate. It missed by 0.000863. The correct label is **near-miss and FAIL**, not practical validation.

That distinction is only the first layer. Code inspection found that the conditional duplication matrix was forced to be symmetric, the purported purchase-count weights were calculated after deduplication, and the reported interval did not implement BCa resampling. The number remains useful as a record of what the pipeline emitted, but it cannot support inference or cross-sell decisions until the estimator is rebuilt.

## Background

Duplication of Purchase describes overlap between buyer groups. For a focal label A and another label B, a directional duplication rate can be written as `P(B|A)`: the share of A buyers who also bought B. The comparison quantity `Pen(B)` is B's penetration in the defined market and observation window.

The archived project summarized deviations between pairwise duplication and penetration through a weighted mean absolute deviation:

`MAD_w = Σ_A w_A · mean_B | P(B|A) − Pen(B) |`.

A smaller value indicated closer agreement under the project's implementation. The 0.015 gate was defined by the project; it is not a universal theoretical boundary. The prerequisite that the median retained labels per user be at least two was intended to prevent a duplication analysis on a cohort with almost no repertoire overlap.

## Archived design

The selected run used the dunnhumby Complete Journey transactions after a project-specific beauty mapping. It applied:

- a 26-week observation window;
- a user purchase-count filter at or above the 0.90 quantile;
- at least two retained labels per user;
- at least 20 buyers per label;
- random seed 42;
- 5,000 reported resamples.

After filtering, the pipeline reduced the transactions to a binary user-by-label table and constructed a pairwise duplication matrix. The selected output contained 1,735 users and 46 labels.

## Archived result

The closest archived run used a 26-week dunnhumby beauty slice, retained users at or above the 0.90 purchase-count quantile, required at least two labels per user, and required at least 20 buyers per label. The resulting matrix contained 1,735 users and 46 labels.

| Metric | Archived output | Gate | Decision |
|---|---:|---:|---|
| Weighted MAD | 0.015863 | ≤0.015 | FAIL |
| Gap to gate | +0.000863 | — | Near-miss |
| Unweighted MAD | 0.015143 | not the confirmatory metric | No decision |
| Logged interval | [0.014792, 0.016928] | — | Descriptive only |
| Median labels per user | 2.0 | ≥2.0 | Met |
| Negative-control MAD | 0.015629 | ≤0.05 under the project rule | Met under that rule |

The Instacart comparison recorded weighted MAD=0.021854 on 1,617 users and 129 labels. It also failed the 0.015 project gate. Its lower unweighted MAD cannot replace the pre-specified weighted result after inspection of the outputs.

![Archived duplication matrix for the selected dunnhumby run. The figure is retained as pipeline output, not as evidence of a validated estimator.](https://res.cloudinary.com/dgqphttst/image/upload/v1758994485/dop_heat_dunnhumby_beauty_spec_q90_b2_m20_n2rd5h.png)

*Figure 1. Archived duplication matrix for the selected dunnhumby run. Its summary value was weighted MAD=0.015863. The code-audit qualifications below apply to both the matrix and the summary.*

## Weighted and unweighted results are not interchangeable

The archive also contains lower unweighted values, including 0.015143 for the selected dunnhumby run and 0.011934 for the Instacart comparison. An unweighted mean gives each retained pair equal influence; the archived weighted calculation gave larger retained labels more influence through an outer product of label counts.

The project had selected the weighted quantity as its decision statistic. Substituting an unweighted value after observing that it crosses a threshold would change the estimand and the decision rule together. The original analysis correctly did not make that substitution. The audit does not change that point.

## Specification search

The archive examined fourteen filter combinations rather than one frozen specification. The varied dimensions included:

- user purchase-count quantiles from 0.60 to 0.95;
- minimum retained labels per user;
- minimum buyers per label;
- 13- and 26-week windows;
- category mappings across datasets.

The reported dunnhumby result came from the combination closest to the internal gate: top-decile users by purchase count, at least two labels per user, at least 20 buyers per label, and a 26-week window. Selection after comparing outputs makes the result exploratory. A new confirmatory run would select and register those conditions before accessing the evaluation data.

## Why the near-miss is not validation

The distance from an internal gate does not measure the probability that the Duplication of Purchase law is true. Fourteen filter combinations were examined, and the reported dunnhumby run was selected as the closest result. A confirmatory design would fix the market definition, observation window, inclusion rules, estimator, and decision gate before examining new data.

The code audit found four implementation problems:

1. The script calculated a directional conditional duplication rate and copied it into both halves of a symmetric matrix.
2. It reduced the data to one user-label row before calculating the values used as weights. The weights therefore represent retained buyer counts, not purchase counts.
3. The logged interval resampled pairwise matrix cells and reported percentile bounds. It was not a bias-corrected and accelerated bootstrap over independent buyers or households.
4. The weekly shuffle was applied after each user-label pair had been reduced to one row, so repeated purchase weeks were no longer available to shuffle.

These defects prevent the result from operating as a confirmatory estimate. The point estimate remains an archived pipeline output.

## Reproduction record

The archived command was:

```bash
poetry run python scripts/eb/compute_dop_specification_compliant.py \
  --tx data/processed/tx_dunnhumby_beauty.csv \
  --category_regex beauty \
  --min_buyers 20 \
  --top_user_quantile 0.9 \
  --min_brand_count_per_user 2 \
  --window_weeks 26 \
  --bca 5000 \
  --seed 42
```

The corresponding [archived log]({{ site.baseurl }}/logs/run_dop_dunnhumby_beauty_spec_q90_b2_m20.jsonl) records an input hash prefix and the emitted statistics. Re-running this command can reproduce the implementation's behavior only if the same private processed input and environment are available. It does not remedy the estimator defects.

## Claim boundary

The defensible statement is narrow: no archived specification-labelled run crossed the pre-set weighted-MAD gate. Calling 0.015863 a near-miss is accurate; calling it a pass, practical validation, or evidence for cross-sell allocation is not.

## Reimplementation requirements

A new DoP analysis should preserve both directional rates rather than mirror one triangle, define the weights from the intended pre-aggregation purchase or buyer unit, and resample independent buyers or households. Temporal negative controls must run before time information is discarded. The category definition, window, filters, estimator, and gate should be frozen before the new evaluation data are inspected.

## References

- Ehrenberg, A.S.C. (1988). *Repeat-Buying: Facts, Theory and Applications*.
- Sharp, B. (2010). *How Brands Grow*.

---

{% include cta-whitepaper.html %}
