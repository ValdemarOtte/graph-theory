### Bellman-Form

Input: a connected graph $G(r)$<br>
Output: an $r$-tree $T$ in $G$ with predecessor function $p$, a level function $l$ such that $l(v)=d_g(r,v) \forall v \in V$, and a time function $t$
 1. set $l(v) := \infty, p(v) := \emptyset, v in V$
 2. remove $r$ from $Q$
 3. set $l(r) := 0$
 4. **while** $Q$ is not $\emptyset$ **do**
 5. &nbsp;&nbsp;&nbsp;remove the first element $y$ from $Q$
 6. &nbsp;&nbsp;&nbsp;**for** all $x \in N^-(y)$ from $Q$
 7. &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**if** $l(x) + w(x, y) < l(y)$ **then**
 8. &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;replace $l(y)$ by $l(x) + w(x, y)$ and $p(y)$ by $x$
 9. &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**end if**
10. &nbsp;&nbsp;&nbsp;**end for**
11. **end while**
12. return $(l, p)$