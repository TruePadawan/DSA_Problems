import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;

/**
 * DFS
 * If to be deleted: set value to null
 */

class Solution {
    List<TreeNode> roots = new ArrayList<>();

    public List<TreeNode> delNodes(TreeNode root, int[] to_delete) {
        root  = traversal(root, to_delete);
        if (root != null) {
            roots.add(root);
        }
        return roots;
    }

    private TreeNode traversal(TreeNode root, int[] to_delete) {
        if (root.left != null) {
            root.left = traversal(root.left, to_delete);
        }
        if (root.right != null) {
            root.right = traversal(root.right, to_delete);
        }
        boolean nodeShouldBeDeleted = isToBeDeleted(root, to_delete);
        if (nodeShouldBeDeleted) {
            if (root.left != null) {
                roots.add(root.left);
            }
            if (root.right != null) {
                roots.add(root.right);
            }
            root = null;
        }

        return root;
    }

    private boolean isToBeDeleted(TreeNode node, int[] to_delete) {
        for (int i: to_delete) {
            if (node.val == i) return true;
        }
        return false;
    }
}