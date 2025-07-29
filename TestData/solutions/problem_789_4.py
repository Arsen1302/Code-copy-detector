class Solution:
    def solution_789_4(self, text: str) -> int:
        counter = collections.Counter(text)
        counter['l'] //= 2
        counter['o'] //= 2
        return min(counter[c] for c in 'balon')