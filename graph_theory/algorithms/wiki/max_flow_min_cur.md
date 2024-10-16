### Max-Flow Min-cut

Input: a network $N := N(x, y)$ and a feasible flow $f$ in $N$<br>
Output: a maximum flow $f$ and a minimum cut $\partial^+(X)$ in $N$
 1. set $X := {x}, p(v) := \emptyset, v \in V$
 2. **while** there is either an f-unsaturated arc $a:=(u,v)$ or an f-positive arc $a:=(v, u)$ with $u\in X$ and $v\in V$ \ $X$ **do**
 3. &nbsp;&nbsp;&nbsp;replace $X$ by $X\cup\{v\}$
 4. &nbsp;&nbsp;&nbsp;replace $p(v)$ by $u$
 5. **end while**
 6. **if** $y\in X$ **then**
 7.  compute $\varepsilon(P):=\min\{\varepsilon(a) : a\in A(P)\}$, where $P$ is the $xy$-path in the tree whose predecessor function is $p$
 8. &nbsp;&nbsp;&nbsp;for each forward arc $a$ of $P$, replace $f(a)$ by $f(a) + \varepsilon(P)$
 9. &nbsp;&nbsp;&nbsp;for each reverse arc $a$ of $P$, replace $f(a)$ by $f(a) - \varepsilon(P)$
10. &nbsp;&nbsp;&nbsp;return to $1$
11. **end if**
12. return $(f, \partial^+(X))$