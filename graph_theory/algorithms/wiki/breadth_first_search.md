### Breadth First Search

Input: a connected graph $G(r)$ <br>
Output: an $r$-tree $T$ in $G$ with predecessor function $p$, a level function $l$ such that $l(v)=d_g(r,v) \forall v \in V$, and a time function $t$
 1. set $i := 0$ and $Q := \emptyset$
 2. increment $i$ by $1$
 3. colour $r$ black
 4. set $l(r) := 0$ and $t(r) := i$
 5. append $r$ to $Q$
 6. **while** $Q$ is not $\emptyset$ **do**
 7. &nbsp;&nbsp;&nbsp;consider the head $x$ of $Q$
 8. &nbsp;&nbsp;&nbsp;**if** $x$ has an uncoloured neighbour $y$ **then**
 9. &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;increment $i$ by $1$
10. &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;colour $y$ black
11. &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;set $p(y) := x, l(x) := l(y) + 1$ and $t(y) := i$
12. &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;append $y$ to $Q$
13. &nbsp;&nbsp;&nbsp;**else**
14. &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;remove $x$ from $Q$
15. &nbsp;&nbsp;&nbsp;**end if**
16. **end while**
17. return $(p, l, t)$