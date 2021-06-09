---
layout: post
title: Organize and implement Hull and White (1994a) interest rate model 
excerpt: "This is a modified version of the report for semminar at a financial consulting firm in 2018."
categories: Business Finance
tags: [ Business Finance]
comments: true
---

* Table of Contents
{:toc}

# Organize and implement Hull and White (1994a) interest rate model
## Derivation of Hull and White (1994a) interest rate model solutions and boundary conditions

* Definition [Hull and White(1994a) interest rate model]
\begin{eqnarray}\label{HullandWhite1994a}
dr(t)=(\theta(t)-ar(t))dt+\sigma d\tilde{W}(t) ．
\end{eqnarray}


However, $\tilde{W}(t)$ is Brownian motion under the risk-neutral measure $\mathbb{P}$.
Also, $\theta (t)$, $a$, and $\sigma$ are positive-definite functions for time (Hull and White, 1994a).
 
* Definition [Discount bond price evaluation formula]
\begin{eqnarray}\label{DiscountBondPrice}
B(t,T)=\tilde{\mathbb{E}}[e^{-\int_{t}^{T}R(s)ds}|{\cal F}(t)] ．
\end{eqnarray}

 
Here, a discount bond is a contract in which $1$ is paid for a certain fixed maturity of $T$, and no payment is made before the maturity.
 
* Definition [Yield from time $t$ to $T$]
\begin{eqnarray}
Y(t,T)=-\frac{1}{T-t}\log B(t,T)．
\end{eqnarray}


This is equivalent to the following equation.

\begin{eqnarray}
B(t,T)=e^{-Y(t,T)(T-t)}．
\end{eqnarray}

Therefore, $B(T, T) =1$.
 
The random variable $e^{-\int_{t}^{T}R(s)ds}$ estimated in the equation \eqref{DiscountBondPrice} depends not only on $R(T)$ but also on the path. However, the path of $R$ to time $t$ depends only on $R(t)$ at time $t$. Therefore, since $R$ is a Markov process, the bond price $B(t, T)$ is considered to be a function of time $t$ and $R(t)$.

\begin{eqnarray}
B(t,T)=f(t,R(t))．
\end{eqnarray}
 
On the other hand, since the equation \eqref{DiscountBondPrice} is the expansion of $D(t)B(t,T)=\tilde{\Bbb{E}}[D(T)B(T,T))|{\cal F}(t)]$, then $D(t)B(t,T)=D(t)f(t,T)$ is a martingale. 

Therefore, in order for the no arbitrage condition to hold, the drift $(dt)$ term obtained by differentiating $D(t)f(t,T)$ must appear as $0$.
 
To find the derivative of $D(t)f(t,T)$, it is required first to find the discount process and its relational expression.

* Definition [discount process]
\begin{eqnarray}
D(t)=e^{-\int_{0}^{t}R(s)ds}．
\end{eqnarray}


Here, if $S(x)=e(-t)$ and $I(t)=\int_{0}^{t}R(s)ds$, then $D(t) = S(I(t))$.
At this time, since $dI(t)=R(t)dt$, $dI(t)dI (t)=0$ and $S'(x)=-S (x)$, $S''(x) =S(x)$ then from Ito's lemma,

\begin{eqnarray}
dD(t)=dS(I(t)) 
=S'(I(t))dI(t)+\frac{1}{2}S''(I(t))dI(t)dI(t) 
=-S(I(t))dI(t) 
=-D(t)R(t)dt．
\end{eqnarray}

therefore,

\begin{eqnarray}
dD(t)=-D(t)R(t)dt．
\end{eqnarray}
 
If the interest rate process $R(t)$ in finding the derivative of $D(t)f(t,T)$ follows the equation \eqref{HullandWhite1994a}, then From $dtdt=0$, $dtd\tilde{W}=0$, $d\tilde{W}d\tilde{W}=dt$ and $drdr= \sigma^2dt$

\begin{eqnarray}
d(D(t)f(t,T))
=f(t,T)dD(t)+D(t)df(t,T)
=f(t,T)(-D(t)R(t))+D(t){f_t(t,T)dt+f_r(t,T)dr+\frac{1}{2}f_rr(t,T)drdr} 
=D(t)(-rf(t,T)+f_t(t,T)+\frac{1}{2}\sigma^2 f_rr(t,T)+(\theta(t)-ar(t))f_r(t,T))dt+D(t)\sigma f_r(t,T)d\tilde{W}(t)．
\end{eqnarray}

