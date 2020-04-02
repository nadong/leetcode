"""
# find the once number in a list
抽象成2进制不进位加法

class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        if not nums:
            return -1
        single_nums = 0
        for n in nums:
            single_nums ^= n
        return single_nums

time complex: O(N)
storage complexity: O(1)
"""

"""
抽象成三进制不进位加法
class Solution:
    def singleNumber(self, nums: [int]) -> int:
        ones, twos, threes = 0, 0, 0
        for num in nums:
            twos |= ones & num # 二进制某位出现1次时twos = 0，出现2, 3次时twos = 1； 
            # | 位或
            ones ^= num  # 二进制某位出现2次时ones = 0，出现1, 3次时ones = 1；
            # ^ 异或
            threes = ones & twos # 二进制某位出现3次时（即twos = ones = 1时）three = 1，其余即出现1, 2次时three = 0；
            ones &= ~threes # 将二进制下出现3次的位置零，实现`三进制下不考虑进位的加法`；
            twos &= ~threes
        return ones
"""
"""
现在数组中有两个数字只出现1次，直接异或一次只能得到这两个数字的异或结果，但光从这个结果肯定无法得到这个两个数字。因此基于single number I 的思路——数组只能有一个数字出现1次。

设题目中这两个只出现1次的数字分别为A和B，如果能将A，B分开到二个数组中，那显然符合“异或”解法的关键点了。因此这个题目的关键点就是将A，B分开到二个数组中。由于A，B肯定是不相等的，因此在二进制上必定有一位是不同的。根据这一位是0还是1可以将A，B分开到A组和B组。而这个数组中其它数字要么就属于A组，要么就属于B组。再对A组和B组分别执行“异或”解法就可以得到A，B了。而要判断A，B在哪一位上不相同，只要根据A异或B的结果就可以知道了，这个结果在二进制上为1的位就说明A，B在这一位上是不相同的。

比如

int a[] = {1, 1, 3, 5, 2, 2}
整个数组异或的结果为3^5，即 0x0011 ^ 0x0101 = 0x0110

对0x0110，第1位（由低向高，从0开始）就是1。因此整个数组根据第1位是0还是1分成两组。

a[0] =1  0x0001  第一组

a[1] =1  0x0001  第一组

a[2] =3  0x0011  第二组

a[3] =5  0x0101  第一组

a[4] =2  0x0010  第二组

a[5] =2  0x0010  第二组
第一组有{1,1,5}，第二组有{3,2,3}，然后对这二组分别执行“异或”解法就可以得到5和3了。

代码：
时间复杂度O(n)，空间复杂度O(1)
"""
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        res = [0 for _ in  range(2)]
        xores = 0
        for n in nums:
            xores ^=n

        bit_index = 1
        while True:
            if (xores & 1) == 1: # 从低位开始找， 第一个值为1 的
                break
            bit_index = bit_index<< 1
            xores = xores >> 1

        for n in nums:
            if n & bit_index == 0:  # 不能写成 == 1
                res[0] ^= n
            else :
                res[1] ^= n
        return res
