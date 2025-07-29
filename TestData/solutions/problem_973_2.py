class Solution:
    def solution_973_2(self, text: str) -> str:
        a = []
        for x in text.split(" "):
            a.append(x.lower())
        return " ".join(sorted(a, key=len)).capitalize()