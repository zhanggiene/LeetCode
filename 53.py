
'''

find the maximum sub array 


       [-2,1,-3,4,-1,2,1,-5,4]
        -2 -1 
        the second array is the largest sub array ending with the current number
        the number below will be either the current number or the sum of the current plus the previous max sub array. 




'''



class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        preMax=[]
        for i in range(len(nums)):
            if i==0:
                preMax.append(nums[i])
            else:
                preMax.append(max(nums[i],nums[i]+preMax[i-1]))
        return max(preMax)