class Solution:
    def solution_448_2(self, licensePlate: str, words: List[str]) -> str:
        req = Counter(filter(str.isalpha, licensePlate.lower()))
        words.sort(key=len)
        for count, word in zip(map(Counter, words), words):
            if count >= req:
                return word