"""
请实现一个函数用来判断字符串是否表示数值（包括整数和小数）。例如，字符串"+100"、"5e2"、"-123"、"3.1416"、"0123"及"-1E-16"都表示数值，但"12e"、"1a3.14"、"1.2.3"、"+-5"及"12e+5.4"都不是。
"""

class Solution:
    def isNumber(self, s: str) -> bool:
        if not s :
            return False

        includeNum = False
        includeDot = False
        includeE = False
        s = s.strip(" ")
        for i in range(0, len(s)):
            if(s[i] >= '0' and s[i] <= '9'):
                includeNum= True
            elif s[i] == '.':
                if (includeE or includeDot):
                    return False
                includeDot = True
            elif s[i] == 'e' or s[i] == 'E':
                if (includeE or not includeNum):
                    return False
                includeE = True
                includeNum = False
            elif s[i] == '-' or s[i] == '+':
                if (i != 0 and s[i-1] != 'e' and s[i-1] != 'E'):
                    return False
            else:
                return False
        return includeNum
