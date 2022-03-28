## Time Complexity

Performance Analysis of algorithm considers the resources used by the system such as space occupied by the algorithm and the time required to execute the algorithm.

Performance Analysis of Algorithm is an important part of a computational theory, which provides theoretical estimates for the resources needed by any algorithm.


** Let n be an integer variable which tends to infinity and let x be a continuous variable tending to some limit. Also, let phi(n) or phi(x) be a positive function and f(n) or f(x) any function. Then Hardy and Wright (1979) define

1. f=O(phi) to mean that |f|<Aphi for some constant A and all values of n and x,

2. f=o(phi) to mean that f/phi->0,

3. f∼phi to mean that f/phi->1,

4. f≺phi to mean the same as f=o(phi),

5. f≻phi to mean f/phi->infty, and

6. f=phi to mean A_1phi<f<A_2phi for some positive constants A_1 and A_2.

f=o(phi) implies and is stronger than f=O(phi).

The term Landau symbols is sometimes used to refer the big-O notation O(x) and little-O notation o(x). In general, O(x) and o(x) are read as "is of order x."

If f=phi, then f and phi are said to be of the same order of magnitude (Hardy and Wright 1979, p. 7).

If f∼g, or equivalently f=phi+o(phi) or f=phi(1+o(1)), then f and phi are said to be asymptotically equivalent (Hardy and Wright 1979, p. 8). **
