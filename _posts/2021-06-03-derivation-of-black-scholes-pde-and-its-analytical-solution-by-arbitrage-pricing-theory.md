---
layout: post
title: Derivation of Black-Scholes PDE and its analytical solution by arbitrage pricing theory
excerpt: "This is a modified version of the report for semminar at a financial consulting firm in 2016."
categories: Business Finance
tags: [ Business Finance]
comments: true
---

* Table of Contents
{:toc}

# Derivation of Black-Scholes PDE and its analytical solution by arbitrage pricing theory
 
In general, when the underlying asset price is given by a stochastic differential equation, the price of the derivative product is given by a partial differential equation. In this paper, it will be derived from the Black-Scholes PDE corresponding to the derivative (here, option) price valuation of the underlying asset (here, stock) modeled as the geometric Brownian motion. The valuation of an option is given by determining the initial funding needed to fully hedge the selling position of the option. Since the determined initial fund is the amount required to build a duplicate portfolio, it is called the no arbitrage price at time zero of the option. The price valuation method that duplicates options in stock market and money market account transactions is called arbitrage pricing theory (APT).
 
Suppose it is given a portfolio valued at $X(t)$ at any time $t$. Here, the composition of the given portfolio is as follows.
 
\begin{enumerate}
\item money-market account with interest rate $r$
\item A stock modeled by the geometric Brownian motion expressed by the following equation
\end{enumerate}
 
\begin{eqnarray}\label{stockPrice}
dS(t)=\alpha S(t)dt+\sigma S(t)dW(t)．
\end{eqnarray}
 
Here, it is assumed that the investor who holds the given portfolio holds the stock in the unit of $\Delta(t)$ at any time $t$. At this time, it is assumed that the number of shares held $\Delta(t)$ is an ‘adapted stochastic process’. The remainder of the portfolio excluding the investment in stocks, $X(t)-\Delta(t)S(t)$, is invested in the money market account.
Here, the small change $dX(t)$ of the portfolio value $X(t)$ at any time $t$ results in the following two factors.
 
* Profit from holding shares $\Delta(t)dS(t)$
*  Profit from holding cash $r\left(X(t)-\Delta(t)S(t)\right)dt$
 
That is, the small change in portfolio value $dX(t)$ is given by the following equation.
 
\begin{eqnarray}\label{portDiff}
dX(t)=\Delta(t)dS(t)+r\left(X(t)-\Delta(t)S(t)\right)dt．
\end{eqnarray}
 
The equation \eqref{portDiff} is expanded as follows from the stochastic differential equation \eqref{stockPrice} of a given stock price.
\begin{eqnarray}\label{portDiff2}
dX(t)&=&\Delta(t)dS(t)+r\left(X(t)-\Delta(t)S(t)\right)dt　\nonumber\\
&=&\Delta(t)\left( \alpha S(t)dt+\sigma S(t)dW(t) \right)+r\left(X(t)-\Delta(t)S(t)\right)dt\nonumber\\
&=&rX(t)dt+\Delta(t)\left( \alpha -r \right)S(t)dt+\Delta(t)\sigma S(t)dW(t)．
\end{eqnarray}
 
Here, the three terms appearing in the small change in portfolio value $dX(t)$\eqref{portDiff2} expanded by the given stock price of the stochastic differential equation \eqref{stockPrice} can be interpreted as follows.
 
* $rX(t)dt$: A term that reflects the profit from the expected rate of return of the portfolio $r$
* $\Delta(t)\left( \alpha -r \right)S(t)dt$: A term that reflects the risk premium on equity investments $\alpha-r$
* $\Delta(t)\sigma S(t)dW(t)$: Volatility term proportional to the size of equity investment
 
