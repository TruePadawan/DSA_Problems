/**
 * First let's find the closest ancestor of both start and end nodes
 * Perhaps post-order traversal
 */
class Solution {
    String shortestPath = "";
    TreeNode closestAncestor;

    public String getDirections(TreeNode root, int startValue, int destValue) {
        getClosestAncestor(root, startValue, destValue);
        System.out.println(closestAncestor.val);
        return "";
    }

    private boolean getClosestAncestor(TreeNode node, int start, int dest) {
        boolean oneFound = false;
        boolean secondFound = false;
        if (node.left != null) {
            oneFound = getClosestAncestor(node.left, start, dest);
        }
        if (node.right != null) {
            secondFound = getClosestAncestor(node.right, start, dest);
        }
        boolean isClosestAncestor = oneFound && secondFound;
        System.out.println(node.val);

        if (isClosestAncestor) {
            closestAncestor = node;
        }
        return node.val == start || node.val == dest;
    }
}