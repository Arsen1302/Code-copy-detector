class Solution:
    def solution_1243_4(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        count = [[] for each in range(len(queries))]
        for i in range(len(queries)):
            for j in range(len(points)):
                x = queries[i][0]
                y = queries[i][1]
                r = queries[i][2]
                c = pow(x-points[j][0],2) + pow(y-points[j][1],2) - pow(r,2)
                if c <= 0:
                    count[i].append(1)
        for i in range(len(count)):
            count[i] = sum(count[i])
        return count