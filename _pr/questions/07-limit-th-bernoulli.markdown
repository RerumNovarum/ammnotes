---
title: "Предельные теоремы в схеме Бернулли"
---
## Предельные теоремы в схеме Бернулли ##


Пусть дана последовательность серий испытаний Бернулли,
в которой $n$-й эксперимент состоит в последовательном проведении $n$ испытаний Бернулли
с вероятностью усреха $p_n$.

${\Omega = \prod_{j=1}^n \Omega_j}$, $\Omega_j = \Omega_i$,

$\SigmaField = S(\Omega)$,

$A \subset \Omega_j$,

$A_{n k} = A^\complement \times\ldots\times A^\complement \times A\times A^\complement \times\ldots\times A^\complement$,

$X_{n k} = I_{A_{nk}}$ --- индикатор события $A$ в $i$-м испытании.

$S_n = \sum_{j=1}^n X_k$ --- число появлений события $A$ в $n$-ной серии.

$X_{n k}, k=\overline{1,n}$ --- попарно независимые.

Заметим: $1 = (p_n+q_n)^n = \sum_{k=1}^n {n\choose k} p_n^m q_n^{n-m}$.

$\E X_{n k} = p_n$, $\E X_{nk}^2 = p_n^2$, $\sigma^2 X_{nk} = p_n - p_n^2 = p_n q_n$.

$\E S_n = \sum_{k=1}^n \E X_{nk} = np_n$, $\sigma^2 S_n = \sum_{k=1}^n \sigma^2 X_{nk} = n p_n q_n$.


### Th. (Пуассона-Бернулли) ###
Если

$$
\left\{\begin{aligned}
 & \lim_{n\to\infty} & p_n  &=& 0 &\\
 & \lim_{n\to\infty} & np_n &=& \lambda &> 0 \\
\end{aligned}\right.
$$
То $$\lim_{n\to\infty} \pr [S_n = k] = \frac{\lambda^k}{k!} e^{-\lambda}, \quad k=\overline{1,n}$$

Действительно:
$$ \pr [S_n=k] = {n\choose k} p^k q^{n-k} = \frac{n!}{k!(n-k)!} p^k (1-p)^{n-k} =
                 \frac{n!}{k!(n-k)!} (\frac{\lambda}{n})^k(1 - \frac{\lambda}{n})^{n-k} = 
                 \frac{n(n-1)\cdots(n-k+1)\lambda^k(1-\frac{\lambda}{n})^n} {m!n^k (1-\frac{\lambda}{n})^k}$$
Переходя к пределу по базе $n\to\infty$:
$$ \pr [S_n=k] \to \frac{\lambda^k}{m!}e^{-\lambda}$$

### Th. (Локальная теорема Муавра-Лапласа) ###

Если

1. $\lim_{n\to\infty} p_n = 0$
2. $\lim_{n\to\infty} np_n = \lambda > 0$
3. Величина $x_k = \frac{k-np_n}{\sqrt {np_n q_n}}$, где $k$ --- число успехов,
   равномерно ограничена по $k$ и $n$

То $$P_n(k) = \frac{1}{\sqrt{2\pi np_n q_n}}\exp(-\frac{x_k^2}{2})(1+\alpha_n(k))$$
$$x \approx \frac{k-np_n}{np_n q_n}$$
