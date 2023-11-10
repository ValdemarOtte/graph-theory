# Graf teori
Samling af algoritmer fra kurset [Grafteori I](https://kursuskatalog.au.dk/da/course/121043/Grafteori-1) 

## Algoritmer
- [Breadth First Search](#Breadth-First-Search)
- [Deep First Search](#Deep-First-Search)
- [Jarník-Prim Algorithm](#Jarník-Prim-Algorithm)

### Breadth First Search
```
Input: a connevted graph G(r)
Output: an r-tree T in G with predecessor function p, a level function l such that l(v)=d_g(r,v) for all v in V, and a time function t
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
11.         set p(y) := x, l(x) := l(x) + 1 and t(y) := i
12.         append y to Q
13.     else
14.         remove x from Q
15.     end if
16. end while
17. return (p, l, t)
```

### Deep First Search
```
Input: a connevted graph G(r)
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

### Jarník-Prim Algorithm
bla