Then, consider the discounted stock price $\mathrm{e}^{-rt} S(t)$ and the discounted portfolio value $\mathrm{e}^{-rt}X(t)$. In order to analyze these price processes, it should be noted that they are different from ordinary analysis due to the nature of the geometric Brownian motion that appeared as a model of stock prices. This property means that Brownian motion has a non-zero quadratic variation, which, as it will be seen later, is the source of the volatility term of the Black-Scholes PDE.
In other words, to differentiate an expression expressed in the form of $f \left(W(t) right)$ with $f(x)$ as a differentiable function and $W(t)$ as the Brown motion. If Brown motion $W(t)$ is differentiable, the following equation holds from ordinary analysis by the chain rule of the composite function.
 
\begin{eqnarray}
\frac{d}{dt}f(W(t))&=&f'(W(t))W'(t)\nonumber\\
\Leftrightarrow df(W(t))&=&f'(W(t))W'(t)dt\nonumber\\
&=&f'(W(t))dW(t)．\nonumber
\end{eqnarray}
 
However, since Brownian motion accumulates a quadratic variation of 1 per unit time, $(dWdW = dt)$, the derivative of $f \left(W(t)\right)$ has a correction term shown in the following equation.
 
\begin{eqnarray}\label{ItoFormDiff}
df(W(t))=f'(W(t))dW(t)+\frac{1}{2}f''(W(t))dt．
\end{eqnarray}
 
The formula \eqref{ItoFormDiff} is called Ito's formula in differential form. The equation \eqref{ItoFormDiff} is an equation obtained by differentiating Ito's formula \eqref{ItoForm} for the Brownian motion shown below.
 
