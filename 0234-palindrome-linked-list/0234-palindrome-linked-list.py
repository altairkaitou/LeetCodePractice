# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        listvalue = []

        while head:
            listvalue.append(head.val)
            head = head.next
        
        left = 0
        right = len(listvalue) - 1

        while left < right and listvalue[left] == listvalue[right]:
            left+=1
            right -= 1
        
        return left >= right 
        