# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        listnode = []

        def inorderTraverse(node):
            if not node:
                return []
            
            inorderTraverse(node.left)
            listnode.append(node.val)
            inorderTraverse(node.right)

        def BST(left, right):

            if left > right:
                return None 
            mid = left + (right - left) // 2
            left = BST(left, mid -1)
            right = BST(mid + 1, right)
            return TreeNode(listnode[mid], left, right)
        
        inorderTraverse(root)
        return BST(0, len(listnode) - 1)


        