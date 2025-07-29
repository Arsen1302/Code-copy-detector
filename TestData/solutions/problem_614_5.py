class Solution:
    def solution_614_5(self, n: int) -> List[int]:
        ans = [1]
        while len(ans) < n: 
            ans = [2*x-1 for x in ans] + [2*x for x in ans]
        return [x for x in ans if x <= n]