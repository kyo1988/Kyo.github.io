---
layout: post
title: "Buyer-Frequency Persistence and NBD: Claims Narrowed After Code Audit"
date: 2025-09-27 13:00:00 +0900
last_modified_at: 2026-08-05 00:00:00 +0900
categories: [Marketing Science, Data Analysis]
tags: [Buyer Frequency, Negative Binomial Distribution, Replication Audit, Research Integrity]
permalink: /marketing/2025/09/27/moderation-dirichlet-analysis.html
description: "August 2026 correction: Q4 R²=0.472 is a descriptive adjacent-quarter association, while the reported NBD result evaluates a constant-mean predictor."
suppress_default_cta: true
---

> **Correction — August 2026**
>
> The original article interpreted Q4 R²=0.472 as response to an additional marketing contact and treated R²≈0 as poor Dirichlet fit. Both claims are withdrawn. The regression contains no contact or treatment variable, and the NBD evaluation predicted the sample mean rather than using the fitted distribution.

Read the [corrected EBM-2025 v0.2 report](https://www.visageaiconsulting.com/en/whitepaper/ebm-2025) or the [v0.2 PDF](https://www.visageaiconsulting.com/whitepapers/ebm-2025-v0.2.pdf). The [original v0.1 PDF](https://www.visageaiconsulting.com/whitepapers/ebm-2025-v0.1.pdf) is archived and superseded.

## Series navigation

- [Duplication of Purchase analysis]({{ site.baseurl }}/marketing/2025/09/27/duplication-of-purchase-near-miss.html)
- [Double Jeopardy analysis]({{ site.baseurl }}/marketing/2025/09/27/double-jeopardy-analysis-fail.html)
- [Category Entry Points analysis]({{ site.baseurl }}/marketing/2025/09/27/category-entry-points-analysis.html)
- [Corrected analysis status]({{ site.baseurl }}/marketing/2025/09/27/marketing-science-analysis-status.html)

## TL;DR

The archived quarterly regression produced its largest within-sample association in Q4: standardized slope 3.341 and R²=0.472. This is a descriptive adjacent-quarter frequency result. It does not measure response to an additional marketing contact and does not establish that high-volume buyers are the most valuable intervention target.

The separate NBD routine successfully returned fitted parameters, but its evaluation assigned every user the sample mean. R²≈-7×10⁻⁶ therefore evaluates a constant predictor, not the fitted negative-binomial distribution or an NBD-Dirichlet model.

## Two different analyses

The original article combined a buyer-frequency regression and a distribution-fitting exercise. They should be read separately.

- **Buyer-frequency persistence:** association between transaction counts in adjacent recorded quarters within purchase-volume groups.
- **NBD diagnostic:** estimation of a negative-binomial purchase-frequency distribution followed by an attempted goodness-of-fit evaluation.

Neither analysis contained a marketing intervention. “Moderation” in the filename did not mean that contact frequency or campaign exposure moderated an outcome.

## Archived buyer-frequency method

The UCI transaction rows were aggregated to user-quarter observations. Within each quarter, purchase-volume quartiles Q1–Q4 were recalculated from the observed outcome. The script then standardized the current transaction count and regressed a shifted adjacent-quarter count on it within each quartile using ordinary least squares.

The variable named `freq_t1` points to the previous recorded quarter under the implemented shift. The name suggests a forward outcome, but the code's temporal direction is reversed relative to that label. This does not erase the observed association; it changes what the coefficient describes.

## Buyer-frequency result

The UCI analysis assigned users to purchase-volume quartiles within each quarter, then regressed transaction frequency in one observed quarter on the adjacent observed quarter within each quartile. The predictor was standardized before estimation.

| Purchase-volume quartile | Observations | Users | Standardized slope | R² |
|---|---:|---:|---:|---:|
| Q1 | 126 | 107 | -0.002 | 0.00001 |
| Q2 | 88 | 76 | 0.321 | 0.196 |
| Q3 | 77 | 67 | 0.765 | 0.204 |
| Q4 | 190 | 120 | 3.341 | 0.472 |

Q4 had the strongest within-sample association under this grouping rule. The result states that adjacent-quarter transaction counts were more predictable among the highest purchase-volume observations in the archived sample.

![Archived buyer-frequency plot. Q4 has the largest within-sample association, but the analysis contains no marketing-contact variable or treatment.](https://res.cloudinary.com/dgqphttst/image/upload/v1758994483/buyer_moderation_bodycare_vylepe.png)

*Figure 1. Archived adjacent-quarter frequency regressions by contemporaneously defined purchase-volume quartile. The chart is descriptive and non-causal.*

## Why the Q4 pattern can become stronger mechanically

Quartile membership is defined from purchase volume in each observed quarter rather than from a fixed pre-period. High-volume groups also have greater variance. Grouping on an outcome-related variable and then regressing nearby outcomes can produce larger slopes and R² values even without a segment-specific response mechanism.

The reported Q1–Q4 gradient is therefore an object for follow-up, not proof of a behavioral treatment effect. The archived analysis also does not establish that all quartile coefficients are stable across later periods or out of sample.

## What R²=0.472 does not identify

The regression contains no marketing-contact variable, campaign exposure, treatment assignment, price, or stock measure. It does not estimate the effect of an additional contact and cannot explain incremental sales or expected return on a targeting budget.

The script's shifted value points to the previous recorded quarter, while quartile membership is recalculated from purchase volume in each quarter. Outcome-related grouping and the greater variance of high-volume buyers can mechanically increase the Q4 association. A predictive follow-up would need a fixed baseline cohort, explicit time direction, and held-out later periods. A causal follow-up would additionally need an identified exposure or randomized treatment.

## Archived NBD method and output

The NBD routine estimated parameters from purchase counts and recorded solver success. The archive reported mean purchases of 19.48, standard deviation 181.9, and R²≈-7×10⁻⁶. Successful optimization only means that the fitting procedure returned a solution; it does not show that the fitted model was used correctly downstream.

The NBD models a category purchase-frequency distribution. A full NBD-Dirichlet analysis would additionally model brand choice probabilities across a valid category-by-brand-by-buyer panel. The archived evaluation did not reach that test.

## Withdrawn Dirichlet-fit claim

The archive reports fitted negative-binomial parameters and R²≈-7×10⁻⁶. The evaluation path, however, assigns the same sample-mean prediction to every user. The resulting R² evaluates a constant-mean predictor. It does not evaluate predictions from the fitted NBD distribution and does not test a full NBD-Dirichlet model.

The archived result therefore cannot support either good or poor Dirichlet fit.

The archived P-P plot remains available as a pipeline artifact: [NBD diagnostic plot](https://res.cloudinary.com/dgqphttst/image/upload/v1758994484/dirichlet_pp_plot_bodycare_ilunrn.png). Because the evaluation path supplied constant-mean predictions, the plot should not be interpreted as fitted-distribution performance.

## Reproduction record

The archived entry points were:

```bash
poetry run python scripts/eb/compute_moderation.py \
  --tx data/processed/tx_uci_beauty_with_categories.csv \
  --category_regex bodycare

poetry run python scripts/eb/compute_dirichlet.py \
  --tx data/processed/tx_uci_beauty_with_categories.csv \
  --category_regex bodycare
```

The logs identify the input only as `loaded` and do not record a Git commit. The commands document the original execution path but do not constitute an exact reproduction package.

## Claim boundary

The Q4 value is a descriptive adjacent-quarter association. It does not support heavy-buyer targeting, contact-frequency changes, budget allocation, or an optimization claim. The NBD output is an implementation diagnostic, not a model-fit result.

## Reimplementation requirements

For prediction, define quartiles from a fixed baseline period, preserve forward time direction, and evaluate on held-out future quarters. For causal response, add an identified exposure or randomized treatment and prevent post-treatment purchase volume from defining the groups. For NBD evaluation, generate expected frequencies or probabilities from the fitted parameters and compare those predictions with observations using pre-specified diagnostics.

## References

- Goodhardt, G.J., Ehrenberg, A.S.C., & Chatfield, C. (1984). “The Dirichlet: A Comprehensive Model of Buying Behaviour.” *Journal of the Royal Statistical Society: Series A*, 147(5), 621–643. [https://doi.org/10.2307/2981696](https://doi.org/10.2307/2981696)
- Chen, D. (2012). *Online Retail II*. UCI Machine Learning Repository. [https://doi.org/10.24432/C5CG6D](https://doi.org/10.24432/C5CG6D)

---

{% include cta-whitepaper.html %}
