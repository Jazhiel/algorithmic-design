# encoding: utf-8
import sys
import time
start_time = time.time()

def recur_factorial(n):
    retorno = 1
    for number in range(1, n + 1):
        retorno *= number;

    return(retorno)

n = int(sys.argv[1])
print(recur_factorial(n))

print("")
print("--- Time")
print("--- %s seconds" % (time.time() - start_time))
