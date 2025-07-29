class Solution:
    def solution_789_3(self, text: str) -> int:
        # Counts the frequency of each character in text
        seen = collections.Counter(text)
        
        # The minimum number of Balloons can be no more than the least frequent character
        return min(seen['b'], seen['a'], seen['l']//2, seen['o']//2, seen['n'])