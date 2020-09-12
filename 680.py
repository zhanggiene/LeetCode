

'''
since it allows for one mistake, then u should have one separate class. 

'''


class Solution:
    def validPalindrome(self, s: str) -> bool:
        def strictpalindrome(s:str) ->bool:
            print(s)
            i=0
            length=len(s)
            if length==0:
                return True
            while i*2<=length:
                if s[i]!=s[length-i-1]:
                    return False
                i+=1
            return True
        i=0
        length=len(s)
        while (i*2<=length):
            #print(i)
            if s[i]!=s[length-i-1]:
                return strictpalindrome(s[i+1:length-i]) or strictpalindrome(s[i:length-i-1])
            else:
                i+=1
        return True
            
        
        
    def strictpalindrome(s:str) ->bool:
        i=0
        length=len(s)
        while i*2<=length:
            if s[i]!=s[length-i-1]:
                return False
            i+=1
        return True
            