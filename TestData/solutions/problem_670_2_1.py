class Solution:
    def solution_670_2_1(self, equations: List[str]) -> bool:
        """
        Time: O(N), Space: O(N)
        """
        parent = {}
        
        def solution_670_2_2(c1, c2):
            pc1 = solution_670_2_3(c1)
            pc2 = solution_670_2_3(c2)
            if pc1 == pc2:
                return
            parent[pc2] = pc1
        
        def solution_670_2_3(c):
            if not parent.get(c):
                parent[c] = c
                return c
            if parent[c] == c:
                return c
            
            return solution_670_2_3(parent[c])
        
        # First make the disjoint sets by traversing the equals
        for eq in equations: 
            if eq[1] == '=':
                x, y = eq[0], eq[3]
                solution_670_2_2(x, y)
        
        # for all inequalities, their parents must be different
        for eq in equations:
            if eq[1] == '!':
                if solution_670_2_3(eq[0]) == solution_670_2_3(eq[3]):
                    return False
        return True