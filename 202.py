
#controled recursion, other wise u wont know if it will fail

class Solution:
    def isHappy(self, n: int) -> bool:
        
        def isHappyN(count,number):
            print(number)
            if count==0:
                return False
            sum=0
            while(number>0):
                lastDigit=number%10
                sum+=lastDigit**2
                number=number//10
            if sum==1:
                return True
            else:
                return isHappyN(count-1,sum)
        return isHappyN(7,n)
