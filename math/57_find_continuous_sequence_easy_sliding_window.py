"""面试题57 - II. 和为s的连续正数序列
输入一个正整数 target ，输出所有和为 target 的连续正整数序列（至少含有两个数）。

序列内的数字由小到大排列，不同序列按照首个数字从小到大排列。



示例 1：

输入：target = 9
输出：[[2,3,4],[4,5]]
示例 2：

输入：target = 15
输出：[[1,2,3,4,5],[4,5,6],[7,8]]


限制：

1 <= target <= 10^5"""

def findContinuousSequence(target: int):
    res = []
    if target < 3:
        return res
    l, r = 1, 2

    while (l < r):
        cur_sum = (l+r)*(r-l+1)//2
        if cur_sum < target:
            r +=1
        elif cur_sum > target:
            l +=1
        else:
            tmp = []
            for i in range(l, r+1):
                tmp.append(i)
            res.append(tmp)
            l += 1
    return res

print(findContinuousSequence(9))
