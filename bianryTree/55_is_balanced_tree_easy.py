"""
输入一棵二叉树的根节点，判断该树是不是平衡二叉树。如果某二叉树中任意节点的左右子树的深度相差不超过1，那么它就是一棵平衡二叉树。

 

示例 1:

给定二叉树 [3,9,20,null,null,15,7]

    3
   / \
  9  20
    /  \
   15   7
返回 true 。

示例 2:

给定二叉树 [1,2,2,3,3,null,null,4,4]

       1
      / \
     2   2
    / \
   3   3
  / \
 4   4
返回 false
"""
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if not root:
            return True
        def depth(root: TreeNode):
            if not root: return 0
            left = depth(root.left)
            if left == -1: return -1
            right = depth(root.right)
            if right == -1: return -1
            return 1 + max(left, right) if abs(left-right) <= 1 else -1
        return depth(root) != -1
