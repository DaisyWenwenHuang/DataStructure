# https://leetcode.com/problems/container-with-most-water/
# start two pointers from the left and right , as to maximum the length
# the conidtion to move the pointer is to compare and move the smaller one.
class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        res = 0
        r = len(height) - 1
        while r > l:
            cur = min(height[l],height[r]) * (r - l)
            res = max(res, cur)
            
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return res
                