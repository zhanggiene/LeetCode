# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        pointer1=head
        pointer2=head
        while(pointer1!=None and pointer1!=None):
                pointer2=pointer1.next
                while(pointer2!=None and pointer2.val==pointer1.val):
                    pointer2=pointer2.next
                pointer1.next=pointer2
                pointer1=pointer1.next
        return head