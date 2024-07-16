# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        path = []
        def findPath(root, value, path):
            if not root:
                return False
            
            if root.val == value:
                return True
            
            path.append('L')
            if findPath(root.left, value, path):
                return True
            path.pop()
            

            path.append('R')
            if findPath(root.right, value, path):
                return True
            
            path.pop()
            return False
        
        def findmatch(root, value1, value2):
            if not root:
                return False
            
            if root.val == value1 or root.val == value2:
                return root
            
            left = findmatch(root.left, value1, value2)
            right = findmatch(root.right, value1, value2)

            
            if left and right:
                return root
            
            return left if left else right
        
        startPath = []
        findPath(root, startValue, startPath)

        desPath = []
        findPath(root, destValue, desPath)

        matchpoint = findmatch(root, startValue, destValue)

        pathToStart = []
        findPath(matchpoint, startValue, pathToStart)

        pathToEnd = []
        findPath(matchpoint, destValue, pathToEnd)

        return 'U' * len(pathToStart) + "".join(pathToEnd)
        


            
    

        