class Solution:
    def solution_448_3(self, licensePlate: str, words: List[str]) -> str:
        l, mx, ans = ''.join([x.lower() for x in licensePlate if x.isalpha()]), 0, ''
        for word in words:
            sumChars = sum([min(word.count(char),l.count(char)) for char in set(l)])
            if sumChars > mx or (sumChars == mx and len(word) < len(ans)): mx, ans = sumChars, word
        return ans