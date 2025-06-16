import java.util.ArrayList;
import java.util.List;

class Solution {
    List<Integer> values1 = new ArrayList<>();
    List<Integer> values2 = new ArrayList<>();

    public boolean leafSimilar(TreeNode root1, TreeNode root2) {
        inorderTraversal1(root1);
        inorderTraversal2(root2);
        if (values1.size() != values2.size()) return false;
        for (int val1 : values1) {
            int val2 = values2.removeFirst();
            if (val1 != val2) {
                return false;
            }
        }
        return true;
    }

    private void inorderTraversal1(TreeNode node) {
        if (node.left == null && node.right == null) {
            values1.add(node.val);
        } else {
            if (node.left != null) {
                inorderTraversal1(node.left);
            }
            if (node.right != null) {
                inorderTraversal1(node.right);
            }
        }
    }

    private void inorderTraversal2(TreeNode node) {
        if (node.left == null && node.right == null) {
            values2.add(node.val);
        } else {
            if (node.left != null) {
                inorderTraversal2(node.left);
            }
            if (node.right != null) {
                inorderTraversal2(node.right);
            }
        }
    }
}