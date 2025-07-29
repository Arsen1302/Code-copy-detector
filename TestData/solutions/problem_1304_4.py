class Solution:
    def solution_1304_4(self, nums: List[int]) -> int:
        # even: max alternating sum of an even-length subsequence
        # odd: max alternating sum of an odd-length subsequence
        even = odd = 0      
        for num in nums:
            even, odd = max(even, odd-num), max(odd, even+num)
        return max(even, odd)