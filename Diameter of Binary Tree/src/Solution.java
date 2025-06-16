/*
* At each node, compare the edge count of each sub-tree:
*   Update the max edge count if needed
* Pass the max of the edge count of the left or right subtree up to the parent node
* */
class Solution {
    int maxDiameter = 0;

    public int diameterOfBinaryTree(TreeNode root) {
        postOrderTraversal(root, 0);
        return maxDiameter;
    }

    private int postOrderTraversal(TreeNode node, int length) {
        int left = length, right = length;
        if (node.left != null) {
            left = postOrderTraversal(node.left, length);
            left += 1;
        }
        if (node.right != null) {
            right = postOrderTraversal(node.right, length);
            right += 1;
        }
        int diameter = left + right;
        if (diameter > maxDiameter) {
            maxDiameter = diameter;
        }
        return Math.max(left, right);
    }
}