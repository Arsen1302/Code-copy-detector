class Solution:
    def solution_4_5_1(self, nums1, nums2) -> float:
        # odd length -> e.g. length 5, left(2) and right(2) would be the same index
        # even length -> e.g. length 6, left(2) and right(3) would be different indices
        m, n = len(nums1), len(nums2)
        left, right = (m+n-1)//2, (m+n)//2
        return (self.solution_4_5_2(nums1, nums2, left) + self.solution_4_5_2(nums1, nums2, right))/2
    
    def solution_4_5_2(self, nums1, nums2, k):
        # if one list is exhausted, return the kth index of the other list
        if nums1 == []:
            return nums2[k]
        if nums2 == []:
            return nums1[k]

        # base case
        # k is 0-based, so finding the kth index equals eliminating k length elements. 
		# k == 0 means we have eliminated all smaller indices, return the next highest number, which would be the median
        # e.g. to find the third index (k = 3), we eliminate 3 smaller elements (index 0, 1, 2)
        if k == 0:
            return min(nums1[0], nums2[0])

        # find the subarray to be eliminated this iteration
        m, n = len(nums1), len(nums2)
        eliminated_length = min(m,n,(k+1)//2)                 # 1-based so k + 1
        eliminated_index = eliminated_length - 1              # 0-based so - 1
        if nums1[eliminated_index] <= nums2[eliminated_index]:
            nums1 = nums1[eliminated_index+1:]
        else:
            nums2 = nums2[eliminated_index+1:]
        
        # update k, the number of elements to be eliminated next round
        k -= eliminated_length

        return self.solution_4_5_2(nums1, nums2, k)