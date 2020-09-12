class Solution:
    def mySqrt(self, x: int) -> int:
        start=0
        end=x
        result=x//2
        if x==1:
            return 1
        while not(result*result<=x and (result+1)*(result+1)>x):
            #print(result)
            if result*result>x:
                end=result
                result=(start+end)//2
            if result*result<x:
                start=result
                result=(start+end)//2
        return result
                
        