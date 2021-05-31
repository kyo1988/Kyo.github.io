---
layout: post
title: Derivation of yield curve construction formula with tenor basis spread 
excerpt: "This is a modified version of the report for semminar at a financial consulting firm in 2016."
categories: Business Finance
tags: [ Business Finance]
comments: true
---

* Table of Contents
{:toc}

# Derivation of yield curve construction formula with tenor basis spread
 
If LIBOR is truly risk-free, the swap of 3-month LIBOR and 6-month LIBOR should be tradable with zero spread. However, LIBOR takes into account the credit risk of banks, and tenor swaps are exactly the transactions that swap the risk of 3-month LIBOR and 6-month LIBOR. After the financial crisis, the risk of bankruptcy, that is, the difference in tenor, was conscious, and when swap 3-month LIBOR and 6-month LIBOR, the 3-month LIBOR side began to trade with a non-negligible spread.
 
After all, after supplementing the discount factor and tenor spread in 0.25 year increments, the future 3-month LIBOR can be calculated as follows (Nakahara, 2013).
 
\begin{eqnarray}\label{3MonthLibor1}
L^{3MWorld}_{forward}(t,t_{i},t_{i+0.25})=\frac{1-DF(t,t_{i+0.25})-TS^{3M-6M}(t,t_{i+0.25})\times\sum_{j=1}^{4i+1}{DF(t,t_{\frac{j}{4}})\times\frac{1}{4}}}{DF(t,t_{i+0.25})\times\frac{1}{4}}+\frac{-\sum_{j=1}^{4i}{L^{3MWorld}_{forward}(t,t_{\frac{j-1}{4}},t_{\frac{j}{4}})\times DF(t,t_{\frac{j}{4}})\times\frac{1}{4}}}{DF(t,t_{i+0.25})\times\frac{1}{4}}．
\end{eqnarray}
 
However,
 
* $L(t,T)$: Observable LIBOR at time point $t$ maturity $T$
* $L^{3MWorld}_{forward}(t,t_{0},t_{0.25})=L(t,t_{0.25})$
* $L^{3MWorld}_{forward}(t,t_{i},t_{i+0.25})$: A 3-month LIBOR with a reset date of $t_{i}$ and a maturity of $t_{i+0.25}$ as seen from the point in time $t$
* $TS^{3M-6M}(t,T)$: Tenor spread when swapping 6-month LIBOR for 3-month LIBOR at time $t$ and maturity $T$
 
In this article, we try to derive the equation \label{3MonthLibor}. 
At this time, the evaluation formula of the JPY tenor swap is expressed as follows (Takahashi, 2010)．
 
\begin{eqnarray}\label{tenor}
\sum_{n=1}^{N}\delta_{n}(E_{t}[L(T_{n-1},T_{n}+\tau_{N}]P_{t,T_{n}})=\sum_{m=1}^{M}\delta_{m}E_{t}[L(T_{m-1},T_{m}]P_{t,T_{m}}．
\end{eqnarray}
 
However,
 
* $N=2M$
* $L(T_{n-1},T_{n})$: LIBOR with a reset date of $T_{n-1}$ and a maturity of $T_{n}$
* $P_{t,T_{n}}$: Zero coupon bond price with maturity of $t$ at time $ T_{n}$
* $\delta_{n}$: Interest calculation period
* $\tau_{N}$: Tenor spread when swapping 6-month LIBOR for 3-month LIBOR at time $t$ and maturity of $T (= T_{N} = T_{M})$
 
Now, we want to derive 3 months LIBOR, that is, $E_{t}[L(T_{N-1}, T_{N}]$, therefore expand the left side of the expression (1) as follows.
 
\begin{eqnarray}
\sum_{n=1}^{N}\delta_{n}(E_{t}[L(T_{n-1},T_{n}+\tau_{N}]P_{t,T_{n}})=\sum_{n=1}^{N-1}\delta_{n}(E_{t}[L(T_{n-1},T_{n})]P_{t,T_{n}}+\delta_{N}E_{t}[L(T_{N-1},T_{N})]P_{t,T_{N}}+\sum_{n=1}^{N}\delta_{n}\tau_{N}P_{t,T_{n}}．
\end{eqnarray}

On the other hand, the relationship between Libor and the discount rate is
 
\begin{eqnarray}
E_{t}[L(T_{m-1},T_{m})]=\frac{1}{\delta_{n}}\left(\frac{P_{t,T_{m-1}}}{P_{t,T_{n}}}-1\right)．
\end{eqnarray}
 
Since it is represented by, the left side of the expression \label{tenor} can be expanded as follows.
 
\begin{eqnarray}
\sum_{m=1}^{M}\delta_{m}E_{t}[L(T_{m-1},T_{m}]P_{t,T_{m}}&=&P_{t,T_{0}}-P_{t,T_{M}} \nonumber\\
&=&1-P_{t,T_{M}}．
\end{eqnarray}
 
After all, JPY 3 months LIBOR, ie $E_{t} [L(T_{N-1},T_{N}]$, is given below.
 
\begin{eqnarray}\label{3MonthLibor2}
E_{t}[L(T_{N-1},T_{N}]&=&\frac{1-P_{t,T_{M}}-\sum_{n=1}^{N}\delta_{n}\tau_{N}P_{t,T_{n}}}{\delta_{N}P_{t,T_{N}}} \nonumber\\
&+&\frac{-\sum_{n=1}^{N-1}\delta_{n}(E_{t}[L(T_{n-1},T_{n})]P_{t,T_{n}}}{\delta_{N}P_{t,T_{N}}}．
\end{eqnarray}

## Reference
* Nakahara, G.，2013. LIBOR and OIS discount that can be seen in EXCEL (In Japanese)
* Fujii, M.，Shimada, Y. and Takahashi, A.，2010. "A Note on Construction of Multiple Swap Curves with and without Collateral"， FSA Research Review Vol.6(March 2010)．