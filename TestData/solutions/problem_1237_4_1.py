class Solution:
    def solution_1237_4_1(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        total = 0 
        for i in range(n):
            total += abs(nums1[i] - nums2[i])
            
        s = sorted(nums1)
        def solution_1237_4_2(x):
            left, right = 0, n-1
            while left < right:
                mid = (left + right) // 2
                if s[mid] >= x:
                    right = mid
                else:
                    left = mid + 1
            if left == 0:
                return s[left]-x
            else:
                return min(abs(s[left]-x), abs(x-s[left-1]))
        
        res = float('inf')
        for i in range(n):
            t = total - abs(nums1[i]-nums2[i])
            c = solution_1237_4_2(nums2[i])
            res = min(res, t + c)
        
        
        return min(res, total) % (10**9 + 7)