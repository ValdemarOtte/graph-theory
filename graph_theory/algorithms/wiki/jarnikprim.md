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