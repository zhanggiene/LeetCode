

import math
test = math.inf
def find(L,number):
    '''
    assumption 1: all the numbers in L and number  are bigger than 0 

    2 :the solution must exist, [1,2,3] -> 100 maximum recursion depth exceeded in comparison as it as no solution and cannot meet the base case
    if the recursion depth exceed the computer maximum recursion depth,then computer will give warning. 

    limit:
    it cannot compute when the list is very large. 
    
    for example from sys.getrecursionlimit() , my computer allow 1000 function recursion, unless i change the recursion limit with sys.setrecursionlimit.
    the solution for find([i for i in range(999)],498501)) exist, which is [1,2,3,4..........998], but the computer is unable to find the solution due to maximum recrusion 
    it is able to compute find([i for i in range(999)],498500)) as it does not exceed maximum recursion imposed by the system. 





    '''
    if number in L:
        return [L.index(number)]
    else:
        maxNumber=max(L)
        maxIndex=L.index(maxNumber)
        L[maxIndex]=-math.inf
        if L.count(0)!=len(L) and min(L)<=number-maxNumber:
            return sorted([maxIndex]+find(L,number-maxNumber))
        else: 
            return find(L,number)


#import sys
#print(sys.getrecursionlimit())

#print(find([i for i in range(999)],498500))
#print(find([i for i in range(999)],498500))
print(find([1,1,2,2,5],4))