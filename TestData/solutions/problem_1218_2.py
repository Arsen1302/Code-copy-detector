class Solution:
    def solution_1218_2(self, edges: List[List[int]]) -> int:
        if edges[0][0] in edges[1]: return edges[0][0]
        return edges[0][1]