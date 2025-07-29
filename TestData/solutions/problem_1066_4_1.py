class Solution:
    def solution_1066_4_1(self, nums1: List[int], nums2: List[int]) -> int:
        cnt1, cnt2 = Counter(nums1), Counter(nums2)
        
        def solution_1066_4_2(x, y, freq): 
            """Return count of triplet of nums[i]**2 = nums[j]*nums[k]."""
            ans = 0
            for xx in x: 
                xx *= xx
                ans += sum(freq[xx//yy] - (yy == xx//yy) for yy in y if not xx%yy and xx//yy in freq)
            return ans//2

        return solution_1066_4_2(nums1, nums2, cnt2) + solution_1066_4_2(nums2, nums1, cnt1)