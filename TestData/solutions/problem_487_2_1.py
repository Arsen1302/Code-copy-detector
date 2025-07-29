class Solution(object):
    def solution_487_2_1(self):
        self.memo = {}
    def solution_487_2_2(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """
        self.memo = {len(graph)-1:[[len(graph)-1]]}
        def solution_487_2_3(N):
            if N in self.memo:
                return self.memo[N]
            a = []
            for n in graph[N]:
                for path in solution_487_2_3(n):
                    a.append([N]+path)
            self.memo[N] = a
            return a
        return solution_487_2_3(0)