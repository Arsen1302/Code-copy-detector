class Solution:
    def solution_1713_4_1(self, robot: List[int], factory: List[List[int]]) -> int:
        robot.sort()
        factory.sort()
        m, n = len(robot), len(factory)
        
        @lru_cache(None)
        def solution_1713_4_2(i, j, k):
            if i >= m:  # all robots fixed
                return 0
            if j >= n:  # not all robots get fixed but run out of factories.
                return math.inf
            if k <= 0:  # the factory uses up repair limit
                if j + 1 < n: # use next factory if it's valid
                    return solution_1713_4_2(i, j + 1, factory[j + 1][1])
                else: # no more factory to use, return inf
                    return math.inf
            dist = abs(robot[i] - factory[j][0]) # cost to use current factory
            # Use current factory or skip it
            return min(dist + solution_1713_4_2(i + 1, j, k - 1), solution_1713_4_2(i, j, -1))
        
        return solution_1713_4_2(0, 0, factory[0][1])