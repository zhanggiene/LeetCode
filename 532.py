class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        dictionary={}
        sum=0
        for i in nums:
            if i not in dictionary:
                dictionary[i]=1
            else:
                dictionary[i]+=1
        if k==0:
            for i in dictionary:
                if dictionary[i]!=1:
                    sum+=1
            return sum
        elif k<0:
            return 0
    
        for i in dictionary:
            first=1 if i-k in dictionary else 0
            second=1 if i+k in dictionary else 0
            sum+=(first+second)
            
        return sum//2