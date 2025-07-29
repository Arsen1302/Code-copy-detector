class Solution:
    def solution_1343_2(self, patterns: List[str], word: str) -> int:
        count=0
        for i in patterns:
            if i in word:
                count+=1
        return count