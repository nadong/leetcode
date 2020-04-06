"""
求 1+2+...+n ，要求不能使用乘除法、for、while、if、else、switch、case等关键字及条件判断语句（A?B:C）。

 

示例 1：

输入: n = 3
输出: 6
示例 2：

输入: n = 9
输出: 45
 
"""

class Solution:
    def sumNums(self, n: int) -> int:
        res = 0
        if n > 0:
            res += self.sumNums(n-1)
        res += n
        return res