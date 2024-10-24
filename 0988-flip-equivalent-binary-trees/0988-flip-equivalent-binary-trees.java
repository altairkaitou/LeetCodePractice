/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public boolean flipEquiv(TreeNode root1, TreeNode root2) {
        return recursiveChecker(root1, root2);
    }

    // Using Recursion to Check the position
    private boolean recursiveChecker(TreeNode node1, TreeNode node2) {
        if (node1 == null && node2 == null ) {
            return true;
        }

        if (node1 == null || node2 == null || node1.val != node2.val ) {
            return false;
        }

        return (recursiveChecker(node1.left, node2.left) || recursiveChecker(node1.left, node2.right)) && 
                (recursiveChecker(node1.right, node2.right) || recursiveChecker(node1.right, node2.left));
    }
}