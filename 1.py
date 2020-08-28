#tricky test case [3,3] 6
# [3,2,3]  6
# super long 

'''
1, sort the number list 
2, [1,2,3,4,5]   start from the first number, use binary search to search for target -1. then if found return the number 4
3, use linear search to search for the index of 4 in the original list. 



'''

def binary_search(arr, low, high, x):
    if high >= low: 

        mid = (high + low) // 2

        # If element is present at the middle itself 
        if arr[mid] == x: 
            return mid 

        # If element is smaller than mid, then it can only 
        # be present in left subarray 
        elif arr[mid] > x: 
            return binary_search(arr, low, mid - 1, x) 

        # Else the element can only be present in right subarray 
        else: 
            return binary_search(arr, mid + 1, high, x) 

    else: 
        # Element is not present in the array 
        return -1
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sortedList=sorted(nums)
        high=len(sortedList)
        for i in range(len(sortedList)):
            if binary_search(sortedList,i,high-1,target-sortedList[i])!=-1:
                lowerNumber=sortedList[i]
                highNumberIndex=binary_search(sortedList,i,high,target-sortedList[i])
                highNumber=sortedList[highNumberIndex]
                if lowerNumber==highNumber:
                    lowerNumberIndex=nums.index(lowerNumber)
                    return [lowerNumberIndex,nums.index(highNumber,lowerNumberIndex+1,high)]
                    
                return [nums.index(lowerNumber),nums.index(highNumber)]
                