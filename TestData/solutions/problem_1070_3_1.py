class Solution:
    def solution_1070_3_1(self, points: List[List[int]]) -> int:

        if len(points) <= 1:
            return 0
        
        graph = self.solution_1070_3_2(points)
        graph.sort(key=lambda x: x[2])
        
        n = len(points)
        uf = UnionFind(n)
        
        result = 0
        count = 0
        
        for i in graph:
            vertex, node, cost = i
        
            if count == n - 1:
                break
            
            if uf.solution_1070_3_6(vertex, node):
                result += cost
                count += 1
            else:
                continue
        
        return result

    def solution_1070_3_2(self, points):
        graph = []
  
        for i in range(len(points) - 1):
            for j in range(i + 1, len(points)):
                
                curr_point = points[i]
                next_point = points[j]
                result = self.solution_1070_3_3(curr_point[0], curr_point[1],
                                        next_point[0], next_point[1])
                
                graph.append([i, j, result])

        return graph
    
    def solution_1070_3_3(self, a, b, c, d):
        return abs(a - c) + abs(b - d)


class UnionFind:
    def solution_1070_3_4(self, size):
        self.root = [i for i in range(size)]
        self.rank = [1 for _ in self.root]
    
    def solution_1070_3_5(self, vertex):
        if vertex == self.root[vertex]:
            return vertex
        self.root[vertex] = self.solution_1070_3_5(self.root[vertex])
        return self.root[vertex]
    
    def solution_1070_3_6(self, v1, v2):
        root1 = self.solution_1070_3_5(v1)
        root2 = self.solution_1070_3_5(v2)
        
        if root1 != root2:
            if self.rank[root1] > self.rank[root2]:
                self.root[root2] = root1
            elif self.rank[root1] < self.rank[root2]:
                self.root[root1] = root2
            else:
                self.root[root2] = root1
                self.rank[root1] += 1
            
            return True
        
        else:
            return False