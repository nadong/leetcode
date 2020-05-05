# 终止条件： 当节点 rootroot 为空（越过叶节点），则直接返回；
# 递归右子树： 即 dfs(root.right)dfs(root.right) ；
# 三项工作：
# 提前返回： 若 k = 0k=0 ，代表已找到目标节点，无需继续遍历，因此直接返回；
# 统计序号： 执行 k = k - 1k=k−1 （即从 kk 减至 00 ）；
# 记录结果： 若 k = 0k=0 ，代表当前节点为第 kk 大的节点，因此记录 res = root.valres=root.val ；
# 递归左子树： 即 dfs(root.left)dfs(root.left) ；
#

class Solution:
    def kthLargest(self, root: TreeNode, k: int) -> int:
        def dfs(root: TreeNode):
            if not root:
                return

            dfs(root.right)
            if self.k == 0:
                return
            self.k -= 1
            if self.k==0:
                self.res = root.val
            dfs(root.left)

        self.k = k
        dfs(root)
        return self.res


