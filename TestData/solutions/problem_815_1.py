class Solution:
    def solution_815_1(self, n: int, start: int) -> List[int]:
        ans = []
        for i in range(1<<n): 
            ans.append(start ^ i ^ i >> 1)
        return ans