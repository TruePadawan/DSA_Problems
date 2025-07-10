import java.util.HashSet;

/*
 * Use a set to determine if a path is pseudo-palindromic
 * When a value is first found, add it
 * If it's found again, remove it from the set
 * If a path is pseudo-palindromic, its set should have a length 0 or 1
 *
 * Use pre-order traversal
 * */
class Solution {
    int count = 0;

    public int pseudoPalindromicPaths(TreeNode root) {
        preOrderSolution(root, new HashSet<Integer>());
        return count;
    }

    private void preOrderSolution(TreeNode node, HashSet<Integer> pathSet) {
        HashSet<Integer> updatedPathSet = new HashSet<>(pathSet);
        if (!updatedPathSet.remove(node.val)) {
            updatedPathSet.add(node.val);
        }
        boolean isLeafNode = node.left == null && node.right == null;
        if (isLeafNode && (updatedPathSet.isEmpty() || updatedPathSet.size() == 1)) {
            count += 1;
        } else {
            if (node.left != null) {
                preOrderSolution(node.left, updatedPathSet);
            }
            if (node.right != null) {
                preOrderSolution(node.right, updatedPathSet);
            }
        }

    }
}