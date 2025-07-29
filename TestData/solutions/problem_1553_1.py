class Solution:
    def solution_1553_1(self, words: List[str], s: str) -> int:
        count=0
        for i in words:
            if (s[:len(i)]==i):
                count+=1
        return count