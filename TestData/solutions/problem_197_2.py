class Solution:
    def solution_197_2(self, n: int) -> List[int]:
        return sorted(list(map(str,list(range(1,n+1)))))