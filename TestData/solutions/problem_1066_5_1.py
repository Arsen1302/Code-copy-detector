class Solution:
    # two-sum. search for nums1[i]^2/nums2[k]
    # O(mn) time : O(m + n) space
    def solution_1066_5_1(self, nums1: List[int], nums2: List[int]) -> int:
        def solution_1066_5_2(arr1, arr2):
            res = 0
            for n1 in arr1:
                n2_freq = defaultdict(int)
                for n2 in arr2:
                    if n1*n1 / n2 in n2_freq:
                        res += n2_freq[n1*n1 / n2]
                    n2_freq[n2] += 1
            return res
        return solution_1066_5_2(nums1, nums2) + solution_1066_5_2(nums2, nums1)