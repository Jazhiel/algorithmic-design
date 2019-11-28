# encoding: utf-8
import sys
import time
start_time = time.time()

def fibonacciVal(n):
    memo = [0] * (n+1)
    memo[0], memo[1] = 0, 1
    for i in range(2, n+1):
        memo[i] = memo[i-1] + memo[i-2]
    return memo[n]

param = int(sys.argv[1])
print(fibonacciVal(param))

print("")
print("--- Time")
print("--- %s seconds" % (time.time() - start_time))
