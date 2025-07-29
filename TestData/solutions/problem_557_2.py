class Solution:
    def solution_557_2(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n = len(nums1)
        nums2_hq_desc = []
        for i, num in enumerate(nums2):
            # need to negate num to sort in descending order
            heapq.heappush(nums2_hq_desc, (-num, i))
        nums1.sort()
        
        res = [0] * n
        left, right = 0, n-1 # two pointers on the sorted nums1 array
        
        while (left <= right):
            max2 = heapq.heappop(nums2_hq_desc)
            maxVal2, idx2 = max2
            # need to negate again to make num positive
            maxVal2 = -maxVal2
            if (maxVal2 < nums1[right]):
                # use current num to compete when it's stronger than maxVal2
                res[idx2] = nums1[right]
                right -= 1
            else:
                # use the weakest num to compete when maxVal2 >= nums[right]
                res[idx2] = nums1[left]
                left += 1
            
        return res