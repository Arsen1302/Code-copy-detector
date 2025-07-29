class Solution:
    def solution_1237_2(self, nums1: List[int], nums2: List[int]) -> int:
        nums1, nums2 = zip(*sorted(zip(nums1, nums2)))
        mad = [abs(nums1[i] - nums2[i]) for i in range(len(nums1))]
        M = sum(mad)
        MOD = 10**9 + 7
        best = 0
        for i in range(len(nums1)):
            if nums1[i] != nums2[i]:
                j = bisect.bisect_left(nums1, nums2[i])
                if j == len(nums1):
                    best = max(best, mad[i] - abs(nums1[-1] - nums2[i]))
                elif j == 0:
                    best = max(best, mad[i] - abs(nums1[0] - nums2[i]))
                else:
                    new = min(abs(nums1[j] - nums2[i]), abs(nums1[j-1] - nums2[i]))
                    best = max(best, mad[i] - new)
        return (M - best) % MOD