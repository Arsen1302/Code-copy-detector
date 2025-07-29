class Solution:
    def solution_577_3_1(self, words: List[str], pattern: str) -> List[str]:
        pattern = self.solution_577_3_2(pattern)
        return [word for word in words if self.solution_577_3_2(word) == pattern]
        
    def solution_577_3_2(self, word):
        ch2Digit = {}
        digits = []
        for ch in word:
            if ch not in ch2Digit: ch2Digit[ch] = len(ch2Digit)
            digits.append(ch2Digit[ch])
        return digits