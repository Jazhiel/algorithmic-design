# encoding: utf-8
import sys
import time
start_time = time.time()

def F(n):
  if n == 0 or n == 1:
    return n
  else:
    return F(n-1)+F(n-2)

param = int(sys.argv[1])
print(F(param))

print("")
print("--- Time")
print("--- %s seconds" % (time.time() - start_time))
