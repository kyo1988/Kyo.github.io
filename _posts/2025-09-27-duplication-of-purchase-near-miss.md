---
layout: post
title: "Duplication of Purchase Analysis: Near-Miss Achievement and the Weighted MAD Challenge"
date: 2025-09-27 11:00:00 +0900
categories: [Marketing Science, Data Analysis]
tags: [Duplication of Purchase, Ehrenberg-Bass, Marketing Analytics, Statistical Analysis, Weighted MAD]
permalink: /marketing/2025/09/27/duplication-of-purchase-near-miss.html
---

# Duplication of Purchase Analysis: Near-Miss Achievement and the Weighted MAD Challenge

## Executive Summary

Our specification-compliant Duplication of Purchase (DoP) analysis achieved a near-miss result with dunnhumby beauty data (weighted MAD = 0.015863, gap: +0.000863 from 0.015 threshold). This analysis reveals the critical importance of weighted MAD calculations and the challenges of meeting theoretical thresholds with real-world data. While simplified versions achieve PASS examples, specification-compliant analysis demonstrates the rigor required for production research.

## Background

Duplication of Purchase (DoP) measures the extent to which buyers of one brand also purchase other brands in the same category. The Ehrenberg–Bass framework suggests that brand duplication should follow predictable patterns, with MAD (Mean Absolute Deviation) values typically below 0.015 for well-behaved categories.

## Methodology

### Specification-Compliant Analysis

Our analysis employed rigorous statistical methods:

- **Weighted MAD**: Brand purchase count weighting (not simple averaging)
- **BCa Bootstrap**: BCa (B=5000, seed=42)
- **Weekly Shuffle Test**: Real temporal randomization
- **Negative Control**: Threshold ≤0.05
- **Minimum Requirements**: ≥10 brands, median brands per user ≥2.0

### Data Sources

1. **Dunnhumby Beauty** (Best Result)
2. **Instacart Shampoo** (Comparison)
3. **Multiple Filtering Strategies**: Top user quantiles, minimum brand counts, buyer thresholds

## Results

### Specification-Compliant Results

#### Dunnhumby Beauty (Best Near-Miss)

| Metric | Target | Actual | Status |
|--------|--------|--------|--------|
| Weighted MAD | ≤0.015 | 0.015863 | ❌ NEAR-MISS (+0.000863) |
| BCa CI | 95% | [0.014792, 0.016928] | ✅ |
| Weekly Shuffle | ≥0.95 | 1.000 | ✅ |
| Median Brands | ≥2.0 | 2.0 | ✅ |
| Negative Control | ≤0.05 | 0.015629 | ✅ |
| Users | ≥1000 | 1,735 | ✅ |
| Brands | ≥10 | 46 | ✅ |

#### Instacart Shampoo (Comparison)

| Metric | Target | Actual | Status |
|--------|--------|--------|--------|
| Weighted MAD | ≤0.015 | 0.021854 | ❌ FAIL |
| BCa CI | 95% | [0.019350, 0.024683] | ✅ |
| Weekly Shuffle | ≥0.95 | 1.000 | ✅ |
| Median Brands | ≥2.0 | 2.0 | ✅ |
| Negative Control | ≤0.05 | 0.0187 | ✅ |
| Users | ≥1000 | 1,617 | ✅ |
| Brands | ≥10 | 129 | ✅ |

### Simplified Version Results (Demonstration)

The simplified version demonstrates pedagogical value by achieving PASS examples using unweighted MAD calculations. This approach serves educational purposes and proof-of-concept validation, contrasting with production-ready specification-compliant analysis that employs brand purchase count–weighted MAD for statistical rigor.

- **Instacart Shampoo (Top 15%)**: Unweighted MAD = 0.011934 ✅ PASS
- **CEP-Stratified Demo**: Unweighted MAD = 0.0108 ✅ PASS

## Discussion

The critical difference between simplified and specification-compliant analysis lies in MAD calculation methodology. Simplified versions use simple averaging of brand pair duplications, while specification-compliant analysis employs brand purchase count–weighted MAD for statistical rigor. This weighting makes the specification-compliant analysis more stringent and reflective of actual market dynamics.

## Key Insights

### 1. Weighted vs. Unweighted MAD

The critical difference between simplified and specification-compliant analysis lies in MAD calculation:

- **Simplified**: Simple average of brand pair duplications
- **Specification-Compliant**: Brand purchase count–weighted MAD

This weighting makes the specification-compliant analysis more stringent and reflective of actual market dynamics.

### 2. Near-Miss Achievement

The dunnhumby beauty result (0.015863) represents the closest achievement to specification-compliant PASS, with a gap of only +0.000863 from the 0.015 threshold. This suggests:

- The theoretical threshold may be achievable with optimal data conditions
- Real-world data often falls just short of theoretical expectations
- Statistical rigor reveals genuine data characteristics

### 3. Statistical Validation

All supporting metrics meet specification requirements:

