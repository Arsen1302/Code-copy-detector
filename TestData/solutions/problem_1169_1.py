class Solution:
    def solution_1169_1(self, rectangles: List[List[int]]) -> int:
        freq = {}
        for l, w in rectangles: 
            x = min(l, w)
            freq[x] = 1 + freq.get(x, 0)
        return freq[max(freq)]