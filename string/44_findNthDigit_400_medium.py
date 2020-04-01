"""
数字以0123456789101112131415…的格式序列化到一个字符序列中。在这个序列中，第5位（从下标0开始计数）是5，第13位是1，第19位是4，等等。

请写一个函数，求任意第n位对应的数字。

 

示例 1：

输入：n = 3
输出：3
示例 2：

输入：n = 11
输出：0

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/shu-zi-xu-lie-zhong-mou-yi-wei-de-shu-zi-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
"""
找数字规律
"""

class Solution:
    def findNthDigit(self, n: int) -> int:
        digit = 1
        n -= 1
        # first_num 1, 10, 100, 1000 --> 10 ** (digit-1)
        # numbers   9, 90, 900, 9000 --> 9 * first_num


        while (digit < 11):
            first_num = 10**(digit -1)
            if n < 9 * first_num * digit:
                return int(str(first_num + n // digit)[n % digit])
            n -= 9 * first_num * digit
            digit += 1
        return 0
