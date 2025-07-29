class Solution:
    def solution_571_4(self, A: str, B: str) -> List[str]:
        return [k for k,v in Counter(A.split()+B.split()).items() if v==1]