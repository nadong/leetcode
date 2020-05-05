"""
在字符串 s 中找出第一个只出现一次的字符。如果没有，返回一个单空格。

示例:

s = "abaccdeff"
返回 "b"

s = ""
返回 " "
在哈希表的基础上，有序哈希表中的键值对是 按照插入顺序排序 的。基于此，可通过遍历有序哈希表，实现搜索首个 “数量为 11 的字符”。
"""
class Solution:
    def firstUniqChar(self, s: str) -> str:
        m = collections.OrderedDict()
        if not s:
            return " "

        for i in s:
            if m.get(i, None):
                m[i] += 1
            else:
                m[i] = 1

        for k, v in m.items():
            if v == 1:
                return k
        return " "