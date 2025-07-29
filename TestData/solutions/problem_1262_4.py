class Solution:
    def solution_1262_4(self, nums1: List[int], nums2: List[int]) -> int:
        result = 0
        max_dist = 0
        m, n = len(nums1), len(nums2)
		#iterate from left of nums1
        for i in range(m):
			#for every element, find the index of nums2 with value <= nums1[i] in the range nums2[i:len(nums2)]
            start = i
            end = len(nums2)-1
			#binary-search
            while start<=end:
                mid = start + (end-start)//2
				#look to the left for a closer match
                if nums2[mid]<nums1[i]:
                    end = mid-1
				#look to the right for a closer match
                elif nums2[mid]>=nums1[i]:
                    start = mid+1
			#at the end of binary-search, nums2[end] will hold the closest value to nums1[i]
			#check if it is the max distance
            max_dist = max(max_dist,end-i)
                
        return max_dist