# https://leetcode.com/problems/3sum-closest/

def threeSumClosest(nums,target):
	nums.sort()
	best_s = float('inf')

	for i in range(len(nums) - 2):
		if nums[i] == nums[i-1] and i > 0:
			continue

		lower = i +1
		upper = len(nums) - 1

		while lower < upper:
			s = nums[i] + nums [upper] + nums[lower]

			if s == target:
				return s

			if abs(target - s) < abs(target-best_s):
				best_s = s

			if s <= target:
				lower += 1
				while(nums[lower] == nums[lower-1] and lower < upper):
					lower += 1
			else:
				upper -= 1
	return best_s

nums = [-1,2,1,-4]
nums1= [0,0,0]
target = 1
print(threeSumClosest(nums1,target))
