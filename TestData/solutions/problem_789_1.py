class Solution:
    def solution_789_1(self, text: str) -> int:
        c = collections.Counter(text)
        return min(c['b'],c['a'],c['l']//2,c['o']//2,c['n'])