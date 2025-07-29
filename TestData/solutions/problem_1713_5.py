class Solution:
    def solution_1713_5(self, robot: List[int], factory: List[List[int]]) -> int:

        m = len(robot)
        n = len(factory)

        factory.sort()
        robot.sort()

        opt = [[float('inf') for j in range(n + 1)] for i in range(m + 1)]

        for j in range(n + 1):
            opt[0][j] = 0

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                cur = 0
                for x in range(min(factory[j - 1][1], i) + 1):
                    opt[i][j] = min(opt[i][j], opt[i-x][j-1] + cur)
                    cur += abs(factory[j-1][0] - robot[i-1-x])

        return opt[-1][-1]