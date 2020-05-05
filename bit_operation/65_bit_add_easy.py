class Solution:
    def add(self, a: int, b: int) -> int:
        x = 0xffffffff
        """
        获取负数的补码： 需要将数字与十六进制数 0xffffffff 相与。可理解为舍去此数字 3232 位以上的数字，从无限长度变为一个 3232 位整数。
        返回前数字还原： 若补码 aa 为负数（ 0x7fffffff 是最大的正数的补码 ），需执行 ~(a ^ x) 操作，将补码还原至 Python 的存储格式。 a ^ x 运算将 11 至 3232 位按位取反； ~ 运算是将整个数字取反；因此， ~(a ^ x) 是将 3232 位以上的位取反，即由 00 变为 11 ， 11 至 3232 位不变。
        """

        a, b = a & x , b &x
        while b != 0:
            a, b = (a ^ b), (a & b) << 1&x
        return a if a <= 0x7fffffff else ~(a^x)