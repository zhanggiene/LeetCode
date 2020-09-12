class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict1={}
        dict2={}
        for i in s:
            if i not in dict1:
                dict1[i]=1
            else:
                dict1[i]=dict1[i]+1
        for j in t:
            if j not in dict2:
                dict2[j]=1
            else:
                dict2[j]=dict2[j]+1
        if len(s)>len(t):
            for i in dict1:
                if i not in dict2 or dict2[i]!=dict1[i]:
                    return False
        else:
            for i in dict2:
                if i not in dict1 or dict1[i]!=dict2[i]:
                    return False
            
        print(dict1)
        print(dict2)
        return True
        