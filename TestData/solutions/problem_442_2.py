class Solution:
    def solution_442_2(self, nums: List[int]) -> int:
        freq = Counter(nums)
        prev = -inf 
        f0 = f1 = 0
        for x in sorted(freq): 
            if prev + 1 == x: f0, f1 = max(f0, f1), f0 + x*freq[x]
            else: f0, f1 = max(f0, f1), max(f0, f1) + x*freq[x]
            prev = x
        return max(f0, f1)