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
 1. set i := 1 and Q := emptyset
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
bla

### Jarník-Prim Algorithm
bla
