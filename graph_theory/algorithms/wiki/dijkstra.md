### Dijkstra's Algorithm

Input: a positively weigted diraph $(D, w)$ with a specified vertex $r$<br>
Output: an $r$-branching in $D$ with predecessor function $p$, and a function $l : V \rightarrow R^+$ such that $l(v)=d_D(r,v) \forall v \in V$
1. set $p(v) := \emptyset, v \in V, l(r) := 0$ and $l(v) := \infty, v \in V$ \ $\{r\}$
2. **while** there is an uncoloured vertex with $l(u) < \infty$ **do**
3. &nbsp;&nbsp;&nbsp;choose such a vertex $u$ for which $l(u)$ is minimum
4. &nbsp;&nbsp;&nbsp;colour $u$ black
5. &nbsp;&nbsp;&nbsp;**for** each uncoloured outneighbour $v$ of $u$ with $l(v) > l(u) + w(u, v)$ **do**
6. &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;replace $p(v)$ by $u$ and $l(v)$ by $l(u) + w(u, v)$
7. &nbsp;&nbsp;&nbsp;**end for**
8. **end while**
9. return $(p, l)$