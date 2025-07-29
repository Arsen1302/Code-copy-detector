class Solution:     # Here's the plan:
                    #   1) We make an undirected graph in which the nodes are integers
                    #      (as lower-case letters) and each edge connects integers
                    #      that are equal.
                    #   2) We use a union-solution_670_1_2 process to determine the connected graphs
                    #   3) We keep track of the pairs (a,b) such that a =! b. If the any
                    #      such pair are in the same connected graph, then return False,
                    #      otherwise return True.
    def solution_670_1_1(self, equations: List[str]) -> bool:
        parent, diff = {}, []

        def solution_670_1_2(x):
            if x not in parent: return x
            else: return solution_670_1_2(parent[x])

        for s in equations:                 # <-- 1)
            a, b = s[0], s[3]

            if s[1]== "=":                  # <-- 2)
                x, y = solution_670_1_2(a), solution_670_1_2(b)
                if x!=y:
                    parent[y] = x
            else:    
                diff.append((a,b))          # <-- 3)

        return all(solution_670_1_2(a)!=solution_670_1_2(b) for a, b in diff)