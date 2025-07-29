class Solution:
    def solution_902_1_1(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        n = len(leftChild)
        
        # tree has 2 requirements
        # 1. every node has a single parent
        # 2. single root (only one node has NO parent)
        # 3. no cycle
        # 4. all nodes connected to each other (single component)
        
        parent = [-1] * n
        
        # checking condition (1. and 2.)
        for idx, (left, right) in enumerate(zip(leftChild, rightChild)):
            
            if left != -1:
                # FAILED: condition (1.)
                if parent[left] != -1: return False
                parent[left] = idx
                
            if right != -1:
                # FAILED: condition (1.)
                if parent[right] != -1: return False
                parent[right] = idx
        
        # FAILED condition (2.)
        if parent.count(-1) != 1: return False
            
        # checking condition (3. and 4.)
        vis = set()
        def solution_902_1_2(u):
            if u in vis:
                return True
            else:
                vis.add(u)
            
            for kid in [leftChild[u], rightChild[u]]:
                if kid != -1:
                    if solution_902_1_2(kid): return True
            
        # FAILED condition (3.) - found a cycle
        if solution_902_1_2(parent.index(-1)): return False
        
        # FAILED condition (4.) - DFS did not visit all nodes!
        if len(vis) != n: return False
        
        # did not FAIL any condition, success ;)
        return True

"""
Tricky test case (cycle and not connected):
4
[1,-1,3,-1]
[2,-1,-1,-1]

"""