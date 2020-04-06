"""
给定一个数字，我们按照如下规则把它翻译为字符串：0 翻译成 “a” ，1 翻译成 “b”，……，11 翻译成 “l”，……，25 翻译成 “z”。一个数字可能有多个翻译。请编程实现一个函数，用来计算一个数字有多少种不同的翻译方法。


示例 1:

输入: 12258
输出: 5
解释: 12258有5种不同的翻译，分别是"bccfi", "bwfi", "bczi", "mcfi"和"mzi"

"""
class Solution:
    def translateNum(self, num: int) -> int:
        num_str = str(num)

        def backTrack(s: str, pos: int)-> int:
            size = len(s)
            if pos == size:
                return 1
            if s[pos] == '0' or pos == size -1 or s[pos:pos+2] > '25':
                return backTrack(s, pos+1)
            return backTrack(s, pos+1) + backTrack(s, pos+2)

        return backTrack(num_str, 0)