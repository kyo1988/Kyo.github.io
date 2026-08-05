---
layout: post
title: "EBM-2025 Analysis Status: Code Audit and Withdrawn Claims"
date: 2025-09-27 14:00:00 +0900
last_modified_at: 2026-08-05 00:00:00 +0900
categories: [Marketing Science, Data Analysis]
tags: [Marketing Science, Ehrenberg-Bass, Replication Audit, Research Integrity]
permalink: /marketing/2025/09/27/marketing-science-analysis-status.html
description: "August 2026 correction: five EBM-2025 claims and the resulting marketing recommendations are withdrawn after a code audit."
suppress_default_cta: true
---

> **Correction — August 2026**
>
> This article originally presented the EBM-2025 pipeline as a specification-compliant analysis with decision-ready marketing implications. A subsequent audit of the code, configuration, and logs found that several statements exceeded what the implementation measured. Five claims and all strategy or budget recommendations derived from them are withdrawn. This page retains the published URL and the archived numerical outputs so that the correction is explicit rather than silent.

The corrected report is [EBM-2025 v0.2: Public-data replication audit](https://www.visageaiconsulting.com/en/whitepaper/ebm-2025). The [v0.2 PDF](https://www.visageaiconsulting.com/whitepapers/ebm-2025-v0.2.pdf) contains the methods, code-audit findings, limits, and references. The [original v0.1 PDF](https://www.visageaiconsulting.com/whitepapers/ebm-2025-v0.1.pdf) remains archived and is superseded.

## Series navigation

- [Duplication of Purchase: a near-miss that did not pass]({{ site.baseurl }}/marketing/2025/09/27/duplication-of-purchase-near-miss.html)
- [Double Jeopardy: failed project gate, inconclusive replication]({{ site.baseurl }}/marketing/2025/09/27/double-jeopardy-analysis-fail.html)
- [Category Entry Points: language-bias claim withdrawn]({{ site.baseurl }}/marketing/2025/09/27/category-entry-points-analysis.html)
- [Buyer-frequency persistence and NBD: claims narrowed]({{ site.baseurl }}/marketing/2025/09/27/moderation-dirichlet-analysis.html)

## TL;DR

The original project asked whether four archived public-data pipelines reproduced patterns associated with Ehrenberg-Bass marketing science. The 2026 code audit changes the answer: one Duplication of Purchase output was close to an internal gate, Double Jeopardy failed two project checks, and the buyer-frequency, CEP, and NBD outputs do not measure the stronger constructs originally attributed to them.

The project remains useful for a different reason. It shows how an analysis can run to completion, emit plausible numbers and figures, and still lose the connection between a named method and the quantity implemented in code. The corrected articles document those breaks at the estimator, resampling, temporal-order, grouping, and configuration-schema levels.

No marketing action follows directly from the archive. A new study can use it as a failure map: define the market and constructs first, pre-specify gates, correct the estimators, and rerun on traceable inputs.

## What the project attempted to measure

The four analysis families answer different questions and should not be treated as one composite validation score.

- **Duplication of Purchase (DoP):** whether buyers of one label also buy other labels in proportions related to those labels' penetration.
- **Double Jeopardy (DJ):** whether lower-penetration labels also have lower average buying frequency among their buyers.
- **Buyer-frequency persistence:** whether transaction frequency in one observed quarter is associated with frequency in an adjacent quarter, conditional on an outcome-derived purchase-volume group.
- **Category Entry Points (CEP):** whether review text can be mapped to intended lexical dimensions across languages and normalized brands.
- **NBD diagnostic:** whether an estimated purchase-frequency distribution produces predictions that match observed behavior.

The datasets were not observations from one market. The archive combined grocery orders, household retail transactions, giftware invoices, and Amazon reviews. Category construction, buyer identifiers, observation windows, and label definitions differed across pipelines. Cross-pipeline agreement cannot therefore be interpreted as triangulation on one consumer process.

## Project-defined gates

The archived DoP gate was weighted MAD ≤0.015, with an alternative rule based on an interval upper bound and additional prerequisite checks. The reported summary took the form

`MAD_w = Σ_A w_A · mean_B | P(B|A) − Pen(B) |`.

The archived Double Jeopardy gate required Pearson r≥0.80 and a lower interval bound ≥0.70. These were internal project rules. They were not universal rejection thresholds supplied by Ehrenberg-Bass theory, and passing or failing them would not by itself validate or refute the underlying empirical regularity.

## Corrected status

The 2025 project is an exploratory replication audit. It is not a validated replication, a client case study, or a marketing playbook.

| Analysis | Archived output | Gate or check | Defensible conclusion |
|---|---:|---:|---|
| Duplication of Purchase, dunnhumby | weighted MAD 0.015863 | ≤0.015 | The run failed; it was a near-miss to the project gate |
| Duplication of Purchase, Instacart | weighted MAD 0.021854 | ≤0.015 | The run failed |
| Double Jeopardy, UCI | Pearson r=0.627 | ≥0.80 | The run failed its project gate and stationarity check |
| Buyer-frequency persistence, UCI Q4 | R²=0.472 | no confirmatory gate | Descriptive adjacent-quarter association only |
| CEP lexical pipeline, Amazon | r=-0.280 | no valid language-bias test | Not interpretable because the parser and configuration schemas disagree |
| NBD diagnostic, UCI | R²≈-7×10⁻⁶ | no valid goodness-of-fit test | Not an NBD fit result; the evaluation predicted the sample mean |

These outputs do not support causal marketing recommendations. The archive contains no experiment connecting them to cross-sell revenue, reach expansion, localization performance, buyer targeting, or return on investment.

## Reading the numerical outputs

### Duplication of Purchase

The dunnhumby output is the closest archived run to its internal threshold. The weighted value exceeded the gate by 0.000863. The Instacart comparison was farther away. These are descriptive outputs from the archived pipeline, not confirmatory estimates, because the matrix construction, weights, interval, temporal shuffle, and run-selection process all require correction.

### Double Jeopardy

Pearson r=0.627 is below the project's 0.80 criterion, and the stationarity flag also failed. The point estimate is still a correlation across derived labels in one transformed dataset. It cannot determine whether the empirical law fails in a validly defined beauty market.

### Buyer-frequency persistence

The Q4 regression had the largest within-sample R². Because purchase-volume groups were recalculated from contemporaneous outcomes and the model contained no intervention, this is a descriptive persistence result. It is neither a moderation effect of marketing contact nor evidence that high-volume buyers should receive more budget.

### CEP and NBD

Both pipelines lost their intended constructs in implementation. The CEP output does not compare languages or normalized brands. The NBD evaluation does not use fitted-distribution predictions. Their numerical outputs are retained to locate the failure, not to characterize market behavior or model fit.

## Withdrawn claims

### 1. Top-decile Double Jeopardy deviation

No top-decile or middle-quantile split exists in the Double Jeopardy script. The reported r=0.627 was computed across all 27 retained labels. It failed the project's 0.80 gate, but that failure does not establish that the Double Jeopardy law fails in the beauty category: the category and label fields were produced by project-specific heuristics from a giftware dataset.

### 2. R²=0.472 as response to an additional contact

The regression contains no contact, campaign, treatment, price, or stock variable. It measures association between transaction counts in adjacent observed quarters. Q4 had the largest within-sample association under the grouping rule; no causal or incremental-sales interpretation follows.

### 3. CEP coverage rising from 38% to 52%

The archived output contains no before/after comparison and no intervention. The reported increase and the associated accuracy statement are withdrawn.

### 4. Language-bias detection across 27 languages

The logged run retained one language and excluded 27 language codes. It also used ASINs as brand identifiers. The value r=-0.280 is therefore not a multilingual language-bias result.

### 5. Poor Dirichlet model fit

The fitting routine estimated negative-binomial parameters, but the evaluation path predicted the same sample mean for every user. R²≈-7×10⁻⁶ evaluates a constant-mean predictor, not the fitted NBD distribution or a full NBD-Dirichlet model.

## Implementation findings

The audit identified defects that prevent confirmatory interpretation:

- the Duplication of Purchase matrix copied one directional conditional rate into both directions;
- weights were calculated after deduplication and therefore reflected retained buyer counts rather than purchase counts;
- the reported “BCa” intervals were percentile resamples and did not calculate bias correction or acceleration;
- the weekly shuffle ran after user-label pairs had been reduced to one row, leaving repeated weeks structurally unavailable;
- the Double Jeopardy bootstrap lost replacement multiplicity and used a denominator inconsistent with the point estimate;
- the CEP parser expected a schema different from the supplied configuration;
- the NBD evaluation compared observations with a constant mean rather than fitted-distribution predictions.

Fourteen Duplication of Purchase filter combinations were examined, and the closest result was selected after those runs. The 0.015 threshold was an internal project rule, not a universal rejection boundary from the underlying theory.

## What remains supported

The weighted dunnhumby Duplication of Purchase statistic did not cross its pre-set gate. The simplified unweighted statistic was not substituted after the result was known to manufacture a pass. That decision remains correct.

The negative and uninterpretable results also identify the requirements for a new study: fixed constructs and gates before analysis, corrected estimators, versioned code, traceable inputs, a clean-environment rerun, and independent review. Those requirements have not yet been met.

## Data and reproduction status

The archive names four source families: dunnhumby Complete Journey, Instacart, UCI Online Retail II, and Amazon Review Data (2018). The raw data are not bundled with this blog or the report. Instacart and dunnhumby also require account- or terms-mediated acquisition.

The dunnhumby, Instacart, and Amazon logs retain input hash prefixes. The UCI runs record their inputs only as `loaded`, and the analysis directory is not tied to a recorded Git commit. The original one-hour reproduction statement was never demonstrated through a clean-environment rerun. Reproduction therefore means rebuilding the analysis under a new versioned specification, not replaying the published commands and assuming identity with the original environment.

## What a valid follow-up would change

1. Define category, brand, buyer, penetration, purchase, and observation window before examining outcomes.
2. Freeze one implementation for each estimator and test it against small hand-calculated fixtures.
3. Resample independent buyers or households rather than derived matrix cells.
4. Preserve temporal information until after negative controls and stationarity checks run.
5. Separate descriptive association, predictive evaluation, and causal intervention claims.
6. Record input hashes, code commit, environment lockfile, and all attempted specifications.
7. Require an independent clean-environment rerun before describing the result as a replication.

## References

- Ehrenberg, A.S.C. (1988). *Repeat-Buying: Facts, Theory and Applications*.
- Sharp, B. (2010). *How Brands Grow*.

---

{% include cta-whitepaper.html %}
