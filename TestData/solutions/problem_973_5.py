class Solution:
    def solution_973_5(self, text: str) -> str:
        return " ".join(sorted(text.split(),key=lambda x:len(x))).capitalize()