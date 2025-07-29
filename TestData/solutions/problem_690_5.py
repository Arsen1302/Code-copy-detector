class Solution:
    def solution_690_5(self, time: List[int]) -> int:
        map = defaultdict(int)
        ans = 0
        for t in time:
            if t % 60 == 0:
                t = 60
                ans += map[60]
            else:
                t = t % 60
                ans += map[60-t]
            map[t] += 1
        return ans