# Graf teori
Samling af algoritmer fra kurset [Grafteori I](https://kursuskatalog.au.dk/da/course/121043/Grafteori-1) 

## Algoritmer
- [Breadth First Search](#Breadth-First-Search)
- [Bellman-Form](#Bellman-Form)
- [Deep First Search](#Deep-First-Search)
- [Dijkstra's Algorithm](#Dijkstras-Algorithm)
- [Fleury](#Fleury)
- [Jarník-Prim Algorithm](#Jarník-Prim-Algorithm)
- [Max-Flow Min-cut](#Max-Flow-Min-Cut)

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



### Deep First Search

Input: a connected graph $G(r)$<br>
Output: a rooted spanning tree of $G$ with predecessor function $p$, and two time functions $f$ and $l$
 1. set $i := 0$ and $S := \emptyset$
 2. choose any vertex $r$ (as root)
 3. increment $i$ by $1$
 4. colour $r$ black
 5. set $f(r) := r$
 6. add $r$ to $S$
 7. **while** $S$ is not $\emptyset$ **do**
 8. &nbsp;&nbsp;&nbsp;consider the top vertex $x$ of $S$
 9. &nbsp;&nbsp;&nbsp;increment $i$ by $1$
10. &nbsp;&nbsp;&nbsp;**if** $x$ has an uncoloured neighbour $y$ **then**
11. &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;colour $y$ black
12. &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;set $p(y) := x$ and $f(y) := i$
13. &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;add $y$ to the top of $S$
14. &nbsp;&nbsp;&nbsp;**else**
15. &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;set $l(x) := i$
16. &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;remove $x$ from $S$
17. &nbsp;&nbsp;&nbsp;**end if**
18. **end while**
19. return $(p, f, l)$


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


### Fleury's Algorithm
Input: a connected even graph $G$ and a specified vertex $u$ of $G$<br>
Output: An Euler tour $W$ of  starting (and ending) at $u$
1. Set $W := u, x := u, F := G$
2. **While** $\partial_F(x)$ is not $\emptyset$ **do**
3. &nbsp;&nbsp;&nbsp;choose an edge $e:= xy \in \partial_F(x)$, where $e$ is not a cut edge of $F$ unless there is no alternative
4. &nbsp;&nbsp;&nbsp;replace $uWx$ by $uWxey$, $x$ by $y$, and $F$ by $F$ \ $e$
5. **end while**
6. return $W$


### Jarník-Prim Algorithm
Input: a weighted connected graph $(G, W)$<br>
Output: an optimal tree $T$ of $G$ with predecessor function $p$, and its weight $w(T)$
 1. set $p(v):=\emptyset$ and $c(v):=\infty$, $v\in V$, and $w(T):=0$
 2. choose any verter $r$ (as root)
 3. replace $c(r)$ by $0$
 4. **while** there is an uncoloured vertex **do**
 5. &nbsp;&nbsp;&nbsp;choose such a vertex $u$ of minimum cost $c(u)$
 6. &nbsp;&nbsp;&nbsp;colour $u$ black
 7. &nbsp;&nbsp;&nbsp;**for** each uncoloured vertex $v$ such that $w(ux) < c(v)$ **do**
 8. &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;replace $p(v)$ by $u$ and $c(v)$ by $w(uv)$
 9. &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;replace $w(T)$ by $w(T) + c(u)$
10. &nbsp;&nbsp;&nbsp;**end for**
11. **end while**
12. return $(p, w(T))$


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
