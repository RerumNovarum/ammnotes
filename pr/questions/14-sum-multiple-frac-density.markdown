---
title: "Плотность вероятности суммы, произведения и частного"
---
## Плотность вероятности суммы, произведения и частного ##

### Плотность суммы ###
Пусть $X = (X_1, X_2)$, $Y = X_1 + X_2$, $f_X$ --- плотность.
Необходимо найти $f_Y$.

Введём $Y_2 = X_2$ и вектор $Y^\star = (Y, Y_2)$.
$$\left\{\begin{aligned}
& X_1 &=& Y - Y_2 \\
& X_2 &=& Y_2
\end{aligned}\right.$$

$$ J(y^\star) =
\begin{vmatrix}
& 1 & -1 \\
& 0 & 1
\end{vmatrix} = 1$$

$$f_{Y^\star}(y) = f_X(\Psi(y)) |J(y)| = f_X (y - y_2, y_2) |1|$$
$$f_Y(y) = \int_{-\infty}^{+\infty} f_X(y - y_2, y_2) \dd y_2$$

### Плотность произведения ###
Пусть $X=(X_1,X_2)$, $Y = X_1 X_2$.
$Y^\star = (Y_1, Y_2) := (Y, X_2)$.

$$\left\{\begin{aligned}
& X_1 = \frac{Y}{Y_2}\\
& X_2 = Y_2
\end{aligned}\right.$$

$$J(y^\star) =
\begin{vmatrix}
& \frac{1}{y_2} & y_1 \frac{1}{y_2^2} \\
& 0             & 1
\end{vmatrix} = \frac{1}{y_2}$$

$$f_Y(y) = - \int_{-\infty}^0 f_X(\frac{y}{y_2}, y_2) \left|\frac{1}{y_2}\right| \dd y_2
           + \int_0^{+\infty} f_X(\frac{y}{y_2}, y_2) \left|\frac{1}{y_2}\right| \dd y_2$$
