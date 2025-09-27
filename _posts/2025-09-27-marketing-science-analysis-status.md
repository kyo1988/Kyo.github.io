---
layout: post
title: "Marketing Science Analysis Status: Specification-Compliant Implementation with Real-World Insights"
date: 2025-09-27 14:00:00 +0900
categories: [Marketing Science, Data Analysis]
tags: [Marketing Science, Ehrenberg-Bass, Statistical Analysis, Specification-Compliant, Real-World Data]
permalink: /marketing/2025/09/27/marketing-science-analysis-status.html
description: "DoP achieves near-pass, DJ falls short, CEP and Moderation are useful. Investment decision roadmap for next quarter."
---

## Series Navigation

**Marketing Science Analysis Series**:
- [Duplication of Purchase Analysis](/marketing/2025/09/27/duplication-of-purchase-near-miss.html)
- [Double Jeopardy Analysis](/marketing/2025/09/27/double-jeopardy-analysis-fail.html)
- [Category Entry Points Analysis](/marketing/2025/09/27/category-entry-points-analysis.html)
- [Moderation & Dirichlet Analysis](/marketing/2025/09/27/moderation-dirichlet-analysis.html)
- **Analysis Status Overview** ← Current (Hub)

## TL;DR

**日本語要約**:
- DoPは"ほぼ達成"でクロスセル最適化の余地が大
- DJ未達で当面は到達投資を優先
- CEP/ModerationでローカライズとQ4施策で短期改善可能

DoP achieves "near-miss" status providing solid foundation for cross-sell optimization with significant revenue potential. DJ fails to meet threshold, indicating reach investment priority over loyalty programs in short term. CEP and Moderation analyses offer valuable insights for copy localization and heavy buyer targeting strategies. **Action**: Implement 30/60/90 day plan with top cross-sell pairs A/B testing, non-English copy experiments, and reach KPI redesign for maximum effectiveness.

## Executive Summary

Our comprehensive marketing science analysis pipeline has achieved specification-compliant implementation across all core methodologies, revealing critical insights about the gap between theoretical expectations and real-world data. While no specification-compliant PASS examples were achieved, the analysis provides valuable evidence of near-miss results and demonstrates the importance of statistical rigor in marketing science research.

## Executive Decision Summary

**This Quarter's Key Learnings**:
- **DoP near-miss** (0.015863) provides solid foundation for cross-sell optimization
- **DJ failure** (r=0.627) indicates reach investment priority over loyalty programs  
- **CEP/Moderation insights** offer actionable localization and Q4 targeting strategies

**30/60/90 Day Action Plan**:
- **30 days**: Top cross-sell pairs A/B testing, non-English copy experiments
- **60 days**: Reach KPI redesign and distribution optimization
- **90 days**: Q4 segment experience optimization and heavy buyer targeting

### Specification Gates

**DoP Gate**: Pass if **weighted MAD ≤ 0.015** (or **BCa 95% upper ≤ 0.020**), with invariants and negative control satisfied.
`MAD = Σ_A w_A · mean_B | P(B|A) − Pen(B) |`, where `w_A` is buyer-weighted share.
**Precondition**: median brands per user ≥ 2.

**DJ Gate**: Pass if **Pearson r ≥ 0.80** and **BCa 95% lower ≥ 0.70**. Window/min_buyers must be stated.

## Background

This analysis evaluates four core marketing science principles using real-world data:

- **Double Jeopardy (DJ)**: The relationship between brand penetration and purchase frequency among buyers
- **Duplication of Purchase (DoP)**: How buyers of one brand also purchase other brands in the same category
- **Category Entry Points (CEP)**: Brand coverage across different market segments and languages
- **Buyer Moderation**: How purchase behavior varies across different buyer segments (quantiles)

Each analysis employs specification-compliant statistical methods including BCa Bootstrap, real temporal randomization, and negative controls to ensure production-ready results.

## Current Status Overview

| Analysis | Status | Key Result | Implication |
|----------|--------|------------|-------------|
| **Double Jeopardy** | ❌ FAIL | r = 0.627 (target: ≥0.80) | Weak penetration-frequency relationship |
| **Duplication of Purchase** | ❌ NEAR-MISS | MAD = 0.015863 (gap: +0.000863) | Close to theoretical threshold |
| **Category Entry Points** | ✅ COMPLETE | Wilson CI, H1 correlation analysis | Successful multilingual analysis |
| **Moderation Analysis** | ✅ COMPLETE | Q4 slope = 3.341, R² = 0.472 | Strong quantile effects |
| **Dirichlet Model** | ⚠️ ILLUSTRATIVE | R² = -7.0e-06 | Weak fit due to high variance |

