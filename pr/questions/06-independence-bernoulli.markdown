---
title: "Независимость испытаний. Схема Бернулли"
---
## Независимость испытаний. Схема Бернулли ##

### Def. (Bernoulli trial) ###
Эксперимент (случайная величина $X$),
исходом которого является либо успех с вероятностью $p$,
либо неудача с вероятностью $(1-p)$, называется *bernoulli trial*.
При этом говорят, что r.v. $X$ *распределена по Бернулли с параметром $p$* и пишут $X\sim\Bern(p)$

### Пример ###
Любому событию $A$ соответствует индикатор $I_A$.
Очевидно, он является \newline
\hbox{r.v. распределённой по Бернулли с параметром $p=\pr A$}:
$I_A\sim\Bern(\pr A)$.
Обратно, любая случайная величина с распределением Бернулли является индикатором
некоторого события.

### Def. (Схема Бернулли) ###
Пусть теперь эксперимент состоит в последовательном проведении
$n$ экспериментов Бернулли с одинаковой вероятностью успеха $p$,
а результат записывается в виде строки $(a_1, a_2, \ldots, a_n), a_i\in \{0,1\}$.

Пространство $\Omega$ элементарных событий имеет вид
$\Omega = \{ \omega = (a_1, a_2, \ldots, a_n), a_i\in \{0,1\} \}$.
Каждому исходу $\omega$ соответствует "вес"
${p_\omega = p^k (1-p)^{n-k}}$
$k=\sum_j a_j$ --- число "успехов", $n-k$ --- число "неудач".

Рассмотрим событие, состоящее в получении $k$ "успехов"
и r.v. $X$ --- число "успехов".
Вес каждого такого события --- ${p_\omega = p^k (1-p)^{n-k}}$.
Всего различных таких событий --- $n \choose k$.
Вероятность этого события --- $\pr\{X=k\} = {n \choose k} {p_\omega = p^k (1-p)^{n-k}}$.
Говорят, что рассматриваемая случайная величина $X$
имеет *биномиальное распределение* $\{ \pr A_0, \pr A_2, \ldots, \pr A_n \}$,
задаваемое функций масс $k \mapsto \pr\{X=k\}$.


### Формализация ###
${\Omega = \{ \omega = (a_1, a_2, \ldots, a_n), a_i\in \{0,1\} \}}$.\newline
${\SigmaField = S(\Omega) = \{ A : A\subset\Omega\}}$.\newline
${\pr(\{\omega\}) := p_\omega = p^k (1-p)^{n-k}}$. Отсюда в виду аддитивности $\pr$: \newline
${\pr(A) = \sum_{\omega\in A} \pr \{\omega\} = \sum_{\omega\in A} p_{\omega}}$

Рассмотрим события $A_k = \{\omega: a_k = 1\}$, $\bar A_k = \{\omega: a_k = 0\}$.\newline
Введём $\sigma$-алгебры $\SigmaField_k = \{ A_k, \bar A_k, \emptyset, \Omega \}$.

Ясно, что $\pr A_k = p$, $\pr \bar A_k = 1-p$ и,
при $i\neq j$,\newline
$\pr A_i A_j = \pr A_i \pr A_j = p^2$,\newline
$\pr A_i \bar A_j = \pr A_i \pr\bar A_j = pq$,\newline
$\pr \bar A_i \bar A_j = \pr\bar A_i \pr\bar A_j = q^2$.

Аналогично, $A_1, A_2, \ldots, A_n$ --- независимы.
Отсюда, алгебры $\SigmaField_1, \ldots \SigmaField_n$ --- независимы.

Вероятностное пространство $(\Omega,\SigmaField,\pr)$
имеет *структуру прямого произведения вероятностных пространств*:

Если даны вероятностные пространства
$(\Omega_1, \SigmaField_1, \pr_1), \ldots (\Omega_n, \SigmaField_n, \pr_n)$.
Их прямое произведение --- вероятностное пространство $(\Omega, \SigmaField, \pr)$,
в котором

1. $\Omega = \prod_{j=1}^n \Omega_j = \{ \omega=(\omega_1,\ldots,\omega_n): \omega_i\in\Omega_i, i=\overline{1,n} \}$
2. $\SigmaField = \prod_{j=1}^n \SigmaField_j$ --- минимальная $\sigma$-алгебра, порождённая цилиндрами $\prod_{j=1}^n A_j, A_j\in\SigmaField_j$.
3. $\pr = \prod_{j=1}^n \pr_j$

Возвращаясь к нашему частному случаю,

  $$\begin{aligned}
  & \Omega_j = \{0,1\} \\
  & \SigmaField_j=\{ \{0\}, \{1\}, \emptyset, \Omega_j \} \\
  & \pr\{1\} = p \\
  & \pr\{0\} = 1-p \\
  & \Omega = \{ \omega=(a_1,\ldots,a_n): a_i\in\Omega_j, j=\overline{1,n} \} \\
  & \SigmaField = \{ A = A_1\times A_2\times \ldots\times A_n : A_j\in\SigmaField_j \} \\
  & p_\omega = p_1(a_1) p_2(a_2) \ldots p_n(a_n) \\
  & \pr A = \sum\limits_{a_j\in\SigmaField_j, j=\overline{1,n}} p_1(a_1)\ldots p_n(a_n) \\
  & \pr\{\omega\} = p^k (1-p)^{n-k}
  \end{aligned}$$

Это и описывает схему Бернулли.
