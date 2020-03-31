"""
解决一个回溯问题，实际上就是一个决策树的遍历过程。需要思考3个问题：
1. 路径： 也就是已经做出的选择。
2. 选择列表： 也就是你当前可以做的选择
3. 结束条件： 也就是到达决策树底层， 无法再做选择的条件。

经典题：
全排列， N皇后问题

回溯算法的框架

result = []
def backtrack(路径，选择列表)：
    if 满足条件：
        result.add(路径)
        return

    for 选择 in 选择列表：
        做选择
        backtrack(路径，列表)
        撤销选择

核心就是for 循环里面的递归， 在递归调用之前「做选择」， 在递归调用之后「撤销选择」

                       []
        1              2               3
       [1]            [2]            [3]
 做出选择/撤销选择
    2     3         1     3       1      2
[1,2,3] [1,3,2] [2,1,3][2,3,1] [3,1,2][3,2,1]

[2] 就是「路径」， 记录已经做过的选择[1,3], 就是「选择列表」， 表示你当前可以做出的选择， 「结束条件」就是遍历到树的底层，在这里就是选择列表为空的时候。

多叉树的遍历框架就是这样：
void traverse(TreeNode root){
    for(TreeNode child: root.children)
    // 前序遍历需要的操作
    traverse(child);
    // 后序遍历需要的操作
}

前序遍历的代码就是进入某一个节点之前的那个时间点执行，后序遍历代码就是在离开某个节点之后的那个时间点执行。

for 选择 in 选择列表：
    #做选择
    将该选择从选择列表移除
    路径.add(选择)
    backtrack(路径，选择列表)
    #撤销选择
    路径.remove(选择)
    将该选择再加入选择列表

主要在递归之前做出选择，在递归之后撤销刚才的选择，就能正确得到每个节点的选择列表和路径。

回溯算法时间复杂度都不可能低于O(N!),  因为穷举整棵决策树是无法避免的。这也是回溯算的一个特点，不像动态规划存在重叠子问题可以优化，回溯算法就是纯暴力穷举，复杂度一般都很高。
"""

test = [1, 2, 3]


def permutation(nums: []) -> []:
    res = []
    if not nums:
        return res
    def backtrack(nums, res, idx):
        if idx == len(nums) - 1:
            #print("in backTrack branch",nums, idx, ">>>>", res)
            res.append(nums)
            print("after append", res)

        for i in range(idx, len(nums)):
            nums[i], nums[idx] = nums[idx], nums[i]
            backtrack(nums[:], res, 1 + idx)
            nums[i], nums[idx] = nums[idx], nums[i]

    backtrack(nums, res, 0)
    return res




print(permutation(test))


class Solution:
    def permutation(self, s: str) -> List[str]:
        res = []

        def backtrack(nums, res, idx):
            if idx == len(nums)-1:
                res.append("".join(nums))

            for i in range(idx, len(nums)):
                nums[i],nums[idx] = nums[idx], nums[i]
                backtrack(nums, res, 1+idx)
                nums[i],nums[idx] = nums[idx], nums[i]

        if not s:
            return res
        backtrack(list(s), res, 0)

        return list(set(res))

        # res = []
        # if len(s) <= 1:
        #     return list(s)

        # for i, ch in enumerate(s):
        #     rest = s[:i] + s[i+1:]
        #     for y in self.permutation(rest):
        #         res.append(ch+y)
        # return list(set(res))

        # res = []
        # if not s:
        #     return res
        # nums = sorted(s)

        # def dfs(nums, path):
        #     if not nums:
        #         res.append(path)

        #     for i, ch in enumerate(nums):
        #         if i > 0 and nums[i] == nums[i-1]:
        #             continue
        #         dfs(nums[:i] + nums[i+1:], path+nums[i])
        #         # print (nums,"path", path+ nums[i])

        # dfs(nums, "")
        # return res


