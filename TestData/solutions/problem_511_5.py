class Solution:
    def solution_511_5(self, arr: List[int]) -> int:
        freq = {}
        for x in sorted(arr): 
            freq[x] = 1
            for xx in freq: 
                freq[x] += freq[xx] * freq.get(x/xx, 0)
        return sum(freq.values()) % 1_000_000_007