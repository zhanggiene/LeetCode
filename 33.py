class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start=0
        end=len(nums)-1
        while (start<=end):
            print(start)
            print(end)
            middle=(start+end)//2
            if start==end and nums[start]==target:
                return start
            elif start==end and nums[start]!=target:
                return -1
            elif end-start==1:
                if target==nums[start]:
                    return start
                elif target==nums[end]:
                    return end
                else:
                    return -1
            if nums[middle]<=nums[start]:
                if target>nums[middle] and target<=nums[end]:
                    start=middle
                else:
                    end=middle
            else:
                if target<nums[middle] and target>=nums[start]:
                    end=middle
                else:
                    start=middle
        return -1
            