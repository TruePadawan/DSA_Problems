import java.util.HashMap;

/**
 * We need to keep track of the latest node at each depth (hashmap)
 * After parsing a depth D, set the latest node at D-1 to be its parent (left first then right)
 * return root (0th Depth node)
 */
class Solution {
    StringBuilder nodeValue = new StringBuilder();
    HashMap<Integer, TreeNode> depthToLatestNodes = new HashMap<>();
    int currentDepth = 0;

    public TreeNode recoverFromPreorder(String traversal) {
        for (int i = 0; i < traversal.length(); i++) {
            char currentChar = traversal.charAt(i);
            // About to parse a node at some depth
            if (currentChar == '-') {
                if (!nodeValue.isEmpty()) {
                    // We should process the previous node
                    processCurrentNode();
                }
                currentDepth += 1;
            } else {
                nodeValue.append(currentChar);
                boolean atLastNode = i == traversal.length() - 1;
                if (atLastNode) {
                    // Don't quit early, process the last node
                    processCurrentNode();
                }
            }
        }
        return depthToLatestNodes.get(0);
    }

    private void processCurrentNode() {
        TreeNode processedNode = new TreeNode(Integer.parseInt(nodeValue.toString()));
        depthToLatestNodes.put(currentDepth, processedNode);
        boolean notRootNode = currentDepth > 0;
        if (notRootNode) {
            TreeNode parentNode = depthToLatestNodes.get(currentDepth - 1);
            if (parentNode.left == null) {
                parentNode.left = processedNode;
            } else {
                parentNode.right = processedNode;
            }
        }
        nodeValue = new StringBuilder();
        currentDepth = 0;
    }
}