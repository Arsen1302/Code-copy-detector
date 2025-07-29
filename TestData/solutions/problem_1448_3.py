class Solution:
    def solution_1448_3(self, sentences: List[str]) -> int:
        return max([len(i.split()) for i in sentences])