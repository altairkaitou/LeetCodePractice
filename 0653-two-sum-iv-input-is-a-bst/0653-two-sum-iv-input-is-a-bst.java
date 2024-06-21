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

    public boolean findTarget(TreeNode root, int k) {
        List<Integer> elements = new ArrayList<>();
        ConvertNode(root, elements);
        int left = 0;
        int right = elements.size() - 1;
        while (left < right) {
            if (elements.get(left) + elements.get(right) == k) {
                return true;
            } else if (elements.get(left) + elements.get(right) < k) {
                left++;
            } else {
                right--;
            }
        }

        return false;


        
    }
    private void ConvertNode(TreeNode node, List<Integer> elements) {
        if (node == null) {
            return;
        }
        ConvertNode(node.left, elements);
        elements.add(node.val);
        ConvertNode(node.right, elements);

    }
}