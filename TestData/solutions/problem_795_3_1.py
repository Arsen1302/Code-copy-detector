class Solution:
    def solution_795_3_1(self, s: str, pairs: List[List[int]]) -> str:

        num_nodes = len(s)
        self.uf = UnionFind(num_nodes)
        for i,j in pairs:
            self.uf.solution_795_3_4(i,j)
        
        indexes_by_root = {}
        chars_by_root = {}
        for i in range(num_nodes):
            root = self.uf.solution_795_3_3(i)
            if root not in indexes_by_root:
                indexes_by_root[root] = [i]
                chars_by_root[root] = [s[i]]
            else:
                indexes_by_root[root].append(i)
                chars_by_root[root].append(s[i])
        
        result = [None] * num_nodes
        for root in indexes_by_root:
            sorted_characters = sorted(chars_by_root[root])
            for index, slot in enumerate(indexes_by_root[root]):
                result[slot] = sorted_characters[index]
                
        result = ''.join(result)
        return result

class UnionFind:
    def solution_795_3_2(self, n):
        self.parent = list(range(n))
        self.rank = [1] * n
        
        return
    
    def solution_795_3_3(self, x):
        if x == self.parent[x]:
            return x
        else:
            self.parent[x] = self.solution_795_3_3(self.parent[x])
            return self.parent[x]
    
    def solution_795_3_4(self, x, y):
        parent_x = self.solution_795_3_3(x)
        parent_y = self.solution_795_3_3(y)
        if parent_x != parent_y:
            if self.rank[parent_x]>=self.rank[parent_y]:
                self.parent[parent_y] = parent_x
                self.rank[parent_x] += self.rank[parent_y]
            else:
                self.parent[parent_x] = parent_y
                self.rank[parent_y] += self.rank[parent_x]
                
        return