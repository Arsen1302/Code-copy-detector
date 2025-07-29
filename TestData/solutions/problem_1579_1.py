class Solution:
    def solution_1579_1(self, s: str, target: str) -> int:
        counter_s = Counter(s)        
        return min(counter_s[c] // count for c,count in Counter(target).items())