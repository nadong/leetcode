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