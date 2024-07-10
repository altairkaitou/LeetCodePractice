# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        if n == 0 or n % 2 == 0:
            return []
        if n == 1:
            return [TreeNode(0)]

        result = []

        for left_node in range(1, n, 2):
            right_node = n - 1 - left_node
            left_trees = self.allPossibleFBT(left_node)
            right_trees = self.allPossibleFBT(right_node)
            for left in left_trees:
                for right in right_trees:
                    result.append(TreeNode(0, left, right))

        return result

        




        