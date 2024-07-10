# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        list_node = []

    

        while head:
            list_node.append(head.val)
            head = head.next
        
        left = 0
        right = len(list_node) - 1

        while left < right and list_node[left] == list_node[right]:
            left += 1
            right -= 1
        
        return left >= right 
        