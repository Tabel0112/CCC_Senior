#!/usr/bin/env python
# ### calculate how many ways to form a number by using 4 and 5
from collections import Counter
def checkDuplicate(counters, compare):
    for cunter in counters:
        if not bool(cunter - compare):
            return False
    return True

def getWays(target):
    dplist = [[]] * (max(7, target + 2))
    dplist[4+1] =  [Counter([4])]
    dplist[5+1] = [Counter([5])]
    if target < 6:
        return len(dplist[target+1])
    for i in range(6, target+2):
        if dplist[i-4] != None:
            for count in dplist[i-4]:
                newCounter = Counter([4])
                newCounter.update(count)
                if dplist[i] == None:
                    dplist[i] = [newCounter]
                else:
                    if checkDuplicate(dplist[i], newCounter):
                        dplist[i].append(newCounter)
        if dplist[i-5] != None:
            for count in dplist[i-5]:
                newCounter = Counter([5])
                newCounter.update(count)
                if dplist[i] == None:
                    dplist[i] = [newCounter]
                else: 
                    if checkDuplicate(dplist[i], newCounter):
                        dplist[i].append(newCounter)
    return len(dplist[target+1])

target = int(input())
print(getWays(target))
