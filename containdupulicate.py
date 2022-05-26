# https://leetcode.com/problems/contains-duplicate/
# array
# using set
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        numset = set(nums)
        if len(numset) == len(nums):
            return False
        else:
            return True