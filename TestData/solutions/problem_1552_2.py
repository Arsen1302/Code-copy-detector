class Solution:
    def solution_1552_2(self, flowers: List[List[int]], persons: List[int]) -> List[int]:
        all_points = sorted([(x, 0) for x in persons] + [(x, -1) for x, _ in flowers] + [(x, 1) for _, x in flowers])
        results = {}
        cnt = 0
        for x, t in all_points:
            if t == -1:
                cnt += 1
            elif t == 1:
                cnt -= 1
            else:
                results[x] = cnt
        return [results[p] for p in persons]