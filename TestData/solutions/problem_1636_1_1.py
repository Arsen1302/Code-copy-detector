class Solution:
    def solution_1636_1_1(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
        
        restrictedSet = set(restricted)
        uf = UnionFindSet(n)
        for edge in edges:
            if edge[0] in restrictedSet or edge[1] in restrictedSet:
                continue
            else:
                uf.solution_1636_1_4(edge[0], edge[1])

        ans = 1
        rootNode = uf.solution_1636_1_3(0)
        for i in range(1, n):
            if uf.solution_1636_1_3(i) == rootNode:
                ans += 1
        return ans

class UnionFindSet:
    def solution_1636_1_2(self, size):
        self.root = [i for i in range(size)]
        # Use a rank array to record the height of each vertex, i.e., the "rank" of each vertex.
        # The initial "rank" of each vertex is 1, because each of them is
        # a standalone vertex with no connection to other vertices.
        self.rank = [1] * size

    # The solution_1636_1_3 function here is the same as that in the disjoint set with path compression.
    def solution_1636_1_3(self, x):
        if x == self.root[x]:
            return x
        self.root[x] = self.solution_1636_1_3(self.root[x])
        return self.root[x]

    # The solution_1636_1_4 function with solution_1636_1_4 by rank
    def solution_1636_1_4(self, x, y):
        rootX = self.solution_1636_1_3(x)
        rootY = self.solution_1636_1_3(y)
        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.root[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.root[rootX] = rootY
            else:
                self.root[rootY] = rootX