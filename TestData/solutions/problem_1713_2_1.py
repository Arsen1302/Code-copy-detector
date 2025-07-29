class Solution:
    def solution_1713_2_1(self, robot: List[int], factory: List[List[int]]) -> int:        
        robot.sort()
        factory.sort()
        cap = []
        for x, limit in factory:
            cap.extend([x] * limit)
        m = len(robot)
        n = len(cap)
        indices = list(range(m))
        ans = sum(abs(x - y) for x, y in zip(robot, cap))
        
        def solution_1713_2_2(i):
            diff = 0
            while i < m:
                if indices[i] + 1 < n:
                    diff -= abs(robot[i] - cap[indices[i]])
                    diff += abs(robot[i] - cap[indices[i] + 1])
                else:
                    return math.inf, i + 1
                if i + 1 < m and indices[i] + 1 == indices[i + 1]:
                    i += 1
                else:
                    return diff, i + 1
        for i in reversed(range(m)):
            while True:
                diff, j = solution_1713_2_2(i)
                if diff <= 0:
                    ans += diff
                    for x in range(i, j):
                        indices[x] += 1
                else:
                    break
        return ans