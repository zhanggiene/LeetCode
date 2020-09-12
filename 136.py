class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dictionary={}
        for i in nums:
            if i not in dictionary:
                dictionary[i]=1
            else:
                dictionary[i]=2
        for i in dictionary:
            if dictionary[i]==1:
                return i
                