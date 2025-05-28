// Definition for a binary tree node.
class TreeNode {
    val: number
    left: TreeNode | null
    right: TreeNode | null

    constructor(val?: number, left?: TreeNode | null, right?: TreeNode | null) {
        this.val = (val === undefined ? 0 : val)
        this.left = (left === undefined ? null : left)
        this.right = (right === undefined ? null : right)
    }
}

function isBalanced(root: TreeNode | null): boolean {
    if (root == null || root.left == null && root.right == null) {
        return true;
    }
    let balanced = true;

    function recurse(node: TreeNode | null, height: number) {
        if (node == null) return 0;
        if (node.left == null && node.right == null) return height;
        let leftHeight = height, rightHeight = height;
        if (node.left !== null) {
            leftHeight = recurse(node.left, height + 1);
        }
        if (node.right !== null) {
            rightHeight = recurse(node.right, height + 1);
        }
        if (balanced == true) {
            balanced = Math.abs(leftHeight - rightHeight) <= 1;
        }
        return Math.max(leftHeight, rightHeight);
    }

    const left = recurse(root.left, 1);
    const right = recurse(root.right, 1);
    if (balanced == true) {
        balanced = Math.abs(left - right) <= 1;
    }
    return balanced;
}