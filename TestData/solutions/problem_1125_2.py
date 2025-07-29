class Solution:
    def solution_1125_2(self, tasks: List[List[int]]) -> int:
        tasks.sort(key=lambda x: x[0]-x[1])
        ans = cur = 0
        for cost, minimum in tasks:
            ans = min(cur-minimum, ans)
            cur -= cost
        return -ans