class Solution:
    def solution_1137_5(self, allowed: str, words: List[str]) -> int:
        count = 0
        allowed = set(allowed)
        for i in words:
            for letter in i:
                if letter not in allowed: 
                    count += 1
                    break
        return len(words) - count