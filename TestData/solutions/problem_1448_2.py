class Solution:
    def solution_1448_2(self, sentences: List[str]) -> int:
        mx=0
        for i in sentences:
            c=i.split()
            if len(c)>mx:
                mx=len(c)
        return mx