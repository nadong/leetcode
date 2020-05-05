def maxSubArray(nums) -> int:
    res = 0
    if not nums:
        return res
    dp = nums
    for i in range(1, len(nums)):
        if dp[i-1] >= 0:
            dp[i] = dp[i-1] + nums[i]
        else:
            dp[i] = nums[i]
    return max(dp)

print(maxSubArray([1,-1,1]) == 1)