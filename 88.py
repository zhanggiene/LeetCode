#merge sorted array

'''
the trick is to sort from behind. 

[1,2,3,0,0,0]    sort from behind so that there will always be spaces
[3,4,5]





'''
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i=m+n-1
        while(i>=0):
            number=0
            #print(n)
            if n==0:
                #print("break")
                break
            elif m==0:
                number=nums2[n-1]
                n-=1
            else:
                if nums1[m-1]>nums2[n-1]:
                    number=nums1[m-1]
                    m-=1
                else:
                    number=nums2[n-1]
                    n-=1
            nums1[i]=number
            i-=1
            #print(nums1)