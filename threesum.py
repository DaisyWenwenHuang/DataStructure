# https://leetcode.com/problems/3sum/
# sort the array to get rid of the dupulicate
# similar to twosum
# log(n)

def threeSum(nums):
    nums.sort()
    res = []
    A = {}
    for i in range(len(nums)):
        print(i)
        if nums[i] in A:
            continue
        else:
            A[nums[i]] = i
        print(A)
        target = 0 - nums[i]
        hashmap = {}
        for k in range(i + 1, len(nums)):
            diff = target - nums[k]
            if nums[k] in hashmap:
                j = hashmap[nums[k]]
                res.append((nums[i],nums[j],nums[k]))
            hashmap[diff] = k
            print(hashmap)
    return res

#??????????????????
# not good  as can not reduce  inside loop duplicate
print(threeSum([0,0,0,0]))


# solution
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res=[]
        
        for i, a in enumerate(nums):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            l, r = i + 1, len(nums) - 1
            while l < r:
                threesum = a + nums[l] + nums[r]
                if threesum > 0:
                    r -=1
                elif threesum < 0:
                    l += 1
                else:
                    res.append([a,nums[l],nums[r]])
                    l += 1
					# only need to update the left pointer to avoid duplicate
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
        return res
