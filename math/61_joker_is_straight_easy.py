def isStraight(nums) -> bool:
    if not nums or len(nums) != 5:
        return False

    nums.sort()
    joker = 0
    for i in range(4):
        if nums[i] == 0:
            joker += 1
        else:
            if nums[i] == nums[i + 1]:
                return False
    return nums[4] - nums[joker] < 5


print(isStraight([0, 0, 1, 2, 5]))
