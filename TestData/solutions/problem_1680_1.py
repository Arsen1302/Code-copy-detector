class Solution:
    def solution_1680_1(self, nums1: List[int], nums2: List[int]) -> int:
        m, n = map(len, (nums1, nums2))
        return (m % 2 * reduce(xor, nums2)) ^ (n % 2 * reduce(xor, nums1))