import java.util.Collections;
import java.util.LinkedList;
import java.util.Queue;

public class Solution {
    public static boolean isCompleteTree(TreeNode root) {
        Queue<TreeNode> nodeQueue = new LinkedList<>(Collections.singletonList(root));
        Boolean encounteredNullNode = false;
        while (!nodeQueue.isEmpty()) {
            TreeNode node = nodeQueue.poll();
            if (node == null) {
                encounteredNullNode = true;
            } else if (node != null && encounteredNullNode) {
                return false;
            } else {
                nodeQueue.add(node.left);
                nodeQueue.add(node.right);
            }
        }
        return true;
    }
}
