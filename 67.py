class Solution:
    def addBinary(self, a: str, b: str) -> str:
        lena=len(a)-1
        lenb=len(b)-1
        result=[]
        carry=0
        while lena>=0 or lenb>=0:
            
            number1=int(a[lena]) if lena>=0 else 0
            number2=int(b[lenb]) if lenb>=0 else 0
            print(carry+number1+number2)
            if carry+number1+number2==3:
                carry=1
                result.append(1)
            elif carry+number1+number2==2:
                carry=1
                result.append(0)
            elif carry+number1+number2==1:
                carry=0
                result.append(1)
            else:
                result.append(0)
            lena-=1
            lenb-=1
        if carry:
            result.append(1)
        print(result)
        resultString=[str(i) for i in result]
        resultString.reverse()
        return "".join(resultString)