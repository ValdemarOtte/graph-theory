# Graf teori
Samling af algoritmer fra kurset [Grafteori I](https://kursuskatalog.au.dk/da/course/121043/Grafteori-1) 

## Algoritmer
- [Breadth First Search](#Breadth-First-Search)
- [Deep First Search](#Deep-First-Search)
- [Dijkstra's Algorithm](#Dijkstra's-Algorithm)
- [Jarník-Prim Algorithm](#Jarník-Prim-Algorithm)

### Breadth First Search
```
Input: a connected graph G(r)
Output: an r-tree T in G with predecessor function p, a level function l such
        that l(v)=d_g(r,v) for all v in V, and a time function t
 1. set i := 0 and Q := emptyset
 2. increment i by 1
 3. colour r black
 4. set l(r) := 0 and t(r) := i
 5. append r to Q
 6. while Q is nonempty do
 7.     consider the head x of Q
 8.     if x has an uncoloured neighbour y then
 9.         increment i by 1
10.         colour y black
11.         set p(y) := x, l(x) := l(y) + 1 and t(y) := i
12.         append y to Q
13.     else
14.         remove x from Q
15.     end if
16. end while
17. return (p, l, t)
```

### Deep First Search
```
Input: a connected graph G(r)
Output: a rooted spanning tree of G with predecessor function p, and two time functions f and l
 1. set i := 0 and S := emptyset
 2. choose any vertex r (as root)
 3. increment i by 1
 4. colour r black
 5. set f(r) := r
 6. add r to S
 7. while S is nonempty do
 8.     consider the top vertex x of S
 9.     increment i by 1
10.     if x has an uncoloured neighbour y then
11.         colour y black
12.         set p(y) := x and f(y) := i
13.         add y to the top of S
14.     else
15.         set l(x) := i
16.         remove x from S
17.     end if
18. end while
19. return (p, f, l)
```

### Dijkstra's Algorithm
```
Input: a positively weited diraph (D, w) with a specified vertex r
Output: an r-branching in D wit predecessor function p,
        and a function l : V -> R^+ such that l(v)=d_D(r,v) for all v in V
1. set p(v) := emptyset, v in V, l(r) := 0 and l(v) := inf, v in V\{r}
2. while there is an uncoloured vertexu wit l(u) < inf do
3.     choose suc a vertex u for which l(u) is minimum
4.     colour u black
5.     for each uncoloured outneighbour v of u withh l(v) > l(v) + w(u, v) do
6.         replace p(v) by u and l(v) by l(u) + w(u, v)
7.     end for
8. end while
9. return (p, l)
```

### Jarník-Prim Algorithm
```
Input: a weighted connected graph (G, W)
Output: an optimal tree T of G with predecessor function p, and its weight w(T)
 1. set p(v) := emptyset and c(v) := infty, v in V, and w(T) := 0
 2. choose any verter r (as root)
 3. replace c(r) by 0
 4. while there is an uncoloured vertex do
 5.     choose such a vertex u of minimum cost c(u)
 6.     colour u black
 7.     for each uncoloured vertex v such that w(ux) < c(v) do
 8.         replace p(v) by u and c(v) by w(uv)
 9.         replace w(T) by w(T) + c(u)
10.     end for
11. end while
12. return (p, w(T))
```
