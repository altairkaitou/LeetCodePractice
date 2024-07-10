# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        pointer = ListNode(0, head)
        dummy = pointer

        while dummy:
            while dummy.next and dummy.next.val == val:
                dummy.next = dummy.next.next
            dummy = dummy.next
        
        return pointer.next

       


        