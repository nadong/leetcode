"""
请从字符串中找出一个最长的不包含重复字符的子字符串，计算该最长子字符串的长度。

 

示例 1:

输入: "abcabcbb"
输出: 3
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。

"""
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 2:
            return len(s)

        # head, tail, res = 0, 0, 1
        # while (tail <= len(s)-1):
        #     if s[tail] not in s[head:tail]:
        #         res = max(res, tail - head + 1)
        #     else:
        #         while s[tail] in s[head:tail]:
        #             head += 1
        #     tail += 1
        # return res
        head, tail, res = 0, 0, 0
        hash_map = {}
        while tail <= len(s)-1:
            if s[tail] in hash_map.keys():
                head  = max(head, hash_map[s[tail]])
            hash_map[s[tail]] = tail + 1
            res = max(res, tail - head + 1)
            tail += 1

        return res
"""
class Ugly:
    def __init__(self):
        self.nums = [1,]
        i2, i3 , i5 = 0,0,0
        for i in range(1, 1690):
            self.nums.append(min(self.nums[i2]*2, self.nums[i3]*3, self.nums[i5]*5))
            if self.nums[i] == self.nums[i2] * 2:
                i2 += 1
            if self.nums[i] == self.nums[i3] * 3:
                i3 += 1
            if self.nums[i] == self.nums[i5] * 5:
                i5 += 1
    

class Solution:
    u = Ugly()
    def nthUglyNumber(self, n: int) -> int:
        return self.u.nums[n-1]
    """