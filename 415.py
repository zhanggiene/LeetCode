
'''
9
999999

we initialize i to be largest length, then 0-i, we add the number backwards, if there is no number then use one from the below, if there are both number, then add two digits. 


'''


class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        sumNumber=0
        num1Lengh=len(num1)
        num2Lengh=len(num2)
        if num1Lengh<=num2Lengh:
            for i in range(1,num2Lengh+1):
                if num1Lengh-i<0:
                    #print(int(num2[num2Lengh-i])*pow(10,i-1))
                    sumNumber+=int(num2[num2Lengh-i])*pow(10,i-1)
                else:
                    sumNumber+=(int(num1[num1Lengh-i])+int(num2[num2Lengh-i]))*pow(10,i-1)
                #print(sumNumber)
        else:
            for i in range(1,num1Lengh+1):
                if num2Lengh-i<0:
                    #print(int(num1[num1Lengh-i])*pow(10,i-1))
                    sumNumber+=int(num1[num1Lengh-i])*pow(10,i-1)
                else:
                    sumNumber+=(int(num2[num2Lengh-i])+int(num1[num1Lengh-i]))*pow(10,i-1)
                #print(sumNumber)
        return str(sumNumber)