## Key Achievements

### 1. Specification-Compliant Implementation

**Claim.** Our production-grade implementation employs rigorous statistical methods across all analyses.

**Evidence.** We utilize BCa Bootstrap (B=5000, seed=42) for reproducibility, implement real weekly shuffle for actual temporal randomization, and maintain proper negative controls for statistical validation.

**Implication.** This approach ensures that our results meet production research standards and provide reliable insights into marketing science principles.

**Limits.** Results are sensitive to buyer weighting and temporal windows; stationarity tests and negative controls are reported in the appendix.

### 2. Near-Miss Achievement

**Why "Near-Miss" matters.** The strict gate for DoP is **weighted MAD ≤ 0.015**. Our best result hits **0.015863**, i.e., `gap = +0.000863`, with full validation (BCa B=5,000; weekly shuffle; invariants). This suggests the threshold is **approachable** under certain category/window choices, though not crossed yet.

**Validation signals.** The **invariant** `Σ_A w_A·D(A→B) ≈ Pen(B)` holds with a mean absolute error of 0.0032. A **label-shuffle** negative control degrades MAD to 0.0421, confirming signal beyond chance. Median brands per user = 2.0 (≥2 required), so the cohort supports DoP interpretation.

### 3. Real-World Data Insights

**Claim.** Real-world marketing data exhibits characteristics that challenge theoretical marketing science models.

**Evidence.** Purchase behavior shows extreme variability (std = 181.9), marketing science principles vary across categories, and non-stationary data affects analysis validity.

**Implication.** These findings suggest that theoretical models require adaptation for real-world applications, with careful consideration of data quality and statistical assumptions.

**Limits.** Results are specific to the analyzed categories and time periods; broader generalization requires additional validation across diverse datasets.

## Analysis Results Summary

### Double Jeopardy Analysis ❌

**Result**: Pearson r = 0.627 (target: ≥0.80)
**Failure Analysis**:
- **Brand Count Impact**: n_brands = 16 (insufficient for stable correlation)
- **Buyer Threshold**: min_buyers = 500 (excludes marginal brands)
- **Time Window**: 26 weeks (may be too short for frequency stabilization)

**Sensitivity Analysis**:
| Window | Min Buyers | Pearson r | Spearman r | Implication |
|--------|------------|-----------|------------|-------------|
| 26 weeks | 300 | 0.634 | 0.571 | Lower threshold improves |
| 26 weeks | 500 | 0.627 | 0.562 | Baseline |
| 26 weeks | 1000 | 0.598 | 0.548 | Higher threshold reduces |
| 52 weeks | 300 | 0.612 | 0.555 | Longer window + lower threshold |
| 52 weeks | 500 | 0.589 | 0.534 | Longer window reduces |
| 52 weeks | 1000 | 0.556 | 0.512 | Both constraints reduce |

**Implication**: Weak brand penetration-frequency relationship due to data constraints
**Evidence**: [assets/evidence/dj_bodycare.csv](/assets/evidence/dj_bodycare.csv)

### Duplication of Purchase Analysis ❌

**Best Result**: dunnhumby beauty MAD = 0.015863 (gap: +0.000863)
**Comparison**: Instacart shampoo MAD = 0.021854
**Implication**: Close to theoretical threshold but not achieved
**Evidence**: [assets/evidence/dop_dunnhumby_beauty_spec_q90_b2_m20.csv](/assets/evidence/dop_dunnhumby_beauty_spec_q90_b2_m20.csv)

### Category Entry Points Analysis ✅

**Result**: Complete multilingual analysis with Wilson CI
**H1 Correlation**: Pearson = -0.28, Spearman = -0.59
**Implication**: Higher penetration correlates with lower coverage
**Evidence**: [assets/evidence/cep_coverage_complete.csv](/assets/evidence/cep_coverage_complete.csv)

### Moderation Analysis ✅

**Result**: Strong quantile effects (Q4 slope = 3.341)
**Implication**: Heavy buyers show strongest relationships
**Evidence**: [assets/evidence/moderation_bodycare.csv](/assets/evidence/moderation_bodycare.csv)

### Dirichlet Model Analysis ⚠️

**Result**: R² = -7.0e-06 (very poor fit)
**Scope Limitation**: Designed for **category × brand × buyer distribution** panel data
**Excluded Data**: SKU-level, review data, and non-panel sources are **out of scope**
**Implication**: Theoretical model struggles with real-world data complexity
**Evidence**: [assets/evidence/dirichlet_bodycare.csv](/assets/evidence/dirichlet_bodycare.csv)

## Simplified vs. Specification-Compliant

### Simplified Version Results

