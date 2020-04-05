"""
输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历结果。如果是则返回 true，否则返回 false。假设输入的数组的任意两个数字都互不相同。

 

参考以下这颗二叉搜索树：

     5
    / \
   2   6
  / \
 1   3
示例 1：

输入: [1,6,3,2,5]
输出: false
示例 2：

输入: [1,3,2,6,5]
输出: true
 

提示：

数组长度 <= 1000

"""


class Solution:
    def verifyPostorder(self, postorder: List[int]) -> bool:
        inorder = sorted(postorder)

        def dfs(inorder: List[int], postorder: List[int]):
            if not inorder: return True
            #if len(inorder) == 1: return inorder[0] == postorder[0]
            try:
                index = inorder.index(postorder[-1])
            except:
                return False
            inorder_left = inorder[:index]
            inorder_right = inorder[index+1:]
            return dfs(inorder_left, postorder[0:index]) and \
                   dfs(inorder_right, postorder[index:-1])

        return dfs(inorder, postorder)