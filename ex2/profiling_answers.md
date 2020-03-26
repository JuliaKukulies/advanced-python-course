# Profiling 



## 3a) matmult.py 

- most time: line 43, the function which contains the nested loop, where the matrices are multiplied and the empty list is filled with the new values 
- most memory: same as for the time, but the memory taken by the different matrices is about the same (ca. 40 MB) 



## 3b) euler72.py 

- most time: line 53, factors = factorize(n,primes) - almost 90% of the time is used for this function 
- most memory: line 53, factors = factorize(n,primes) - this function takes most of the memory



## 3c) optimized matmult.py 


- see script *matmult_improved.py*
- the main change is the new function **multiply_matrices**, which now takes much less time (ca. 1/3 of the time before)
- I also used list comprehension to create the random matrices (instead of the append() function), but this improvement saves only space in the code and not much time or memory 
- best performance: 


