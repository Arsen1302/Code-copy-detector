class Solution:
    def solution_933_2(self, s: str, k: int) -> bool:
        freq = {}
        for c in s: 
		    freq[c] = 1 + freq.get(c, 0)
        return sum(freq[c]&amp;1 for c in freq) <= k <= len(s)