# CMPS 2200 Reciation 5
## Answers

**Name:**Jordan Sztejman


Place all written answers from `recitation-05.md` here for easier grading.







- **1b.**
Random/Shuffled data
|      n |   qsort-fixed-pivot |   qsort-random-pivot |   timsort |
|--------|---------------------|----------------------|-----------|
|    100 |               0.095 |                0.110 |     0.005 |
|    200 |               0.179 |                0.227 |     0.011 |
|    500 |               0.485 |                0.608 |     0.027 |
|   1000 |               1.198 |                1.314 |     0.060 |
|   2000 |               2.337 |                2.489 |     0.125 |
|   5000 |               5.960 |                7.028 |     0.359 |
|  10000 |              12.550 |               15.396 |     0.766 |
|  20000 |              26.908 |               31.235 |     1.654 |
|  50000 |              76.651 |               83.635 |     4.607 |
| 100000 |             157.080 |              179.770 |     9.785 |

Sorted data
|     n |   qsort-fixed-pivot |   qsort-random-pivot |   timsort |
|-------|---------------------|----------------------|-----------|
|   100 |               0.362 |                0.117 |     0.001 |
|   200 |               1.123 |                0.187 |     0.002 |
|   500 |               6.728 |                0.526 |     0.003 |
|  1000 |             inf     |                1.237 |     0.005 |
|  2000 |             inf     |                2.454 |     0.009 |
|  5000 |             inf     |                6.692 |     0.028 |
| 10000 |             inf     |               13.857 |     0.050 |

From this data,  the run times for qsort with a random pivot for both random and sorted data produced a growth rate of O(n log(n)).  Timsort demonstrated O(n log n) behavior on random data but achieved near O(n) performance on sorted data.  Qsort with fixed pivot showed O(n^2) growth rate for sorted data, shown when it reaches "inf" or when it reaches the pyhton recursion maximum. It also produces a O(n log(n)) with shuffled data. 

The change from random to sorted data makes timsort almost 200 times faster. While qsort random maintains aorund the same time complexity. On the other hand, qsort fixed pivot has a much worse time complexity and even reaches the recursion limit.

- **1c.**

Timsort has a worst case time complexity of O(n (log(n))) for random inputs and for sorted inputs it is O(n). For comparison, timsort with a n value of 500 had a time of .003 milliseconds compared to that of the qsort randoms time of .526 milliseconds and 6.728 milliseconds for qsort fixed for the sorted data. This represents a 175x improvement compared to qsort random and over a 2000x improvement for qsort fixed. When we compare it for the shuffled data with a n value of 100000, timsort had a time of 9.785 milliseconds compared to qsort randoms 179.77 and qsort fixed 157.08 milliseconds. It is about 15x faster than either of these sorting algorithms. 