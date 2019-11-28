# encoding: utf-8
import sys
import time
start_time = time.time()

def recur_factorial(n):
   if n == 1:
       return n
   else:
       return n * recur_factorial(n-1)

n = int(sys.argv[1])
print(recur_factorial(n))

print("")
print("--- Time")
print("--- %s seconds" % (time.time() - start_time))
