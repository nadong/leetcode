"""
输入数字 n，按顺序打印出从 1 到最大的 n 位十进制数。比如输入 3，则打印出 1、2、3 一直到最大的 3 位数 999。

示例 1:

输入: n = 1
输出: [1,2,3,4,5,6,7,8,9]
 

说明：

用返回一个整数列表来代替打印
n 为正整数
"""

class Solution:
    def __init__(self):
        self.result = [] # 用来保存结果

    def printNumbers(self, n: int) -> List[int]:
        if n <= 0:
            return []
        number = ["0"]*n
        number[-1] = "1"
        for i in range(0, 10):
            number[0] = chr(ord("0")+i) # ord 是将一个字符转换成 ASCII 码，chr 是将一个 ASCII 码转换成一个数字
            self.Print1ToMaxOfDigitsRecursively(number, n, 0)
        return (self.result[1:])

    def Print1ToMaxOfDigitsRecursively(self, number, length, index):
        if index == length - 1:
            self.PrintNumberNormal(number)
            self.result.append(int("".join(number)))
            return

        for i in range(10):
            number[index+1] = chr(ord("0")+i)
            self.Print1ToMaxOfDigitsRecursively(number, length, index+1)

    def PrintNumberNormal(self, number):
        number = int("".join(number))
        if number != 0:
            print(number)