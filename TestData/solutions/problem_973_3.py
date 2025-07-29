class Solution:
    def solution_973_3(self, text: str) -> str:
        return " ".join(sorted(text.split(" "), key=len)).capitalize()