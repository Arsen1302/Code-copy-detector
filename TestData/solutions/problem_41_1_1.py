class Node:
    def solution_41_1_1(self, val):
        self.val = val
        self.parent = self
        self.size = 1
    
class UnionFind:
        
    def solution_41_1_2(self, node):
        if node.parent != node:
            node.parent = self.solution_41_1_2(node.parent)
        return node.parent
    
    def solution_41_1_3(self, node1, node2):
        parent_1 = self.solution_41_1_2(node1)
        parent_2 = self.solution_41_1_2(node2)
        if parent_1 != parent_2:
            parent_2.parent = parent_1
            parent_1.size += parent_2.size
        return parent_1.size
                
        
        
class Solution:
    def solution_41_1_4(self, nums: List[int]) -> int:
        uf = UnionFind()
        nodes = {}
        max_size = 0
        for num in nums:
            if num not in nodes:
                node = Node(num)
                nodes[num] = node
                size = 1
                if num + 1 in nodes:
                    size = uf.solution_41_1_3(node, nodes[num+1])
                if num - 1 in nodes:
                    size = uf.solution_41_1_3(node, nodes[num-1])
                max_size = max(max_size, size)
                
        return max_size
		```