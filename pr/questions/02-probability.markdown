---
title: "Вероятность и её свойства"
---
## Вероятность и её свойства ##


### Def. (Функция множеств)
Функцией множеств называется функция вида $\phi : S(\Omega)\mapsto\KK$,
где $\KK$ --- числовое поле, быть может расширенное специальным числом $\infty$.
Далее будут рассматриваться функции множества вида
$\phi : S(\Omega)\mapsto\RR$ или $\phi : S(\Omega)\mapsto [-\infty,+\infty]$

### Def. (Аддитивность) ###
Фукция множеств $\phi : S(\Omega)\mapsto\KK$ называется аддитивной,
если для любого конечного числа
взаимно-непересекающихся множеств $A_{1}, \ldots, A_n \in \Omega$ выполняется равенство
$$ \sum_{j=1}^n \phi A_j = \phi \sum_{j=1}^n A_j $$

### Def. ($\sigma$-аддитивность) ###
Функция множеств $\phi : S(\Omega)\mapsto\KK$ назвыается $\sigma$-аддитивной,
если для любого не более чем счётного числа взаимно-непересекающихся множеств $A_{j}, j\in J$
выполняется равенство
$$ \sum_{j\in J} \phi A_{j} = \phi \sum_{j\in J} A_{j} $$
Где сумма по $j\in J$ в левой части равенства понимается в смысле
суммы либо абсолютно сходящегося,
либо расходящегося к $+\infty$ числового ряда.
Сумма в правой части представляет собой либо сумму конечного числа взаимно-непересекающихся множеств,
либо $\limsup_n \sum_{j=j_1}^{j_n} A_j$

### Def. (Мера) ###
*Мерой* называется $\sigma$-аддитивная неотрицательная функция множеств \hbox{$\mu : \SigmaField\mapsto [0,+\infty]$},
определённая на $\sigma$-алгебре $\SigmaField$

### Def. (Вероятность) ###
Если мера $\pr$ такова, что $\pr\Omega = 1$, то она называется *нормированной* мерой, или *вероятностью*.
То есть $pr$ --- вероятность, если:

1.  $\pr  : \SigmaField\mapsto [0,1]$  (неотрицательность)
2.  $\pr A = 1$                         (нормированность)
2.  $\sum_j \pr A_j = \pr \sum_j A_j$   ($\sigma$-аддитивность)

### Def. (Измеримое пространство) ###
Измеримым пространством называется пара $(\Omega, \SigmaField)$, состоящая из

* пространства $\Omega$
* $\sigma$-алгебры $\SigmaField$ измеримых множеств из $\Omega$

### Def. (Пространство с вероятностью) ###
Пространством с вероятностью называется тройка $(\Omega, \SigmaField, \pr)$, состоящая из

* пространства $\Omega$
* $\sigma$-алгебры $\SigmaField$ измеримых множеств (событий) из $\Omega$
* вероятности $\pr : \SigmaField\mapsto [0,1]$

### Свойства $\sigma$-аддитивных функций, меры и вероятности ###
Пусть дано измеримое пространство $(\Omega, \SigmaField)$.

* Если некоторая аддитивная функция $\phi$ множеств конечна хотя бы на одном множестве $A\in \SigmaField$,
  то $\phi\emptyset = 0$, так как $\mu A = \mu (A+\emptyset) = \mu A + \mu\emptyset$
Пусть дана некоторая мера $\mu : \SigmaField \mapsto [0,+\infty]$, конечная хотя бы на одном множестве $A$.
Тогда:

* $\mu\emptyset = 0$
  так как мера $\sigma$-аддитивна, а по условию ещё и конечна
* $\mu A\cup B = \mu A + \mu B - \mu AB$
  так как в виду аддитивности и очевидных разбиений множеств $A$ и $A\cup B$
    $$\begin{aligned}
      & \mu A       = \mu AB +  \mu A B^\complement \\
      & \mu A\cup B = \mu B  +  \mu A B^\complement \\
      & \mu A - \mu A\cup B = \mu AB - \mu B \\
      & \mu A + \mu B - \mu AB = \mu A\cup B
    \end{aligned}$$
* $A_{1}\subset A_{2} \subset\ldots \implies \mu A_{1} \leq \mu A_{2} \leq \ldots$ (монотонность)
    $$\begin{aligned}
      & A_2     &&= A_1 + A_2 A_1^\complement \\
      & \mu A_2 &&= \mu A_1 + \mu A_2 A_1^\complement \\
      & \mu     &&\geq 0 \\
      & \mu A_2 &&\geq \mu A_1 \\
      & A_n     &&= A_1 + A_2 A_1^\complement + A_3 A_2^\complement A_1^\complement + \ldots \\
      & Далее по индукции
    \end{aligned}$$
* $\mu \cup A_j \leq \sum \mu A_j$ (суб-аддитивность)
    $$\begin{aligned}
      & \cup_{j=1}^\infty A_j = A_1 + A_2 A_1^\complement + \ldots \\
      & \begin{aligned}
        & A_2 A_1^\complement \subset A_2 \\
        & A_3 A_2^\complement A_1^\complement \subset A_3\\
        & \ldots
        \end{aligned} \\
      & \begin{aligned}
          & \mu A_2 \leq \mu (A_2 A_1^\complement) \\
          & \mu A_n \leq \mu (A_{n-1} A_{n-2} \ldots A_1)
        \end{aligned}
      \end{aligned}$$
* $A \subset B \implies \mu (B - A) = \mu B - \mu A$
     
     $A (B-A) = \emptyset$, т.е. $A$ и $B-A$ не пересекаются, а значит имеет место аддитивность:
     $$\begin{aligned}
       & A \cup (B-A) = A + (B-A) \\
       & \mu A\cup (B-A) = \mu A + \mu (B-A) \\
       & \mu (B-A) = \mu A - \mu B
     \end{aligned}$$

Если же данная мера --- *вероятность* $\pr$, то

1.  $\pr A = 1 - \pr A^\complement$
    
    $1 = \pr \Omega = \pr A + \pr A^\complement$
