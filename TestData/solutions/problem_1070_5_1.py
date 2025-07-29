class Solution:
    def solution_1070_5_1(self, points):
        return tuple(tuple(point) for point in points)
    
    def solution_1070_5_2(self, x, y):
        return abs(y[0]-x[0])+abs(y[1]-x[1])
    
    def solution_1070_5_3(self, pointsTuple, length):
        edges = []
        for point1 in range(length-1):
            for point2 in range(point1+1,length):
                dist = self.solution_1070_5_2(pointsTuple[point1], pointsTuple[point2])
                edges.append((pointsTuple[point1], pointsTuple[point2], dist))
        return edges

    def solution_1070_5_4(self, points: List[List[int]]) -> int:
        def solution_1070_5_5(parent, node):
            if node != parent[node]:
                parent[node] = solution_1070_5_5(parent, parent[node])
            return parent[node]
        
        def solution_1070_5_6(parent, rank, parent1, parent2):
            if rank[parent2] > rank[parent1]:
                parent[parent1] = parent2
                rank[parent2] += rank[parent1]
            else:
                parent[parent2] = parent1
                rank[parent1] += rank[parent2]
        
        pointsTuple = self.solution_1070_5_1(points)
        length = len(pointsTuple)
        edges = self.solution_1070_5_3(pointsTuple, length)
        edges.sort(key=lambda x:x[2])
        
        parent, rank, visited, current, mincost = {}, {}, 0, 0, 0
        for node in pointsTuple:
            parent[node] = node
            rank[node] = 1
        
        while visited < length - 1:
            node1, node2, cost = edges[current]
            current += 1
            parent1, parent2 = solution_1070_5_5(parent, node1), solution_1070_5_5(parent, node2)
            if parent1 != parent2:
                mincost += cost
                visited += 1
                solution_1070_5_6(parent, rank, parent1, parent2)

        return mincost