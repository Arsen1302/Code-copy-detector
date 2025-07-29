class Solution:
    def solution_1348_3(self, word: str) -> int:
        count = 0
        prev = 0
        for idx in map(lambda c: ord(c) - ord('a'), word):
            distance = abs(idx-prev)
            count += 1 + min(distance, 26-distance)
            prev = idx
            
        return count