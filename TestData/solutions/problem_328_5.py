class Solution:
    def solution_328_5(self, wall: List[List[int]]) -> int:
        ans = {}
        for list in wall:
            gap = 0
            for i in range(len(list)-1):
                gap += list[i]
                if gap in ans:
                    ans[gap] += 1
                else:
                    ans[gap] = 1

        res = ans.values()
        return len(wall)-max(res, default=0)