---
title: "Плотность вероятности функции от случайной величины"
---
## Плотность вероятности функции от случайной величины ##

### Def. (Борелевская функция) ###
Борелевской называется измеримая функция вида $g : (\RR^n, \BB^n)\mapsto (\RR^m,\BB^m)$.
То есть функция, относительно которой прообразами борелевских множеств являются борелевские множества.

### Def. (Борелевская фунция от случайной величины) ###
Пусть $X = (X_1, \ldots, X_n)$ --- r.v. на $(\Omega, \FF, \pr)$.
${\Psi_j, j=\overline{1,k}}$ --- борелевские функции ${\Psi_j : X(\Omega)\mapsto\RR}$.
${\Psi = (\Psi_1, \ldots, \Psi_k)}$,
${\Psi : X(\Omega)\mapsto\Gamma, \quad \Gamma\subset\RR^k}$ --- отображение из области $X(\Omega)$ значений r.v. $X$
в область $k$-мерного вещественного пространства.

$Y = (Y_1, \ldots, Y_k), \quad Y_j = \Psi_j(X)$ --- случайная величина $Y: \Omega\mapsto\Gamma$

### Задача: найти плотность $f_Y$ по данной плотности $f_X$ ###

1.  $f_Y (y_1,\ldots,y_k) = \frac{\partial^k F(y_1, \ldots, y_k)}{\partial y_1 \ldots \partial y_k}$

2.  $A = \Psi^{-1}(B)$
    $\pr\{ Y(\omega)\in B\} = \pr\{ X(\omega)\in A\}$
    $\idotsint_B f_Y(y_1,\ldots,y_k) \dd y_1\ldots \dd y_k = \idotsint_A f_X (x_1,\ldots,x_n) \dd x_1 \ldots \dd x_n$

3.  В частности, пусть $k=n$.
    
    $\Psi\in C^{\infty} (X(\Omega), \Gamma), \Psi\uparrow,$
    $x = \Psi^{-1}(y)$

    $$J(y) = \frac{\partial\Psi^{-1}}{\partial y} =
      \begin{vmatrix}
      &\frac{\partial\Psi_1^{-1} (y)}{\partial y_1} & \ldots & \frac{ \partial \Psi_1^{-1}(y)}{\partial y_n} \\
      &\vdots & \ddots & \vdots \\
      &\frac{\partial\Psi_n^{-1} (y)}{\partial y_1} & \ldots & \frac{ \partial \Psi_n^{-1}(y)}{\partial y_n}
      \end{vmatrix}
    $$
    
    $$f_Y (y) = f_X (\Psi(y)) \left|{\frac{\partial\Psi^{-1}}{\partial y}}\right|$$

    Пример:
    
    $X\sim \Gaussian(0,1)$.
    
    $f_X = \frac{1}{\sqrt{2\pi}}\exp{-\frac{x^2}{2}}$.

    $Y = aX + b, a\neq 0$.
    $X = \frac{Y-b}{a}$.
    
    $J = \frac{1}{a}$

    $f_Y(y) = f_X(\Psi^{-1}(y))|J(y)| = \frac{1}{|a|\sqrt{2\pi}} \exp{-\frac{(y-b)^2}{2a^2}}$

    То есть $Y\sim \Gaussian(b, |a|)$.

4.  Пусть $k < n$.
`
    $X = (X_1, \ldots, X_n)$,
    $Y = (\Psi_1(X), \ldots, \Psi_k(X))$

    Введём

    $Y^\star = (Y_1, \ldots, Y_n) := (\Psi_1(X), \ldots, \Psi_k(X), X_{k+1}, \ldots, X_{n})$

    ${y^\star = (y_1, \ldots, y_n)}\in\RR^n, {y = (y_1,\ldots,y_k) \in\Gamma}$


    $$f_{Y^\star}(y^\star) = f_X(\Psi_1^{-1}(y_1,\ldots,y_k), \ldots, \Psi_k^{-1}(y_1,\ldots,y_k), y_{k+1}, \ldots, y_{n})$$

    $$\begin{aligned}
      & f_Y(y) &&=
        \idotsint_{-\infty}^{+\infty}
        f_{Y^\star} (y) \dd y_{k+1} \ldots \dd y_{n} = \\
      & &&= \idotsint_{-\infty}^{+\infty}
          f_X(\Psi_1^{-1}(y_1,\ldots,y_k), \ldots, \Psi_k^{-1}(y_1,\ldots,y_k), y_{k+1}, \ldots, y_{n})
          |J(y)|
          \dd y_{k+1} \ldots \dd y_{n}
    \end{aligned}$$