- **Weekly Shuffle**: 1.000 (real temporal randomization)
- **Median Brands per User**: 2.0 (adequate brand diversity)
- **Negative Control**: ≤0.05 (proper statistical validation)
- **BCa Confidence Intervals**: Robust statistical inference

## Experimental Grid

Our analysis tested 14 different filter combinations:

1. **User Quantiles**: 0.6, 0.7, 0.8, 0.9, 0.95
2. **Minimum Brand Counts per User**: 2, 3 (baseline 1 in some datasets)
3. **Minimum Buyers**: 5, 10, 20, 30 (baseline values for different datasets)
4. **Time Windows**: 13, 26 weeks
5. **Category Filters**: Various beauty subcategories

The dunnhumby beauty result emerged from the optimal combination: top 10% users, 2+ brands per user, minimum 20 buyers, 26-week window.

## Evidence Files

![Figure 1. DoP heatmap for dunnhumby beauty; warmer cells indicate higher duplication.](/assets/images/marketing-science/dop_heat_dunnhumby_beauty_spec_q90_b2_m20.png)

*Figure 1 displays the duplication matrix for dunnhumby beauty data, showing the near-miss result (MAD=0.015863) that approaches the 0.015 threshold.*

### Specification-Compliant Results
- **Best Near-Miss**: [results/dop_dunnhumby_beauty_spec_q90_b2_m20.csv](https://github.com/kyo1988/marketing-science/blob/main/results/dop_dunnhumby_beauty_spec_q90_b2_m20.csv)
- **Comparison**: [results/dop_instacart_shampoo_specification_compliant.csv](https://github.com/kyo1988/marketing-science/blob/main/results/dop_instacart_shampoo_specification_compliant.csv)
- **Heatmap**: [figs/dop_heat_dunnhumby_beauty_spec_q90_b2_m20.png](https://github.com/kyo1988/marketing-science/blob/main/figs/dop_heat_dunnhumby_beauty_spec_q90_b2_m20.png)
- **Audit Log**: [logs/run_dop_dunnhumby_beauty_spec_q90_b2_m20.jsonl](https://github.com/kyo1988/marketing-science/blob/main/logs/run_dop_dunnhumby_beauty_spec_q90_b2_m20.jsonl)

### Simplified Version Results
- **Instacart PASS**: [results/dop_instacart_shampoo_top15_pass.csv](https://github.com/kyo1988/marketing-science/blob/main/results/dop_instacart_shampoo_top15_pass.csv)
- **CEP Demo**: [results/dop_by_cep_realistic.csv](https://github.com/kyo1988/marketing-science/blob/main/results/dop_by_cep_realistic.csv)

## Reproducibility

**Command (repo)**: `poetry run python scripts/eb/compute_dop_specification_compliant.py --tx data/processed/tx_dunnhumby_beauty.csv --category_regex beauty --min_buyers 20 --top_user_quantile 0.9 --min_brand_count_per_user 2 --window_weeks 26 --bca 5000 --seed 42`

## Current Status

**Specification-Compliant Analysis**: ❌ NEAR-MISS - Best result 0.015863 (gap: +0.000863)
**Simplified Version**: ✅ PASS examples available (unweighted MAD basis)
**Statistical Validation**: ✅ Complete with BCa (B=5000, seed=42), real weekly shuffle, negative controls

## Key Takeaways

1. **Weighted MAD Matters**: Specification-compliant analysis requires brand purchase count weighting
2. **Near-Miss Achievement**: Real-world data can approach theoretical thresholds
3. **Statistical Rigor**: Proper implementation reveals genuine data characteristics
4. **Version Distinction**: Simplified vs. specification-compliant analysis serve different purposes

## Implications for Marketing Science

This analysis demonstrates that:

- Theoretical thresholds may be achievable but require optimal conditions
- Weighted MAD provides more realistic market dynamics assessment
- Statistical rigor is essential for production research
- Near-miss results provide valuable insights into data characteristics

## Limitations and Threats to Validity

These results are contingent on category selection, temporal windowing, and minimum buyer thresholds. In particular, brand-count weighting increases stringency in DoP; non-stationarity and heterogeneous purchase variance attenuate DJ and Dirichlet fits. We report full audit logs and input SHAs to support replication.

## Next Steps

Future research should investigate additional data sources for specification-compliant PASS, explore alternative MAD calculation methods, examine category-specific threshold requirements, and develop guidelines for near-miss result interpretation.

## References

- Ehrenberg, A.S.C. (1988). Repeat-buying: facts, theory and applications
- Sharp, B. (2010). How Brands Grow
- [Project Documentation](https://github.com/kyo1988/marketing-science/blob/main/README.md)
- [Specification-Compliant Analysis Report](https://github.com/kyo1988/marketing-science/blob/main/notes/specification_compliant_pass_analysis.md)

---

*This analysis is part of a comprehensive marketing science research project. For complete methodology and results, see the [Statement of Work](https://github.com/kyo1988/marketing-science/blob/main/SOW.md) and [Progress Summary](https://github.com/kyo1988/marketing-science/blob/main/notes/progress_summary.md).*
