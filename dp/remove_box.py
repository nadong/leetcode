"""
https://leetcode-cn.com/problems/remove-boxes/

给出一些不同颜色的盒子，盒子的颜色由数字表示，即不同的数字表示不同的颜色。
你将经过若干轮操作去去掉盒子，直到所有的盒子都去掉为止。每一轮你可以移除具有相同颜色的连续 k 个盒子（k >= 1），这样一轮之后你将得到 k*k 个积分。
当你将所有盒子都去掉之后，求你能获得的最大积分和。

e.g. [1, 3, 2, 2, 2, 3, 4, 3, 1]
"""
from functools import lru_cache

from typing import List


def removeBoxes(boxes: List[int]) -> int:
    @lru_cache(None)
    def dp(l, r, k):
        if l > r: return 0
        while r > l and boxes[r - 1] == boxes[r]:
            r -= 1
            k += 1
        res = dp(l, r - 1, 0) + (k + 1) * (k + 1)
        for i in range(l, r):
            if boxes[i] == boxes[r]:
                res = max(res, dp(l, i, k + 1) + dp(i + 1, r - 1, 0))
        return res

    return dp(0, len(boxes) - 1, 0)


print(removeBoxes([1,3,2,2,2,3,4,3,1]))