Therefore, $f(t, T))$ must be met.
 
\begin{eqnarray}\label{HullWhitePDE}
f_t(t,T)+\frac{1}{2}\sigma^{2} f_rr(t,T)+(\theta(t)-ar(t))f_r(t,T)=rf(t,T)
\end{eqnarray}

Also, since $1=B(T, T)=f(T, r)$, the terminal condition is obtained.
 
For all $r$,
\begin{eqnarray}
f(T,r)=1
\end{eqnarray}
 
Next, the partial differential equation of the equation \eqref{HullWhitePDE} is expanded to obtain an analytical solution.
If you set $f_t(t, T)=e^{-rC (t, T) -A (t, T)}$,

\begin{eqnarray}
f_t(t,r)=(-rC'(t,T)-A'(t,T))f(t,r)． 
f_r(t,r)=-C(t,T)f(t,r)． 
f_rr(t,r)=-C^{2}(t,T)f(t,r)．
\end{eqnarray}

Where $C'(t,T)=\frac{\partial C(t,T)}{\partial t}$，$A'(t,T)=\frac{\partial A(t,T)}{\partial t}$．
Therefore, the left side of the formula \eqref{HullWhitePDE} is

\begin{eqnarray}
f_t(t,T)+\frac{1}{2}\sigma f_rr(t,T)+(\theta(t)-ar(t))f_r(t,T) 
=(-rC'(t,T)-A'(t,T)+\frac{1}{2}\sigma^{2}C^{2}(t,T)-(\theta(t)-ar(t))C(t,T))f(t,r)．
\end{eqnarray}

Therefore, by transposing the right side to the left side and enclosing it with $r$, the following relational expression is obtained.

