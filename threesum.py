# https://leetcode.com/problems/3sum/
# sort the array to get rid of the dupulicate
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        A = {}
        for i in range(len(nums)):
            if nums[i] in A:
                continue
            else:
                A[nums[i]] = i
            target = 0 - nums[i]
            hashmap = {}
            for k in range(i + 1, len(nums)):
                diff = target - nums[k]
                if nums[k] in hashmap:
                    j = hashmap[nums[k]]
                    res.append((nums[i],nums[j],nums[k]))
                hashmap[diff] = k
        return res