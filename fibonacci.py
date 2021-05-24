import math,numpy as np
def fib(n,hashmap=dict()):
    if n == 0 :
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)
       
def fab(n):
    val = np.matrix([[2,1],[1,1]])**((n)//2)
    
    obj = np.array(val)

    if n & 1 :
        return obj[0][0]
    else:
        return obj[0][1]

def fib_series(n):
    series = []
    for i in range(n+1):
        series += [fab(i)]
    
    return series

    
    


print(fib(10))
print(fab(10))
print(fib_series(10))