\begin{eqnarray}
((-C'(t,T)+aC(t,T)-1)r-A'(t,T)-\theta(t)C(t,T)+\frac{1}{2}\sigma^{2}C^{2}(t,T))f(t,r)=0．
\end{eqnarray}

From the assumption, $f_t(t, T)=e^{-rC(t, T)-A(t, T)}>0$, and this relation must hold for all $r$, then this term for $r$ must be $0$.

\begin{eqnarray}
C'(t,T)=aC(t,T)-1．
A'(t,T)=-\theta(t)C(t,T)+\frac{1}{2}\sigma^{2}C^{2}(t,T)．
\end{eqnarray}

Furthermore, $C(T, T)=A'(T, T)=A(T, T)=0$ is required to hold for the terminal condition.
 
A function that satisfies $C'(t, T)=aC(t, T)-1$, $C(T, T)=0$

\begin{eqnarray}
C(t,T)=\int_{t}^{T}e^{-\int_{t}^{s}a(v)dv}ds．
\end{eqnarray}

It is shown that this is a unique solution to be obtained.
 
\begin{eqnarray}
\frac{d }{d s}(e^{-\int_{0}^{s}a(v)dv} C(s,T))
=e^{-\int_{0}^{s}a(v)dv}(-a(s)C(s,T)+C'(s,T) ) 
=e^{-\int_{0}^{s}a(v)dv}(-a(s)C(s,T)+aC(t,T)-1 ) 
=e^{-\int_{0}^{s}a(v)dv}．
\end{eqnarray}

Integrating both sides of this equation from $t$ to $T$

\begin{eqnarray}
e^{-\int_{0}^{T}a(v)dv}C(T,T)-e^{-\int_{0}^{t}a(v)dv}C(t,T)=-\int_{t}^{T}e^{-\int_{0}^{s}a(v)dv}ds 
\Leftrightarrow C(t,T)=e^{\int_{0}^{t}a(v)dv}\int_{t}^{T}e^{-\int_{0}^{s}a(v)dv}ds  
=\int_{t}^{T}e^{-\int_{t}^{s}a(v)dv}ds．
\end{eqnarray}

The expansion of this unique solution is as follows. However, $a(v)=a$ is set from the equation \eqref{HullandWhite1994a}.

\begin{eqnarray}
C(t,T)=\int_{t}^{T}e^{-\int_{t}^{s}a(v)dv}ds 
=\int_{t}^{T}e^{-as+at}ds 
=\frac{1}{a}(1-e^{-a(T-t)})．
\end{eqnarray}

Similarly, the function, that satisfies $A(T, T)=1$, $A'(t, T)=-\theta(t)C(t, T)+\frac{1}{2}\sigma^{2}C^{2}(t, T)$, is shown below as a unique solution.

\begin{eqnarray}
A(t,T)=\int_{t}^{T}(\theta(t)C(t,T)-\frac{1}{2}\sigma^{2}C^{2}(t,T) )ds．
\end{eqnarray}

Integrating both sides of this equation from $t$ to $T$
\begin{eqnarray}
A(T,T)-A(t,T)=-\int_{t}^{T}\theta(t)C(t,T)ds+\frac{1}{2}\int_{t}^{T}\sigma^{2}C^{2}(t,T)ds 
\Leftrightarrow A(t,T)=\int_{t}^{T}(\theta(t)C(t,T)-\frac{1}{2}\sigma^{2}C^{2}(t,T))ds．
\end{eqnarray}

The expansion of this unique solution is as follows. However, $a(v)=a$ is set from the equation \eqref{HullandWhite1994a}.

\begin{eqnarray}
A(t,T)=\int_{t}^{T}(\theta(t)C(t,T)-\frac{1}{2}\sigma^{2}C^{2}(t,T) )ds 
=\int_{t}^{T}(\frac{\theta(t)}{a}(1-e^{-a(T-t)})-\frac{1}{2}\sigma^{2}\frac{1}{a^2}(1-e^{-a(T-t)} )^{2} )ds 
=\frac{\sigma^{2}}{2a^3}(-a(T-t)+2(1-e^{-a(T-t)})-\frac{1}{2}(1-e^{-2a(T-t)})) 
+\frac{1}{a}\int_{t}^{T}\theta(s)(1-e^{-a(T-s)})ds．
\end{eqnarray}
 
Next, the parameter $\theta(t)$ in the equation \eqref{HullandWhite1994a} means the speed of mean reversion. It is required to match this parameter to the term structure of the quoted interest rate.
 
* Definition [Instantaneous Forward Rate]
Let $f^{M}(0, T)$ be the instantaneous forward rate of the market at maturity $T$ at time $0$.
\begin{eqnarray}
f^{M}(0,T)=-\frac{\partial \ln B^{M}(0,T)}{\partial T}．
\end{eqnarray}
Here, $B^{M}(0, T)$ is the discount bond price quoted in the market at maturity $T$.

 
Because it is $B(t,T)=f(t,r)=e^{-rC(t,T)-A(t,T)}$，
 
\begin{eqnarray}
\ln B(0,T)=-rC(0,T)-A(0,T) 
=-\frac{r}{a}(1-e^{-aT} ) 
-\frac{\sigma^{2}}{2a^3}(-aT+2(1-e^{-aT})-\frac{1}{2}(1-e^{-2aT})) 
+\frac{1}{a}\int_{0}^{T}\theta(s)(1-e^{-a(T-s)})ds 
\Leftrightarrow \frac{\partial \ln B^{M}(0,T)}{\partial T}=re^{-aT}+\frac{\sigma^{2}}{2a^3}(-a+2ae^{-aT}+e^{-2aT})+\int_{t}^{T}\theta(s)e^{-a(T-s)}ds 
\Leftrightarrow f^{M}(0,T)=re^{-aT}+\frac{\sigma^{2}}{2a^3}(-a+2ae^{-aT}+e^{-2aT})+\int_{t}^{T}\theta(s)e^{-a(T-s)}ds．
\end{eqnarray}
 
The following relationship is used to derive $\theta(T)$ from $f^{M}(0, T)$.
 
\begin{eqnarray}
H(t)=\int_{0}^{t}h(s,t)dsarrow H'(t)=\int_{0}^{t}\frac{\partial h(s,t)}{\partial t}ds+h(t,t)．
\end{eqnarray}
 
Here, $x(t)=re^{-at}+\int_{0}^{t}\theta(s)e^{-a(t-s)}ds$

\begin{eqnarray}
x'(t)=-a(re^{-at}+\int_{0}^{t}\theta(s)e^{-a(t-s)}ds)+\theta(t) 
x'(t)=-ax(t)+\theta(t) 
\Leftrightarrow \theta(t)=x'(t)+ax(t) 
arrow \theta(T)=x'(T)+ax(T)．
\end{eqnarray}
 
On the other hand, if it is set $g(t)=\frac{\sigma^2}{2a^2}(-1+2e^{-at}+e^{-2at})$

\begin{eqnarray}
f^{M}(0,T)=x(T)+g(T) 
\Leftrightarrow x(T)=f^{M}(0,T)-g(T)．
\end{eqnarray}
 
Therefore 
\begin{eqnarray}
\theta(T)=\frac{\partial f^{M}(0,T)}{\partial T}-\frac{\partial g(T)}{\partial T}+ax(t)．
\end{eqnarray}

Here, since it is $\frac{\partial g(T)}{\partial T}=-\frac{\sigma^2}{a}(e^{-aT}+e^{-2aT})$, the following equation is obtained after all.


\begin{eqnarray}
\theta(T)=\frac{\partial f^{M}(0,T)}{\partial T}+\frac{\sigma^2}{a}(e^{-aT}+e^{-2aT})+af^{M}(0,T)-\frac{\sigma^2}{2a^2}(-1+2e^{-at}+e^{-2at})．
\end{eqnarray}
 
## Hull and White Tree formulation
 
In the following, to represent the interest rate model as the $3$ term tree, it is derived the relational expression between the parameters of the continuous time process and the parameters of the $3$ term process.

In the $3$ term process, it is expressed by $p_u$, $p_m$, and $p_d$, respectively, during the minute time $\Delta t$ as the interest rate rises by the spatial division width $\Delta x$, or stays at the same level, decreasing by $\Delta x$. 

Furthermore, $\Delta t$ and $\Delta x$ cannot be selected independently and must satisfy the conditions for stability and convergence of the finite difference method $\Delta x=\sigma \sqrt{3\Delta t}$ (Hull and White, 1994).

Here, if the drift term of the formula \eqref{HullandWhite1994a} is set $\nu=\theta(t)-ar(t)$,

\begin{eqnarray}\label{averrageA}
\mathbb{E}[\Delta x]=p_u(\Delta x)+p_m(0)+p_d(-\Delta x)=\nu\Delta t．
\end{eqnarray}
\begin{eqnarray}\label{varianceA}
\mathbb{E}[\Delta x^2]=p_u(\Delta x^2)+p_m(0)+p_d(-\Delta x^2)=\sigma^2\Delta t+\nu^2\Delta t^2．
\end{eqnarray}
\begin{eqnarray}\label{SumProA}
p_u+p_m+p_d=1．
\end{eqnarray}
 
The expression \eqref{averrageA} and the expression \eqref{varianceA} are expanded as follows.

\begin{eqnarray}\label{averrageAA}
p_u\Delta x-p_d\Delta x=\nu \Delta t．
\end{eqnarray}
\begin{eqnarray}\label{varianceAA}
p_u\Delta x^2-p_d\Delta x^2=\sigma^2\Delta t+\nu^2\Delta t^2．
\end{eqnarray}
 
Multiply the expression \eqref{averrageAA} by $\Delta x$ and add the expression \eqref{varianceAA},

\begin{eqnarray}\label{puA}
2p_u\Delta x^2=\nu^2\Delta t^2+\sigma^2\Delta t+\nu \Delta t\Delta x 
p_u=\frac{1}{2}(\frac{\nu^2\Delta t^2+\sigma^2\Delta t}{\Delta x^2}+\frac{\nu \Delta t}{\Delta x} )．
\end{eqnarray}
 
Also, substituting the expression \eqref{puA} into the expression \eqref{averrageAA},

\begin{eqnarray}
p_u\Delta x-p_d\Delta x=\frac{1}{2}(\frac{\nu^2\Delta t^2+\sigma^2\Delta t}{\Delta x^2}+\frac{\nu \Delta t}{\Delta x} )\Delta x-p_d\Delta x 
\Leftrightarrow p_d\Delta x=\frac{1}{2}(\frac{\nu^2\Delta t^2+\sigma^2\Delta t}{\Delta x^2}-\frac{\nu \Delta t}{\Delta x} )\Delta x  
p_d=\frac{1}{2}(\frac{\nu^2\Delta t^2+\sigma^2\Delta t}{\Delta x^2}-\frac{\nu \Delta t}{\Delta x} )．
\end{eqnarray}
 
And if it is substituted the expression \eqref{puA} and the expression \eqref{puA} into the expression \eqref{SumProA}

\begin{eqnarray}\label{pmA}
p_u+p_m+p_d=\frac{1}{2}(\frac{\nu^2\Delta t^2+\sigma^2\Delta t}{\Delta x^2}+\frac{\nu \Delta t}{\Delta x} )+p_m+\frac{1}{2}(\frac{\nu^2\Delta t^2+\sigma^2\Delta t}{\Delta x^2}-\frac{\nu \Delta t}{\Delta x} ) 
=\frac{\nu^2\Delta t^2+\sigma^2\Delta t}{\Delta x^2}+p_m 
\Leftrightarrow p_m=1-\frac{\nu^2\Delta t^2+\sigma^2\Delta t}{\Delta x^2}．
\end{eqnarray}
 
Hull And White (1994a) proposed a method for constructing an efficient and accurate short rate for the equation \eqref{HullandWhite1994a}. Also, it is assumed $\theta(t)=0$，$r(0)=0$. 

\begin{eqnarray}
dr(t)=ar(t)dt+\sigma d\tilde{W}(t) ．
\end{eqnarray}
 
Therefore, note that $\nu=-ar$. In this simplified tree, the value of $r$ at the time $i\Delta t$ is $j\Delta t$. Since the tree is designed to reduce the amount of calculation, $j$ needs to be between $BottomNode[i]$ and $TopNode[i]$. The choice of which branching process to take at each node depends on the sign of $a$ and the size of $j$, and the range of change $\Delta x(=\Delta r)$ in the simplified $r$ process is chosen to match the expected value of $\mathbb{E}[\Delta x]$ and the variance $Var(\Delta x)$. Furthermore, when $a$ is positive, if $M$ is the expected value of the fluctuation range, when $j$ is the smallest integer larger than $-0.184/M$, the standard branching process is switched to the downward branching process. In order to maintain the symmetry, HW proposes to switch from the standard branching process to the upward branching process in the node $j$ with a negative sign for this node (Hull and White, 1994). 

Here，
\begin{eqnarray}
\mathbb{E}[\Delta x]=\nu \Delta t 
=-ar\Delta t 
=Mr 
\Leftrightarrow M=-a\Delta t．
\end{eqnarray}

Also，
\begin{eqnarray}
Var(\Delta x)=\mathbb{E}[\Delta x^2]-(\mathbb{E}[\Delta x])^2 
=(\nu^2\Delta t^2+\sigma^2\Delta t)-(\nu \Delta t)^2 
=\sigma^2\Delta t．
\end{eqnarray}
It becomes. Here,$M^2=a^2\Delta t^2$，$r=j\Delta r$,
 
\begin{eqnarray}\label{ExForPb1}
\frac{\nu^2\Delta t^2+\sigma^2\Delta t}{\Delta x^2}=\frac{(-ar)^2\Delta t^2+\sigma^2\Delta t}{ (\sigma \sqrt(3\Delta t))^2} 
=\frac{(-a\Delta t)^2r^2+\sigma^2\Delta t}{ 3\sigma^2 \Delta t} 
=\frac{M^2(j\Delta r)^2+\sigma^2\Delta t}{ 3\sigma^2 \Delta t} 
=\frac{1}{3}\frac{j^2 M^2 \Delta r^2+\sigma^2\Delta t}{ \sigma^2 \Delta t} 
=\frac{1}{3}\frac{j^2 M^2 \Delta r^2}{ \sigma^2 \Delta t}+\frac{1}{3} 
=\frac{1}{3}\frac{j^2 M^2 (3\sigma^2 \Delta t)}{ \sigma^2 \Delta t}+\frac{1}{3} 
=j^2M^2+\frac{1}{3}．
\end{eqnarray}
 
Therefore from the formula \eqref{ExForPb1},
\begin{eqnarray}
p_m=1-\frac{\nu^2\Delta t^2+\sigma^2\Delta t}{\Delta x^2} 
=1-(j^2M^2+\frac{1}{3}) 
=\frac{2}{3}-j^2M^2．
\end{eqnarray}
 
On the other hand,
\begin{eqnarray}\label{ExForPb2}
\frac{\nu\Delta t}{\Delta x}=\frac{(-ar)\Delta t}{\sigma\sqrt(3\Delta t)} 
=\frac{-Mr}{\sigma\sqrt(3\Delta t)} 
=\frac{-jr\Delta r}{\sigma\sqrt(3\Delta t)} 
=\frac{-jr(\sigma\sqrt(3\Delta t))}{\sigma\sqrt(3\Delta t)} 
=-jM．
\end{eqnarray}
 
Therefore from the formula \eqref{ExForPb2},

\begin{eqnarray}
p_u=\frac{1}{2}(\frac{\nu^2\Delta t^2+\sigma^2\Delta t}{\Delta x^2}+\frac{\nu \Delta t}{\Delta x} ) 
=\frac{1}{2}( j^2M^2+\frac{1}{3} -jM ) 
=\frac{1}{6}+\frac{j^2M^2-jM}{2}．
\end{eqnarray}
 
\begin{eqnarray}
p_d=\frac{1}{2}(\frac{\nu^2\Delta t^2+\sigma^2\Delta t}{\Delta x^2}-\frac{\nu \Delta t}{\Delta x}) 
=\frac{1}{2}(j^2M^2+\frac{1}{3}+jM) 
=\frac{1}{6}+\frac{j^2M^2+jM}{2}．
\end{eqnarray}
 
Next, it is derived from the probabilities corresponding to the upward branching process.
 
\begin{eqnarray}\label{averrageB}
\mathbb{E}[\Delta x]=p_u(2\Delta x)+p_m(\Delta x)+p_d(0)=\nu\Delta t．
\end{eqnarray}
\begin{eqnarray}\label{varianceB}
\mathbb{E}[\Delta x^2]=p_u(2\Delta x)^2+p_m(\Delta x^2)+p_d(0)=\sigma^2\Delta t+\nu^2\Delta t^2．
\end{eqnarray}
\begin{eqnarray}\label{SumProB}
p_u+p_m+p_d=1．
\end{eqnarray}
 
The expression \eqref{averrageB} and the expression \eqref{varianceB} are expanded as follows.

\begin{eqnarray}\label{averrageBB}
2p_u\Delta x+p_m\Delta x=\nu \Delta t．
\end{eqnarray}
\begin{eqnarray}\label{varianceBB}
4p_u\Delta x^2+p_m\Delta x^2=\sigma^2\Delta t+\nu^2\Delta t^2．
\end{eqnarray}
 
Subtracting the expression \eqref{averrageBB} from the expression \eqref{varianceBB} multiplied by $\Delta x$

\begin{eqnarray}\label{puB}
2p_u\Delta x^2=\nu^2\Delta t^2+\sigma^2\Delta t-\nu \Delta t\Delta x 
p_u=\frac{1}{2}(\frac{\nu^2\Delta t^2+\sigma^2\Delta t}{\Delta x^2}-\frac{\nu \Delta t}{\Delta x} )．
\end{eqnarray}
 
Also, if it is assigned the expression \eqref{puB} to the expression \eqref{averrageBB},
\begin{eqnarray}\label{pmB}
2p_u\Delta x+p_m\Delta x=\frac{\nu^2\Delta t^2+\sigma^2\Delta t}{\Delta x^2}-\frac{\nu \Delta t}{\Delta x}+p_m\Delta x 
\Leftrightarrow p_m\Delta x=2\nu \Delta t-\frac{\nu^2\Delta t^2+\sigma^2\Delta t}{\Delta x^2}  
\Leftrightarrow p_m=\frac{2\nu \Delta t}{\Delta x}-\frac{\nu^2\Delta t^2+\sigma^2\Delta t}{\Delta x^2}．
\end{eqnarray}
 
And if it is substituted the expression \eqref{puB} and the expression \eqref{pmB} into the expression \eqref{SumProB}
\begin{eqnarray}\label{pdB}
p_u+p_m+p_d=\frac{1}{2}(\frac{\nu^2\Delta t^2+\sigma^2\Delta t}{\Delta x^2}-\frac{\nu \Delta t}{\Delta x} )+\frac{2\nu \Delta t}{\Delta x}-\frac{\nu^2\Delta t^2+\sigma^2\Delta t}{\Delta x^2}+p_d 
=\frac{3}{2}\frac{\nu \Delta t}{\Delta x}-\frac{1}{2}\frac{\nu^2\Delta t^2+\sigma^2\Delta t}{\Delta x^2}+p_d 
\Leftrightarrow p_d=1-\frac{1}{2}( \frac{3\nu \Delta t}{\Delta x}-\frac{\nu^2\Delta t^2+\sigma^2\Delta t}{\Delta x^2} ) ．
\end{eqnarray}
 
Therefore from the formula \eqref{ExForPb1},
\begin{eqnarray}
p_u=\frac{1}{2}(\frac{\nu^2\Delta t^2+\sigma^2\Delta t}{\Delta x^2}-\frac{\nu \Delta t}{\Delta x} ) 
=\frac{1}{2}( j^2M^2+\frac{1}{3}-(-jM)) 
=\frac{1}{6}-\frac{j^2M^2+jM}{2}．
\end{eqnarray}
 
\begin{eqnarray}
p_m=\frac{2\nu \Delta t}{\Delta x}-\frac{\nu^2\Delta t^2+\sigma^2\Delta t}{\Delta x^2} 
=-2jM-(j^2M^2+\frac{1}{3}) 
=\frac{1}{3}-j^2M^2-2jM．
\end{eqnarray}
 
\begin{eqnarray}
p_d=1-\frac{1}{2}( \frac{3\nu \Delta t}{\Delta x}-\frac{\nu^2\Delta t^2+\sigma^2\Delta t}{\Delta x^2} ) 
=1-frac{1}{2}( -3jM-j^2M^2-\frac{1}{3}) 
=\frac{7}{6}+\frac{j^2M^2+3jM}{2}．
\end{eqnarray}
 
Then, the probability corresponding to the downward branching process is derived.
 
\begin{eqnarray}\label{averrageC}
\mathbb{E}[\Delta x]=p_u(0)+p_m(-\Delta x)+p_d(-2\Delta x)=\nu\Delta t．
\end{eqnarray}
\begin{eqnarray}\label{varianceC}
\mathbb{E}[\Delta x^2]=p_u(0)+p_m(-\Delta x)^2+p_d(-2\Delta x)^2=\sigma^2\Delta t+\nu^2\Delta t^2．
\end{eqnarray}
\begin{eqnarray}\label{SumProC}
p_u+p_m+p_d=1．
\end{eqnarray}
 
The expression \eqref{averrageC} and the expression \eqref{varianceC} are expanded as follows.
\begin{eqnarray}\label{averrageCC}
-p_m\Delta x-2p_d\Delta x=\nu \Delta t．
\end{eqnarray}
\begin{eqnarray}\label{varianceCC}
p_m\Delta x^2+4p_d\Delta x^2=\sigma^2\Delta t+\nu^2\Delta t^2．
\end{eqnarray}
 
Add the expression \eqref{varianceCC} multiplied by $\Delta x$ and the expression \eqref{averrageCC},
\begin{eqnarray}\label{pdC}
2p_d\Delta x^2=\nu^2\Delta t^2+\sigma^2\Delta t+\nu \Delta t\Delta x 
p_d=\frac{1}{2}(\frac{\nu^2\Delta t^2+\sigma^2\Delta t}{\Delta x^2}+\frac{\nu \Delta t}{\Delta x} )．
\end{eqnarray}
 
Also, if it is assigned the expression \eqref{pdC} to the expression \eqref{averrageCC},
\begin{eqnarray}\label{pmC}
-p_m\Delta x-2p_d\Delta x=-p_m\Delta x-\frac{\nu^2\Delta t^2+\sigma^2\Delta t}{\Delta x^2}-\frac{\nu \Delta t}{\Delta x} 
\Leftrightarrow -p_m\Delta x=2\nu \Delta t+\frac{\nu^2\Delta t^2+\sigma^2\Delta t}{\Delta x^2}  
\Leftrightarrow p_m=-\frac{2\nu \Delta t}{\Delta x}-\frac{\nu^2\Delta t^2+\sigma^2\Delta t}{\Delta x^2}．
\end{eqnarray}
 
And if it is substituted the expression \eqref{pdC} and the expression \eqref{pmC} into the expression \eqref{SumProC},
\begin{eqnarray}\label{puC}
p_u+p_m+p_d=p_u-\frac{2\nu \Delta t}{\Delta x}-\frac{\nu^2\Delta t^2+\sigma^2\Delta t}{\Delta x^2}+\frac{1}{2}(\frac{\nu^2\Delta t^2+\sigma^2\Delta t}{\Delta x^2}+\frac{\nu \Delta t}{\Delta x} ) 
=p_u-\frac{3}{2}\frac{\nu \Delta t}{\Delta x}-\frac{1}{2}\frac{\nu^2\Delta t^2+\sigma^2\Delta t}{\Delta x^2} 
\Leftrightarrow p_u=1+\frac{3}{2}\frac{\nu \Delta t}{\Delta x}+\frac{1}{2}\frac{\nu^2\Delta t^2+\sigma^2\Delta t}{\Delta x^2}．
\end{eqnarray}
 
Therefore from the formula \eqref{ExForPb1},
\begin{eqnarray}
p_d=\frac{1}{2}(\frac{\nu^2\Delta t^2+\sigma^2\Delta t}{\Delta x^2}+\frac{\nu \Delta t}{\Delta x} ) 
=\frac{1}{2}( j^2M^2+\frac{1}{3}-jM) 
=\frac{1}{6}-\frac{j^2M^2-jM}{2}．
\end{eqnarray}
 
\begin{eqnarray}
p_m=-\frac{2\nu \Delta t}{\Delta x}-\frac{\nu^2\Delta t^2+\sigma^2\Delta t}{\Delta x^2} 
=2jM-(j^2M^2+\frac{1}{3}) 
=-\frac{1}{3}-j^2M^2+2jM．
\end{eqnarray}
 
\begin{eqnarray}
p_u=1+\frac{3}{2}\frac{\nu \Delta t}{\Delta x}+\frac{1}{2}\frac{\nu^2\Delta t^2+\sigma^2\Delta t}{\Delta x^2} 
=1+\frac{3}{2}(-jM)+\frac{1}{2}(j^2M^2+\frac{1}{3}) 
=\frac{7}{6}+\frac{j^2M^2-3jM}{2}．
\end{eqnarray}
 
Finally, the short rate process is introduced into the drift term $a_i$, which fluctuates with time. This drift term is chosen to be consistent with the discount bonds market quoted.
\begin{eqnarray}
P(0,i+1)=\int_{j=BottomNode[i]}^{TopNode[i]}Q_{i,j}e^{(-a_i+j\Delta r)\Delta t}．
\end{eqnarray}

Here, $Q_{i,j}$ is a security that pays $1$ when the node $(i,j)$ is reached, and pays nothing at other times.
Therefore, the drift term $ a_i $ is given as follows.

\begin{eqnarray}
\ln P(0,i+1)=\ln \int_{j=BottomNode[i]}^{TopNode[i]}Q_{i,j}e^{j\Delta r\Delta t}-a_i\Delta t 
\Leftrightarrow a_i\Delta t=\ln \int_{j=BottomNode[i]}^{TopNode[i]}Q_{i,j}e^{j\Delta r\Delta t}-\ln P(0,i+1) 
\Leftrightarrow a_i=\frac{\ln \int_{j=BottomNode[i]}^{TopNode[i]}Q_{i,j}e^{j\Delta r\Delta t}-\ln P(0,i+1)}{\Delta t}．
\end{eqnarray}

## Reference
* Hull, J. and A. White, 1994. "Numerical procedures for implementing term structure models I:Single-Factor Models,'' Journal of Derivatives, 2, 1 (Fall 1994a) 7−16
* Strickland, C. and Clewlow, L., 1998. Implementing Derivatives Models
* Shreve, S., 2004. Stochastic Calculus for Finance II: Continuous-Time Models