class Solution:
    def solution_870_5_1(self, n: int, connections: List[List[int]]) -> int:
        #Check the numbers of cables 
        if n>len(connections)+1:
            return -1
        uf=UnionFind(n)
        for [x,y] in connections:
            uf.solution_870_5_4(x,y)
        return uf.groups-1
# UnionFind class
class UnionFind:
    def solution_870_5_2(self, size):
        self.root = [i for i in range(size)]
        self.groups=size

    def solution_870_5_3(self, x):
        if x == self.root[x]:
            return x
        self.root[x] = self.solution_870_5_3(self.root[x])
        return self.root[x]
    def solution_870_5_4(self, x, y):
        rootX = self.solution_870_5_3(x)
        rootY = self.solution_870_5_3(y)
        if rootX != rootY:
            self.root[rootY] = rootX
            self.groups-=1