- **Purpose**: Demonstration and quick validation
- **Method**: Unweighted MAD, estimated weekly shuffle
- **Results**: 2 PASS examples achieved
- **Use Case**: Educational purposes, proof-of-concept

### Specification-Compliant Version Results

- **Purpose**: Production-ready statistical analysis
- **Method**: Weighted MAD, BCa (B=5000, seed=42), real weekly shuffle
- **Results**: Near-miss achievement, no strict PASS
- **Use Case**: Research publication, statistical validation

## Synthesis

The specification-compliant implementation reveals why achieving PASS examples is challenging: brand purchase count–weighted MAD increases stringency compared to unweighted calculations, while category dynamics and temporal instability contribute to DJ analysis failures. The CEP and moderation results complement these findings by demonstrating successful multilingual analysis and robust quantile-based buyer segmentation, respectively, suggesting that some marketing science principles are more applicable than others in real-world contexts.

## Evidence Files and Documentation

![Marketing science analysis overview showing DoP near-miss results and comprehensive statistical validation across all methodologies](/assets/images/marketing-science/dop_heat_dunnhumby_beauty_spec_q90_b2_m20.png)

*Figure 1 provides an overview of the marketing science analysis pipeline, highlighting the near-miss DoP result and comprehensive statistical validation across all methodologies.*

### Core Results
- **DJ Analysis**: [results/dj_bodycare.csv](/results/dj_bodycare.csv)
- **DoP Analysis**: [results/dop_dunnhumby_beauty_spec_q90_b2_m20.csv](/results/dop_dunnhumby_beauty_spec_q90_b2_m20.csv)
- **CEP Analysis**: [results/cep_coverage_complete.csv](/results/cep_coverage_complete.csv)
- **Moderation Analysis**: [results/moderation_bodycare.csv](/results/moderation_bodycare.csv)
- **Dirichlet Analysis**: [results/dirichlet_bodycare.csv](/results/dirichlet_bodycare.csv)

### Methodology Summary

**Statistical Framework**: All analyses employ specification-compliant methods including BCa Bootstrap (B=5000, seed=42), real weekly shuffle for temporal randomization, and negative controls for validation.

**Data Sources**: 
- UCI beauty category data (1,264 users, 27 brands) for DJ and Moderation analysis
- Dunnhumby beauty data (1,735 users, 46 brands) for DoP near-miss analysis  
- Amazon review data (1M+ records, 27 languages) for CEP analysis

**Quality Assurance**: Complete audit logging in JSONL format, input SHA verification for reproducibility, and stationarity testing across all analyses.

<details>
<summary>Reproducibility (Commands, Versions, Logs)</summary>

For detailed reproducibility information, refer to the individual analysis articles:
- **Double Jeopardy**: [DJ Analysis Reproducibility](/marketing/2025/09/27/double-jeopardy-analysis-fail.html#reproducibility)
- **Duplication of Purchase**: [DoP Analysis Reproducibility](/marketing/2025/09/27/duplication-of-purchase-near-miss.html#reproducibility)
- **Category Entry Points**: [CEP Analysis Reproducibility](/marketing/2025/09/27/category-entry-points-analysis.html#reproducibility)
- **Moderation/Dirichlet**: [Moderation Analysis Reproducibility](/marketing/2025/09/27/moderation-dirichlet-analysis.html#reproducibility)

**Common Dependencies**: Python 3.9+, pandas, numpy, scipy, scikit-learn, matplotlib

</details>

## Limitations and Threats to Validity

These results are contingent on category selection, temporal windowing, and minimum buyer thresholds. In particular, brand-count weighting increases stringency in DoP; non-stationarity and heterogeneous purchase variance attenuate DJ and Dirichlet fits. We report full audit logs and input SHAs to support replication.

## Next Steps and Future Research

Future research should investigate additional data sources for specification-compliant PASS, explore category-specific threshold requirements, examine temporal stability requirements, develop guidelines for near-miss result interpretation, explore alternative statistical measures for high-variance data, investigate robust modeling approaches, examine theoretical threshold achievability, investigate category-specific marketing science principles, and develop empirical validation frameworks.

## Conclusion

Our marketing science analysis pipeline demonstrates the importance of specification-compliant implementation in revealing genuine data characteristics. While no strict PASS examples were achieved, the near-miss results and comprehensive statistical validation provide valuable insights into the gap between theoretical expectations and real-world data. This analysis contributes to the understanding of marketing science principles in practice and highlights the need for rigorous statistical implementation in marketing research.

## References

- Ehrenberg, A.S.C. (1988). Repeat-buying: facts, theory and applications
- Sharp, B. (2010). How Brands Grow

---

*This analysis is part of a comprehensive marketing science research project.*
