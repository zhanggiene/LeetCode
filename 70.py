class Solution:
    def climbStairs(self, n: int) -> int:
        dictionary={0:0,1:1,2:2}
        def climbStairsRecursion(n):
            if n in dictionary:
                return dictionary[n]
            else:
                result=climbStairsRecursion(n-1)+climbStairsRecursion(n-2)
                dictionary[n]=result
                return result
        return climbStairsRecursion(n)
        