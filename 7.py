
'''

the key is just to use pre-computed number instead of 2**32
'''


class Solution:
    def reverse(self, x: int) -> int:
        result=0
        negative=False
        if x<0:
            x=-x
            negative=True
        while abs(x)>0:
            result=result*10+x%10
            x=(int) (x/10)
        if (result < -2147483648) or (2147483647 < result):
            return 0
        if negative:return -result
        else:
            return result
            
            