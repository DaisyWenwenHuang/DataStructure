# https://leetcode.com/problems/rotate-array/
# array
# solution 1
# extra memory O(1), time O(k)
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        # edge case:
        if k == 0 or n == 1 or k == n:
            return 
        # K could be bigger than n
        k = k % n
        
        for i in range(k):
            ele = nums.pop()
            nums.insert(0,ele)
            
# solution 2
# reverse 3 times
# faster , no extra memory 
# solution 1 is slower because inserting in array is not that fast
# bacause array need to be shift after inserting/deleting
# as all the elements in an array are stored neighbouring each other in the memory 
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        # edge case:
        if k == 0 or n == 1 or k == n:
            return 
        # K could be bigger than n
        k = k % n
        
        def helper_reverse(start, end):
            while end > start:
                nums[start],nums[end] = nums[end], nums[start]
                start += 1
                end -= 1
                
        helper_reverse(0,n-1)
        helper_reverse(0,k-1)
        helper_reverse(k,n-1)
       