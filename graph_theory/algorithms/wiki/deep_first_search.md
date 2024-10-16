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