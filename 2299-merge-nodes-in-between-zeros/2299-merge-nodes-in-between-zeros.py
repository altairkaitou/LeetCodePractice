# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        start = head.next
        dummy = start

        while dummy:
            result = 0

            while dummy.val != 0:
                result += dummy.val
                dummy = dummy.next
            
            start.val = result
           
            dummy = dummy.next
            start.next = dummy
            start = start.next
        
        return head.next
        