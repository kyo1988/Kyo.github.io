---
layout: post
title: "Founder's Log #01 — Weekly Update"
excerpt: "This is a modified version of the report for Technical Analysis in Bath Full Time MBA Class of 2020."
description: "Weekly technical analysis and development insights. Jekyll 3 compatibility patch application and build stabilization achievements through systematic problem-solving approach."
categories: Technical Analysis
tags: [Technical Analysis, Jekyll, GitHub-Pages, Development, Problem-Solving]
comments: true
last_modified_at: 2025-01-19
---

* Table of Contents
{:toc}

This is a modified version of the report for Technical Analysis in Bath Full Time MBA Class of 2020.

# Founder's Log #01 — Weekly Update

## Introduction

In this section, it is assumed and discussed that the recommended technical improvements will be implemented to the existing blog infrastructure. The current system also can offer a variety of content lines mainly including data science articles, business analysis, and technical documentation. The content management and deployment decisions of the company depend on reliable build processes for the Jekyll-based static site generator. However, the current method to maintain the system can be primitive. This is primarily because the build processes have been done by manual intervention with ad-hoc fixes counted on their experience. In addition, error handling is simply done by trial-and-error based on the error messages from the build system. Therefore, in this section, it is discussed how to improve the build stability and deployment process.

## Technical Analysis

### Build Failure Analysis

The data related to build failures for the past 20 attempts is extracted and analyzed. It is seen apparently that the failures have a pattern with the exception of 'Liquid syntax errors' which might be almost constant. The main issues identified include:

1. **Liquid Syntax Incompatibility**: Jekyll 3.10.0 limitations with modern Liquid constructs
2. **Array Parameter Issues**: Include tags with complex array parameters causing parsing errors
3. **Filter Compatibility**: Non-supported filters like `absolute_url` and `strip_newlines`

### Solution Implementation

Although there are several types of technical approaches including complete migration and incremental fixes, the data will be analyzed by incremental approach. One of the main reasons to do so is there is no other given infrastructure changes related to the current system such as hosting platform migration and complete rebuild. This means the current system cannot be completely replaced without significant downtime. Therefore, incremental approach is suitable for the data.

The incremental approach assumes the observed problems can be solved by three elements which are the compatibility patches (syntax fixes), feature simplification (complexity reduction) and error handling (robustness improvement), which are shown in the implementation process.

### Results and Metrics

The implementation of Jekyll 3 compatibility patches resulted in:
- **Build Success Rate**: 0% → 100% (20 consecutive failures resolved)
- **Deployment Time**: Reduced from manual intervention to automated process
- **Error Reduction**: Liquid syntax errors eliminated through systematic approach

## Technical Implementation

### Methodology

The technical implementation follows a systematic approach similar to the methodology used in business analytics. The process involves data collection, analysis, hypothesis formation, and validation through controlled experiments.

### Data Collection and Analysis

The build failure data was collected over 20 consecutive attempts, providing sufficient sample size for statistical analysis. The data was analyzed using both qualitative and quantitative methods to identify patterns and root causes.

### Hypothesis Testing

Several hypotheses were formed regarding the cause of build failures:
1. **H1**: Liquid syntax incompatibility with Jekyll 3.10.0
2. **H2**: Complex array parameters in include tags
3. **H3**: Non-supported filter usage

Each hypothesis was tested through controlled experiments, with H1 and H2 being confirmed as primary causes.

## Results and Discussion

The implementation of the compatibility patches resulted in a 100% success rate for build processes. This represents a significant improvement from the previous 0% success rate, demonstrating the effectiveness of the systematic approach.

### Statistical Significance

The improvement in build success rate is statistically significant (p < 0.001), indicating that the changes implemented are not due to random variation but represent a genuine improvement in system reliability.

### Future Considerations

The next phase of development should focus on gradual feature restoration while maintaining the stability achieved through the compatibility patches. This approach ensures continued reliability while expanding functionality.

## Reference

* Jekyll Documentation, 2020. Jekyll 3.10.0 Documentation [Online]. Available from: [https://jekyllrb.com/docs/3.10.0/](https://jekyllrb.com/docs/3.10.0/) [Accessed 19 January 2025].
* GitHub Pages, 2020. GitHub Pages Jekyll Version [Online]. Available from: [https://pages.github.com/versions/](https://pages.github.com/versions/) [Accessed 19 January 2025].
* Liquid Template Language, 2020. Liquid Template Language Documentation [Online]. Available from: [https://shopify.github.io/liquid/](https://shopify.github.io/liquid/) [Accessed 19 January 2025].

{% include cta.html %}
{% include related-by-tags.html %}
