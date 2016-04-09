---
title: "Неравенство Чебышёва. Закон больших чисел"
---
## Неравенство Чебышёва. Закон больших чисел ##

### Неравенство Чебышёва ###
Пусть $X$ --- r.v., то
$\forall \varepsilon > 0$
$$ \pr [ |X| > \varepsilon ] \leq \frac{1}{\varepsilon^2} \E X $$
так как
$$ \E X^2 = \E X^2 I_{[|X|<\varepsilon]} + \E X^2 I_{[|X| \geq \varepsilon]} \geq 
   \E X^2 I_{[|X| \geq \varepsilon]} \geq
   \varepsilon^2 \E I_{[|X|\geq\varepsilon]} = \varepsilon^2 \pr [|X|\geq\varepsilon] $$

### Закон больших чисел ###

Пусть $X_1, X_2, \ldots$ --- последовательность случайных независимых величин, таких что

$\E X_j = m_j$

$\D X_j - \delta_j^2 < C < +\infty$

Тогда $$\frac{1}{n} \sum_{j=1}^n X_j \xrightarrow{\pr} \frac{1}{n}\sum_{j=1}^n m_j$$
