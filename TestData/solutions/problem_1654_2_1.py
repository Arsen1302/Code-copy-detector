class Solution:
    def solution_1654_2_1(self, n: int, rowC: List[List[int]], colC: List[List[int]]) -> List[List[int]]:
		# create two graphs, one for row and one for columns
        row_adj = {i: [] for i in range(1, n + 1)}
        col_adj = {i: [] for i in range(1, n + 1)}
        for u, v in rowC:
            row_adj[u].append(v)
        for u, v in colC:
            col_adj[u].append(v)
            
        # inorder to do topological sort, we need to maintain two visit lists: one marks which node 
        # we have already processed (because not all nodes are connected to each other and we do not 
        # want to end up in a infinite loop), the other one marks nodes we are currently visiting(or in 
        # our recursion stack). If we visit a node that we are currently visiting, that means there is 
        # a loop, so we return False; if it is not in our current visit but has already been visited, we 
        # can safely travel to the next node and return True. 

        row_stack = []
        row_visit = set()
        row_visiting = set()
        col_stack = []
        col_visit = set()
        col_visiting = set()
        
        def solution_1654_2_2(node, stack, visit, visiting, adj):
            if node in visiting:
                return False
            if node in visit:
                return True
            visit.add(node)
            visiting.add(node)
            for child in adj[node]:
                if not solution_1654_2_2(child, stack, visit, visiting, adj):
                    return False
            visiting.remove(node)
            stack.append(node)
            return True
        
        # do solution_1654_2_2 on each row/col graph
        for i in range(1, n + 1):
            if i not in row_visit:
                if not solution_1654_2_2(i, row_stack, row_visit, row_visiting, row_adj):
                    return []
            if i not in col_visit:
                if not solution_1654_2_2(i, col_stack, col_visit, col_visiting, col_adj):
                    return []

		    

        # After the solution_1654_2_2, we also need a stack to store which node has been entirely explored. That's why we 
        # append the current node to our stack after exploring all its neighbors. Remember we have to reverse 
        # the stack after all DFS's, because the first-explored node gets appended first. 
        row_stack, col_stack = row_stack[::-1], col_stack[::-1]
        
        
        # mark position for each element
        row_memo, col_memo = {}, {}
        for idx, num in enumerate(row_stack):
            row_memo[num] = idx
        for idx, num in enumerate(col_stack):
            col_memo[num] = idx
            
        # create an empty matrix as our ans
        ans = [[0]*n for _ in range(n)]
        
        # plug in values from what we have discovered
        for i in range(1, n + 1):
            ans[row_memo[i]][col_memo[i]] = i
        return ans