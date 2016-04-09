---
title: "Независимые случайные величины. Их функции распределения и плотности вероятности"
---
## Независимые случайные величины. Их функции распределения и плотности вероятности ##

### Def. (Независимые случайные величины) ###
Случайные величины $X_t, t\in T$ *независимы*, если
для каждого конечного класса $(S_{t_1},\ldots,S_{t_n})$ борелевских множеств в $\RR$

$$\pr \cap_{k=1}^n [X_{t_k} \in S_{t_k}] = \prod_{k=1}^n \pr [X_{t_k} \in S_{t_k}]$$


### Lemma (О умножениях) ###
Если $X_1, \ldots, X_n$ независимы, то
$$\E \prod_{k=1}^n X_k = \prod_k \E X_k$$

Докажем для $n=2$.
Пусть сначала $X, Y$ --- неотрицательные простые (или элементарные):
$X=\sum_j x_j I_{A_j}$,
$Y = \sum_k y_k I_{B_k}$.
Без ограничения будем считать как $x_j$, так и $y_k$ различными, положив
$A_j = [X=x_j]$, $B_k = [Y=y_k]$.

$$ \E XY = \E \sum_{jk} x_j y_k I_{A_j B_k} = \sum_{jk} x_j y_k \pr A_j \pr B_k = \sum_j x_j \pr A_j \sum_k y_k \pr B_k = \E X \E Y $$

Общий случай: (TODO; см. Лоэв, Теория вероятностей, ИИЛ, 1962, с. 240)

### Функция распределения ###
$X = (X_1, \ldots, X_n)$
$$F_X(x_1, \ldots, x_n) = \pr[ X_1\leq x_1, \ldots, X_n\leq x_n = \pr [X_1\leq x_1]\ldots\pr [X_n\leq x_n] = F_{X_1}(x_1) \cdots F_{X_n}(x_n)$$

### Плотность распределения ###
$$f_X = \frac{\partial^n F}{\partial x} =
        \frac{\partial^n F}{\partial x_1 \cdots \partial x_n} = 
        \frac{\partial F}{\partial x_1} \cdots \frac{\partial F}{\partial x_n} =
        f_{X_1} \cdots f_{X_n} $$
