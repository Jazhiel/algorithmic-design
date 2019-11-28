# encoding: utf-8
import sys
import time
start_time = time.time()

def returnChange(change, denominations):
    denominationsCount = len(denominations)
    # makes a list size of length denominations filled with 0
    toGiveBack = [0] * denominationsCount


    # goes backwards through denominations list
    # and also keeps track of the counter, pos.
    for pos, coin in enumerate(reversed(denominations)):
        # while we can still use coin, use it until we can't
        while coin <= change:
            change -= coin
            toGiveBack[denominationsCount - pos - 1] += 1
    return(toGiveBack)


change = int(sys.argv[1])
denominations = [1, 2, 5, 10, 20, 50, 100]
# 100p is £1

print(returnChange(change, denominations))
# returns [0, 0, 0, 1, 1, 0, 0]
# 1x 10p, 1x 20p
print("")
print("--- Time")
print("--- %s seconds" % (time.time() - start_time))
