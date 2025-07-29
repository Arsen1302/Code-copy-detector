class Solution:
    def solution_1612_4(self, nums1: List[int], nums2: List[int], k1: int, k2: int) -> int:
      k = k1 + k2
      diff_data = [abs(x - y) for x,y in zip(nums1, nums2)]
      left, right = 0, max(diff_data)
      
      while left < right:
        mid = floor((left + right)/2)
        k_needed = sum([max(0, x - mid) for x in diff_data])
        if k_needed <= k:
          right = mid
        else:
          left = mid + 1
        
      if left == 0: return 0
      else:
        return sum([min(x, left)**2 for x in diff_data]) \
               - (left**2 - (left-1)**2)*(k - sum([max(0, x - left) for x in diff_data]))