class Solution:
    def solution_445_4(self, letters: List[str], target: str) -> str:
        letters.sort()
        for i in letters:
            if (i>target):
                return i
        return letters[0]