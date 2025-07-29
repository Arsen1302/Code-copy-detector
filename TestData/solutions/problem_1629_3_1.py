class Solution:
    def solution_1629_3_1(self, edges: List[int], node1: int, node2: int) -> int:
        n = len(edges)

        def solution_1629_3_2(start: int) -> list:
            res = [inf] * n
            res[start] = 0
            next_node = edges[start]
            count = 1
            while (next_node != -1 and
                   count < res[next_node]):
                res[next_node] = count
                next_node = edges[next_node]
                count += 1
            return res

        ans, min_max_d = -1, inf
        for i, (a, b) in enumerate(zip(solution_1629_3_2(node1),
                                       solution_1629_3_2(node2))):
            if (distance := max(a, b)) < min_max_d:
                ans = i
                min_max_d = distance

        return ans