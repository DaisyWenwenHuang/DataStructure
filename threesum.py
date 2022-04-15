# https://leetcode.com/problems/3sum/
# sort the array to get rid of the dupulicate

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
            if diff in hashmap:
                continue
            if nums[k] in hashmap:
                j = hashmap[nums[k]]
                res.append((nums[i],nums[j],nums[k]))
            hashmap[diff] = k
            print(hashmap)
    return res

# not good  as can not reduce  inside loop duplicate
print(threeSum([0,0,0,0]))