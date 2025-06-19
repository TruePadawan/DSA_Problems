class Solution {
    public TreeNode removeLeafNodes(TreeNode root, int target) {
        if (root.left != null) {
            removeLeafNodes(root.left, target);
        }
        if (root.right != null) {
            removeLeafNodes(root.right, target);
        }

        boolean leftIsLeafNode = root.left != null && root.left.left == null && root.left.right == null;
        boolean rightIsLeafNode = root.right != null && root.right.left == null && root.right.right == null;
        if (leftIsLeafNode && root.left.val == target) {
            root.left = null;
        }
        if (rightIsLeafNode && root.right.val == target) {
            root.right = null;
        }

        boolean currentNodeIsLeafNode = root.left == null && root.right == null;
        if (currentNodeIsLeafNode && root.val == target) {
            return null;
        }
        return root;
    }
}