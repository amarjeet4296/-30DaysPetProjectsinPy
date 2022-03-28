## Time Complexity

Performance Analysis of algorithm considers the resources used by the system such as space occupied by the algorithm and the time required to execute the algorithm.

Performance Analysis of Algorithm is an important part of a computational theory, which provides theoretical estimates for the resources needed by any algorithm.


**There is no single data structure that offers optimal performance in every case. In order to choose the best structure for a particular task, we need to be able to judge how long a particular solution will take to run. Or, more accurately, you need to be able to judge how long two solutions will take to run, and choose the better of the two. We don't need to know how many minutes and seconds they will take, but we do need some way to compare algorithms against one another**

The analysis of algorithms is the estimation of the amount of resources as time taken to execute an algorithm and the memory storage required by an algorithm.

The running time of an algorithm is defines as a function with the time complexity and the Space complexity. These estimates provide the directions of search for efficient algorithms. 

Asymptotic complexity is a way of expressing the main component of the cost of an algorithm

Theoretical analysis of algorithms generally includes estimation of their complexity in the asymptotic notation[1],which deals with the large input. O(big O),theta and omega notations are used. For instance, binary search takes O(log(n)), the logarithmic time. Asymptotic estimates are used because different algorithms which are intended to perform the same functionality may differ in terms of their complexity.


When n is arbitrarily big, growth of functions highly depends on the dominant term in the function:
- n+5 - O(n)

- n+1000000 - O(n)
 
- n^2+n+5 - O(n^2)

- n^2+1000000n+5 - - O(n^2)

- 2n^2 + n3 - - O(n^3)

- n + log n + n log n - - O(nlogn)

- n + (log n)5 + n log n - - O(nlogn)

- 2^n + n^2 - O(2^n)

- 2^n + n^200 - O(2^n)

## Example

def max(list):<br />
max = list[0] <br />
 for i in range(len(list)):<br />
 if max < list[i]: max = list[i]<br />
 return max<br />

Exact counting:<br />
Count the number of comparisons:<br />
- Assume len(list) = n<br />
- The max < list[i] comparison is made n times.<br />
- Each time i is incremented, a test is made to see if i < len(list).<br />
- One last comparison determines that i ≥ len(list).<br />
- Exactly 2n + 1 comparisons are made.<br />
- Consider the dominant term (as well as ignoring the coefficient)<br />
- Hence, the time complexity of the max algorithm is O(n).<br />
