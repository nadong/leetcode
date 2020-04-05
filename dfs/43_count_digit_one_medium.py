"""
输入一个整数 n ，求1～n这n个整数的十进制表示中1出现的次数。

例如，输入12，1～12这些整数中包含1 的数字有1、10、11和12，1一共出现了5次。

"""

class Solution:
    def countDigitOne(self, n: int) -> int:
        # count = 0
        # for i in range(1, n+1):
        #     while i > 0:
        #         if i % 10 == 1:
        #             count += 1
        #         i = i // 10
        # return count
        def dfs(n: int) -> int:
            if n <= 0 : return 0
            numStr = str(n)
            high = int(numStr[0])
            digit = int(pow(10, len(numStr)-1))
            last = n - high * digit

            if high == 1:
                return dfs(last) + last + 1 + dfs(digit -1 )
            else:
                return digit + high * dfs(digit -1 ) + dfs(last)

        return dfs(n)