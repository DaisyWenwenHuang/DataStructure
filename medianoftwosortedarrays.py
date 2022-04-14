# https://leetcode.com/problems/median-of-two-sorted-arrays/
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
		A,B = nums1, nums2
		total = len(nums1) + len(nums2)
		half = total // 2

		if len(B) < len(A):
			A, B = B, A # make sure that A is the shorter array

		l,r = 0, len(A) - 1
		while True:
			i = (l + r) // 2 # A
			j = half - i - 2 # B, here -2 becasue of j is index, 0 based,i,j

			if i >= 0:
				Aleft = A[i]
			else:
				Aleft = float(-inf)
			if (i + 1) < len(A):
				Aright = A[i + 1]
			else:
				Aright = float(inf)
			if j >= 0:
				Bleft = B[j]
			else:
				Bleft = float(-inf)
			if j + 1 < len(B):	
				Bright = B[j + 1]
			else:
				Bright = float(inf)

			if Aleft <= Bright and Bleft <= Aright:
				# odd
				if total % 2:
					return min(Aright,Bright)
				# Even 
				return (max(Aleft,Bleft) + min(Aright,Bright)) / 2
			elif Aleft > Bright:
				r = i - 1
			else:
				l = i + 1
				
			