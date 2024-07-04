# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        def leftheight(node):
            height = 0
            while node:
                height += 1
                node = node.left 
            return height
        
        def rightheight(node):
            height = 0
            while node:
                height += 1
                node = node.right

        left_height = leftheight(root)
        right_height = rightheight(root)

        if left_height == right_height:
            return 2^left_height + 1

        else:
            return 1 + self.countNodes(root.left) + self.countNodes(root.right)

        