\begin{theorem}[Ito's formula for Brownian motion]
Partial differentiation of $ f(t, x) $f_ {t}(t, x), f_{x}(t, x), f_ {xx}(t, x)$ is defined and continuous. Let $W(t)$ be the Brownian motion. At this time, the following equation holds for all $T \geq0$.
 
\begin{eqnarray}\label{ItoForm}
f\left(T，W(T)\right)=f\left(0，W(0)\right)&+&\int^{T}_{0}f_{t}\left(t，W(t)\right)dt\nonumber\\
&+&\int^{T}_{0}f_{x}\left(t，W(t)\right)dW(t)+\frac{1}{2}\int^{T}_{0}f_{xx}\left(t，W(t)\right)dt．
\end{eqnarray}
\end{theorem}
 
Where the third term of the expression \eqref{ItoForm} $\int^{T}_{0}f_{x}\left(t, W(t) \right) dW(t)$ is called Ito integral, and the second and fourth terms are Lebesgue integrals for variables of time. Ito's formula can be extended to general stochastic processes including the Brown process, excluding jump process. This stochastic process is called the Ito process $dX(t)=a(t)dW(t)+b(t)dt$, and $a^{2}(t) per unit time, which accumulate the quadratic variation of $. It is assumed that $a(t) and b(t)$ are adapted stochastic  processes.
 
\begin{theorem}[Ito's formula for the Ito process]
Let $X(t)$ be the Ito process, and $f(t, x)$ be the partial derivative $f_{t}(t, x), f_{x}(t, x), f_{xx}(Let t, x)$ be a defined and continuous function, and let $W(t)$ be Brownian motion. At this time, the following equation holds for all $T \geq 0$.
 
\begin{eqnarray}\label{ItoFormII}
f\left(T，X(T)\right)=f\left(0，X(0)\right)&+&\int^{T}_{0}f_{t}\left(t，X(t)\right)dt\nonumber\\
&+&\int^{T}_{0}f_{x}\left(t，X(t)\right)dX(t)+\frac{1}{2}\int^{T}_{0}f_{xx}\left(t，X(t)\right)a^{2}(t)dt．
\end{eqnarray}
\end{theorem}
 
Therefore, the derivative of the discounted stock price $\mathrm{e}^{-rt} S(t)$ is $f(t, x) = \mathrm{e}^{-rt} x$ which is gotten to apply Ito's formula \eqref{ItoForm}. In the following, it is used that $f_{t} \left(t, x \right)=-r \mathrm{e}^{-rt} x$, $ f_{x} \left (t, x \right)=\, mathrm{e}^{-rt}$, $f_{xx} \left(t, x \right)=0 $.
 
\begin{eqnarray}\label{DiscountStockPrice}
d\left( \mathrm{e}^{-rt}S(t) \right)&=&df\left(t，S(t)\right) \nonumber\\
&=&f_{t}\left(t，S(t)\right)dt+f_{x}\left(t，S(t)\right)dS(t)+f_{xx}\left(t，S(t)\right)dt\nonumber\\
&=&-r\mathrm{e}^{-rt}S(t)dt+\mathrm{e}^{-rt}dS(t) \nonumber\\
&=&-r\mathrm{e}^{-rt}S(t)dt+\mathrm{e}^{-rt}\left( \alpha S(t)dt+\sigma S(t)dW(t) \right) \nonumber\\
&=&\left(\alpha-r\right)\mathrm{e}^{-rt}S(t)dt+\sigma\mathrm{e}^{-rt}S(t)dW(t)
\end{eqnarray}
 
Similarly, the derivative of the discounted portfolio value $\mathrm{e}^{-rt} X(t)$ is given by
 
\begin{eqnarray}\label{DiscountPort}
d\left( \mathrm{e}^{-rt}X(t) \right)&=&df\left(t，X(t)\right) \nonumber\\
&=&f_{t}\left(t，X(t)\right)dt+f_{x}\left(t，X(t)\right)dX(t)+\frac{1}{2}f_{xx}\left(t，X(t)\right)dt\nonumber\\
&=&-r\mathrm{e}^{-rt}X(t)dt+\mathrm{e}^{-rt}dX(t) \nonumber\\
&=&-r\mathrm{e}^{-rt}X(t)dt+\mathrm{e}^{-rt}\left( \Delta(t)dS(t)+r\left(X(t)-\Delta(t)S(t)\right)dt \right) \nonumber\\
&=&\Delta(t)\left(\alpha-r\right)\mathrm{e}^{-rt}S(t)dt+\Delta(t)\sigma\mathrm{e}^{-rt}S(t)dW(t)\nonumber\\
&=&\Delta(t)d\left( \mathrm{e}^{-rt}S(t) \right)．
\end{eqnarray}
 
In this way, the formula \eqref{DiscountPort} is obtained by the discounted stock price $S(t)$ and the portfolio value $X(t)$ at the discount rate $\mathrm{e}^{-rt}$ with the interest rate $r $ of the money market account. The formula \eqref {DiscountPort} indicates that small change in the discount portfolio value $d\left (\mathrm{e}^{-rt} X(t) \right) depends only on a small change in the discounted stock price $d\left(\mathrm{e}^{-rt} S(t) \right)$.
 
Consider a European call option where the payment on the maturity date $T$ is $\left(S(T)-K \right)^{+}$. Here, the strike price $K$ is assumed to be a non-negative constant.
Fischer Black, Myron Scholes and Robert Cox Merton argued that the value of European call option on maturity $T$ with payment $\left(S(T) -K \right)^{+}$ at any time $t$ depends on the length of time to maturity, the value of the stock price $S(t)$ at time $t$, the model parameters $r, \sigma$ and the strike price $K$.

Since the model parameters $r, \sigma$ and the strike price $K$ are assumed to be constants, among the variables that affect the price evaluation of the European call option, only the time $t$ and the stock price $S(t)$ are  changed. 

Here, according to the inference of Fischer Black et al, let the value of the European call option be $c(t, x)$ when the stock price is $S(t) = x$ at time $t$. Since the stock price $S(t)$ follows the stochastic differential equation \eqref{stockPrice}, the value of the European call option is also stochastic.

Therefore, the value of the European call option is the stochastic process $c(t, S(t))$ obtained by replacing the stochastic process $S(t)$ with the parameter $x$. At the initial time, the future stock price $S(t)$ is unknown because it is probabilistic, then the value $c(t, S(t))$ of the future European call option is also unknown. Therefore, if the function $c(t, x)$ is determined, the value of the future European call option $c(t, S(t))$ is expressed by the future stock price $S(t)$.

To duplicate a portfolio which does full hedge the option sell position, it is required to fit the value of the duplicate portfolio $X(t)$ at any time $t\in[0, T]$ in the value of future European call options $c(t, S(t))$ starting with a certain initial fund of $X(0)$ and investing in the stock market and money market accounts.

The necessary and sufficient conditions for constructing this replication portfolio are $\ mathrm{e}^{-rt}X(t)=\mathrm{e}^{-rt} c(t, S (t))$ for any time $t \in[0, T]$. To show that the necessary and sufficient conditions are met,
 
\begin{eqnarray}\label{IsCopyPort}
d\left(\mathrm{e}^{-rt}X(t)\right)=d\left(\mathrm{e}^{-rt}c(t，S(t))\right)，t\in[0，T)
\end{eqnarray}
 
And show that $X(0) = c(0, S(0))$ holds. In fact, the following equation is obtained by integrating the equation \eqref{IsCopyPort} from 0 to $t$.
 
\begin{eqnarray}
\mathrm{e}^{-rt}X(t)-X(0)=\mathrm{e}^{-rt}c(t，S(t))-c(0，S(0))，t\in[0，T)
\end{eqnarray}
 
At this time, if $X(0) = c(0, S(0))$, then it is obtained the necessary and sufficient conditional expression $\mathrm{e}^{-rt} X(t) = \mathrm{e}^{-rt} c(t, S (t))$.

## Necessary and sufficient condition to duplicate the portfolio, which does fully hedge the option sell position 

To expand the right-hand side \eqref{IsCopyPort}, it is required to calculate the derivative of discount option price $\mathrm{e}^{-rt} c(t, S (t, S) t))$. To do this, it is needed to calculate the derivative of the option price $c(t, S(t))$. From Ito's formula for the Ito process \eqref{ItoFormII} and the given stock price stochastic differential equation \eqref{stockPrice}
 
\begin{eqnarray}
dc(t，S(t))&=&c_{t}\left(t，S(t)\right)dt+c_{x}\left(t，S(t)\right)dS(t)+\frac{1}{2}c_{xx}\left(t，S(t)\right)\left(\sigma S(t)\right)^{2}dt\nonumber\\
&=&c_{t}\left(t，S(t)\right)dt+c_{x}\left(t，S(t)\right)\left( \alpha S(t)dt+\sigma S(t)dW(t) \right)+\frac{1}{2}c_{xx}\left(t，S(t)\right)\left(\sigma S(t)\right)^{2}dt\nonumber\\
&=&\left( c_{t}\left(t，S(t)\right)dt+\alpha c_{x}\left(t，S(t)\right)+\frac{1}{2}\sigma^{2} S^{2}(t)c_{xx}\left(t，S(t)\right)\right)dt\nonumber\\
&+&\sigma S(t)c_{x}\left(t，S(t)\right)dW(t)．
\end{eqnarray}
 
It is calculated the derivative of discount option price $\mathrm{e}^{-rt} c (t)$ by Ito's formula \eqref{ItoFormII} for the Ito process as $f(t, x) =\mathrm{e}^{-rt} x, S(t))$. In the following, it is used that $f_{t} \left(t, x \right) = -r \mathrm{e}^{-rt}x$, $f_{x} \left(t, x \right) =\, \mathrm{e}^{-rt}$, $f_{xx} \left(t, x \right) = 0$.
 
\begin{eqnarray}\label{expandCallDis}
d\left(\mathrm{e}^{-rt}c(t，S(t))\right)&=&df\left(t，c(t，S(t))\right) \nonumber\\
&=&f_{t}\left(t，c(t，S(t))\right)dt+f_{x}\left(t，c(t，S(t))\right)dc(t，S(t))\nonumber\\
&+&\frac{1}{2}f_{xx}\left(t，c(t，S(t)\right) \left(\sigma S(t)c_{x}\left(t，S(t)\right)\right)^{2}dt\nonumber\\
&=&-r\mathrm{e}^{-rt}c(t，S(t))+\mathrm{e}^{-rt} dc(t，S(t))\nonumber\\
&=&\mathrm{e}^{-rt}\left( -rc(t，S(t))+c_{t}\left(t，S(t)\right)+\alpha c_{x}\left(t，S(t)\right)\right.\nonumber\\
&+&\left.\frac{1}{2}\sigma^{2} S^{2}(t)c_{xx}\left(t，S(t)\right)\right)dt+\mathrm{e}^{-rt}\sigma S(t)c_{x}\left(t，S(t)\right)dW(t)．
\end{eqnarray}
 
It is given the following equation to expand the right-hand side of \eqref{IsCopyPort} with the formula \eqref{expandCallDis} and the left-hand side with the formula \eqref{DiscountPort}.
 
\begin{eqnarray}\label{expandCopyPort}
&\Delta(t)\left(\alpha-r\right)S(t)dt+\Delta(t)\sigma S(t)dW(t)\nonumber\\
&=\left( -rc(t，S(t))+c_{t}\left(t，S(t)\right)+\alpha c_{x}\left(t，S(t)\right)+\frac{1}{2}\sigma^{2} S^{2}(t)c_{xx}\left(t，S(t)\right)\right)dt\nonumber\\
&+\sigma S(t)c_{x}\left(t，S(t)\right)dW(t)．
\end{eqnarray}
 
If the expansion formula \eqref{expandCopyPort}, which is a necessary and sufficient condition for replicating a portfolio that completely hedges an option's sell position, holds, the coefficients on both sides must be matched. Therefore, since the coefficients on both sides of $dW(t)$ are equal, the following equation is obtained.
 
\begin{eqnarray}\label{deltaHedging}
\Delta(t)=c_{x}\left(t，S(t)\right)，t\in[0，T)
\end{eqnarray}
 
The number of shares held to fully hedge the option's sell position at any time $t$ before maturity is the partial derivative of the option value at time $t$ with respect to the stock price $c_{x}\left(t, S(t)\right)$. The relational expression \eqref{deltaHedging} of $\Delta(t)$ is called the delta-hedging rule because it is called the optional delta.

Since the coefficients on both sides of $dt$ are also equal, the following equation holds for any time $t\in[0, T)$ from the relational expression \eqref{deltaHedging} of $\Delta(t)$.
 
\begin{eqnarray}\label{expandCopyPortForT}
&\left(\alpha-r\right)S(t)c_{x}\left(t，S(t)\right)\nonumber\\
&=-rc(t，S(t))+c_{t}\left(t，S(t)\right)+\alpha c_{x}\left(t，S(t)\right)+\frac{1}{2}\sigma^{2} S^{2}(t)c_{xx}\left(t，S(t)\right)
\end{eqnarray}
 
Since $\alpha c_{x} \left(t, S(t) \right)$ term appears on both sides of the expression \eqref{expandCopyPortForT} for any time $t\in[0, T)$, it is obtained the following equation to extract this term.
 
\begin{eqnarray}\label{PreBlackScholes}
rc(t，S(t))=c_{t}\left(t，S(t)\right)+rS(t)c_{x}\left(t，S(t)\right)+\frac{1}{2}\sigma^{2} S^{2}(t)c_{xx}\left(t，S(t)\right)
\end{eqnarray}
 
Here, if the value of the European call option when the stock price is $S(t) = x$ at time $t$ is $c(t, x)$, then it is obtained the partial differential equation of Black-Scholes from the equation \eqref{PreBlackScholes}.
 
\begin{eqnarray}\label{BlackScholes}
c_{t}\left(t，x\right)+rxc_{x}\left(t，x\right)\frac{1}{2}\sigma^{2} x^{2}c_{xx}\left(t，x\right)=rc(t，x)，t\in[0，T)，x\geq0
\end{eqnarray}
 
In addition to satisfying the equation \eqref{BlackScholes}, the function $c(t, x)$ must also satisfy the boundary conditions shown in the following equation.
 
\begin{eqnarray}\label{BoundaryCondtion}
c\left(T，x\right)=\left(x-K\right)^{+}，c\left(t，0\right)=0，\lim_{x \to \infty}\left[c\left(t，x\right)-\left( x-\mathrm{e}^{-r\left( T-t \right)}K \right)\right]=0
\end{eqnarray}
 
In fact, the first equation of the expression \eqref{BoundaryCondtion} follows from the definition of the European call option.

The second equation is that when $x = 0$ is substituted into the Black-Scholes partial differential equation \eqref{BlackScholes}, it is obtained the ordinary differential equation $c_{t} \left(t, 0 \right) = rc \left(t, 0 \right)$ for the function $c(t, 0)$ at time $t$ and then it is obtained its solution $c\left(t, 0 \right) = \mathrm{e}^{rt} is substituted $t = T$ for c \left(0, 0 \right)$, which results in $c \left (T, 0 \right) = \left(0-K \right)^{+} = 0$ , $C \left(0, 0 \right) = 0$. 

In the third equation, ‘Put/Call Parity’ holds because it is likely to end with ‘In the money’ for European call options for very large $x$ and the value of the forward contract is almost equal to $x-\mathrm{e}^{-r \left(Tt \right)}K$.

In order to obtain an analytical solution of the Black-Scholes PDE \eqref{BlackScholes}, it is reduced by change of variables to a PDE whose exact solution is known. Therefore, two variables $u and v$ are defined by the following equation, which are introduced for this purpose.
 
\begin{eqnarray}\label{val1}
u&=&\log \frac{x}{K}+\left(r-\frac{\sigma^{2}}{2}\right)\left(T-t\right) \nonumber\\
v&=&T-t
\end{eqnarray}
 
Here, using the variables $u and v$ defined in the expression \eqref{val1}, the function $c(t, x)$ is converted into two functions $\mathrm{e}^{-rv}$ and $y \left(u, v \right)$ as shown in the following expression. 
 
\begin{eqnarray}\label{val2}
c(t，x)=\mathrm{e}^{-rv}y\left(u，v\right)．
\end{eqnarray}
 
Substituting the equation \eqref{val2} into the partial differential equation \eqref{BlackScholes} of Black-Scholes and rearranging it gives the following equation.
 
\begin{eqnarray}\label{HeatConductionEquation}
y_{u u}\left(u，v\right)-\frac{2}{\sigma^{2}}y_{v}\left(u，v\right)=0．
\end{eqnarray}
 
The equation \eqref{HeatConductionEquation} is a known partial differential equation with an exact solution called the heat conduction equation. Here, the boundary condition is changed by variable transformation.
 
\begin{eqnarray}

c(t，x)=\left\{

\begin{array}{l}
x-K\cdots x\geq K\\
0\cdots x \lt K
\end{array}

\right.

\end{eqnarray}
 
Note that the following conditions have changed.
 
\begin{eqnarray}
y(u，0)=\left\{
\begin{array}{l}
K\left( \mathrm{e}^{u}-1 \right)\cdots u\geq 0\\
0\cdots u \lt 0
\end{array}
\right.
\end{eqnarray}
 
It is known that the heat conduction equation \eqref{HeatConductionEquation} is solved by the separation of variables method. The separation of variables method means that the solution $y \left(u, v \right)$ is expressed as the product of two functions $p(u) and q(v)$.
 
\begin{eqnarray}\label{val3}
y\left(u，v\right)=p(u)q(v)．
\end{eqnarray}
 
Substituting the equation \eqref{val3} into the heat conduction equation \eqref{HeatConductionEquation} and rearranging it gives the following equation.
 
\begin{eqnarray}\label{SeparationVariables}
\frac{p_{u u}(u)}{p(u)}=\frac{2}{\sigma^{2}}\frac{q_{v}(v)}{q(v)}．
\end{eqnarray}
 
Focusing on both sides of the obtained equation \eqref{SeparationVariables}, the left side is a function of only $u$ and the right side is a function of only $v$, then constants irrelevant to $u$ and $v$, which is $-k^{2} \left(0 \leq k \lt \infinity \right)$. Therefore, finding the solution of the heat conduction equation \eqref{HeatConductionEquation} results in the problem of solving the following two ordinary differential equations.
 
\begin{enumerate}
\item $\dfrac{p_{u u}(u)}{p(u)}=-k^{2}$
\item $\dfrac{2}{\sigma^{2}}\dfrac{q_{v}(v)}{q(v)}=-k^{2}$
\end{enumerate}
 
The first equation is a second-order ordinary differential equation with constant coefficients, then if the coefficients are constants $C(k) and D(k)$ with respect to constants $k$ irrelevant to $u$ and $v$, the solution is given by the following equation.
 
\begin{eqnarray}\label{ODE1Sol}
p(u)=C(k)\sin\left( ku \right) +D(k)\cos\left( ku \right) ．
\end{eqnarray}
 
Since the second equation is a variable separable ordinary differential equation, if the coefficients are the constant $E(k)$ for the constant $k$ irrelevant to $u$ and $v$, the solution is given by the following equation.
 
\begin{eqnarray}\label{ODE2Sol}
q(v)=E(k)\exp\left( -\frac{\sigma^{2}k^{2}}{2}v \right) ．
\end{eqnarray}
 
Therefore, the solution $y \left(u, v \right)$ of the heat conduction equation \eqref {HeatConductionEquation} is a constant $k \left(0\leq k \lt \infty \right)$ irrelevant to $u$ and $v$. Then all are superposed to obtain the general solution shown in the following equation.
 
\begin{eqnarray}\label{HeatConductionEquationSol}
y\left(u，v\right)=\int^{+\infty}_{0}\left( C(k)\sin\left( ku \right) +D(k)\cos\left( ku \right) \right)\exp\left( -\frac{\sigma^{2}k^{2}}{2}v \right)dk．
\end{eqnarray}
 
Here, the coefficients $C(k) and D(k)$ of the equation \eqref{HeatConductionEquationSol} are given by the following equation from Fourier's integral theorem as $y \left(u, 0 \right) = g(a)$.
 
\begin{eqnarray}\label{FourierCoefficient}
\left\{
\begin{array}{l}
C(k)=\frac{1}{\pi}\int^{+\infty}_{-\infty}g(a)\cos \left(ka\right) da\\
D(k)=\frac{1}{\pi}\int^{+\infty}_{-\infty}g(a)\sin \left(ka\right) da
\end{array}
\right.
\end{eqnarray}
 
Substituting the obtained equation of coefficients \eqref{FourierCoefficient} into the solution \eqref{HeatConductionEquationSol} of the heat conduction equation \eqref{HeatConductionEquation} and rearranging it gives the following equation.
 
\begin{eqnarray}\label{HeatConductionEquationSol2}
y\left(u，v\right)=\dfrac{1}{\sigma \sqrt[]{\mathstrut 2 \pi v}} \int^{+\infty}_{-\infty}g(a)\exp\left( -\dfrac{1}{2}\left(\dfrac{a-u}{\sigma \sqrt[]{\mathstrut v}}\right)^{2} \right) da．
\end{eqnarray} 

For further analysis, the change of variables is performed again as follows. 
\begin{eqnarray}\label{}
w=\dfrac{a-u}{\sigma \sqrt[]{\mathstrut v}}．
\end{eqnarray}
 
Note that the boundary conditions have changed to the following conditions due to the change of variables.
 
\begin{eqnarray}
g(a)=g\left( u+\sigma \sqrt[]{\mathstrut v}w \right)=\left\{
\begin{array}{l}
K\left( \mathrm{e}^{u+\sigma \sqrt[]{\mathstrut v}w}-1 \right)\cdots w\geq -\dfrac{u}{\sigma \sqrt[]{\mathstrut v}}\\
0\cdots w \lt -\dfrac{u}{\sigma \sqrt[]{\mathstrut v}}
\end{array}
\right.
\end{eqnarray}
 
Focusing on the change of variables by $w$ and the changed boundary conditions, the equation \eqref{HeatConductionEquationSol2} is expanded as follows.
 
\begin{eqnarray}\label{HeatConductionEquationSol3}
y\left(u，v\right)&=&\dfrac{1}{ \sqrt[]{\mathstrut 2 \pi}} \int^{+\infty}_{-\dfrac{u}{\sigma \sqrt[]{\mathstrut v}}}K\left( \exp\left(u+\sigma \sqrt[]{\mathstrut v}w\right)-1 \right)\exp\left( -\dfrac{w^{2}}{2} \right) dw\nonumber \\
&=&\dfrac{1}{ \sqrt[]{\mathstrut 2 \pi}} \int^{+\infty}_{-\frac{u}{\sigma \sqrt[]{\mathstrut v}}}K\exp\left(u+\sigma \sqrt[]{\mathstrut v}w-\dfrac{w^{2}}{2} \right) dw-\dfrac{1}{ \sqrt[]{\mathstrut 2 \pi}} \int^{+\infty}_{-\frac{u}{\sigma \sqrt[]{\mathstrut v}}}K\exp\left( -\dfrac{w^{2}}{2} \right) dw．
\end{eqnarray}
 
Furthermore, if the first term on the right side of the equation \eqref{HeatConductionEquationSol3} is replaced with $z = w- \sigma \sqrt[]{\mathstrut v}$ and the second term is replaced with $z = w$, the following equation is obtained.
 
\begin{eqnarray}\label{HeatConductionEquationSol4}
y\left(u，v\right)&=&x\exp\left(rv\right) \dfrac{1}{ \sqrt[]{\mathstrut 2 \pi}} \int^{+\infty}_{-\frac{u}{\sigma \sqrt[]{\mathstrut v}}-\sigma \sqrt[]{\mathstrut v}}\exp\left( -\dfrac{z^{2}}{2} \right) dz-K\dfrac{1}{ \sqrt[]{\mathstrut 2 \pi}} \int^{+\infty}_{-\frac{u}{\sigma \sqrt[]{\mathstrut v}}}\exp\left( -\dfrac{z^{2}}{2} \right) dz\nonumber \\
&=&x\exp\left(rv\right)N\left( \frac{u}{\sigma \sqrt[]{\mathstrut v}}+\sigma \sqrt[]{\mathstrut v} \right)-KN\left( \frac{u}{\sigma \sqrt[]{\mathstrut v}} \right)．
\end{eqnarray}
 
Finally, by substituting the obtained equation \eqref{HeatConductionEquationSol4} into the solution of the Black-Scholes PDE \eqref{val2} is obtained as an analytical solution of the Black-Scholes PDE, which is a function that satisfies the Black-Scholes PDE.
 
\begin{eqnarray}\label{HeatConductionEquationSol4}
c\left(t，x\right)=xN\left(\frac{u}{\sigma\sqrt[]{\mathstrutv}}+\sigma\sqrt[]{\mathstrut v} \right)-K\exp\left(-rv\right)N\left( \frac{u}{\sigma \sqrt[]{\mathstrut v}} \right)．
\end{eqnarray}
 
However,
 
\begin{eqnarray}
u=\log \frac{x}{K}+\left(r-\frac{\sigma^{2}}{2}\right)\left(T-t\right)
v=T-t
\end{eqnarray}

## Reference
* Shreve, S., 2004. Stochastic Calculus for Finance II: Continuous-Time Models
* Ishimura, S., 2008. Black Shoals differential equations for finance and securities (In Japanese)