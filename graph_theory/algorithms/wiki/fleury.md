### Fleury's Algorithm

Input: a connected even graph $G$ and a specified vertex $u$ of $G$<br>
Output: An Euler tour $W$ of  starting (and ending) at $u$
1. Set $W := u, x := u, F := G$
2. **While** $\partial_F(x)$ is not $\emptyset$ **do**
3. &nbsp;&nbsp;&nbsp;choose an edge $e:= xy \in \partial_F(x)$, where $e$ is not a cut edge of $F$ unless there is no alternative
4. &nbsp;&nbsp;&nbsp;replace $uWx$ by $uWxey$, $x$ by $y$, and $F$ by $F$ \ $e$
5. **end while**
6. return $W$