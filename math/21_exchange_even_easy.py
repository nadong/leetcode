"""
面试题21. 调整数组顺序使奇数位于偶数前面 LCOF
"""
class Solution:
    def exchange(self, nums: List[int]) -> List[int]:
        if not nums:
            return nums

        i, j = 0 , len(nums) -1

        while (i < j):
            # 奇数
            if nums[i] % 2 == 1:
                i += 1
            elif nums[j] %2 == 0:
                j -= 1
            else:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1
        return nums