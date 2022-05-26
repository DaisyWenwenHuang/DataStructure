# https://leetcode.com/problems/move-zeroes/
# array
# move zeros to the rigth , equals move non-zeros to the left
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = 0
        for r in range(len(nums)):
            if nums[r]:
                nums[l], nums[r] = nums[r],nums[l]
                l += 1
        # return nums
#