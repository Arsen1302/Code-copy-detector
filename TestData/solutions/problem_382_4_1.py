class Solution:
    def solution_382_4_1(self, root: Optional[TreeNode]) -> List[List[str]]:
        # GET HEIGHT OF THE TREE
        def solution_382_4_2(node, count):
            if not node: return count
            return max(solution_382_4_2(node.left, count+1), solution_382_4_2(node.right, count+1))
        height = solution_382_4_2(root, -1)
        
        # m and n IS PROVIDED FORMULA FROM PROBLEM DESCRIPTION
        m = height + 1
        n = (2 ** (m)) - 1
        
        # CREATE RESULT
        result = [["" for x in range(0, n)] for x in range(0, m)]

        # r and c IS PROVIDED FORMULA FROM PROBLEM DESCRIPTION
        r = 0
        c = (n-1) // 2
        
        # FILL THE RESULT WITH DFS TRAVERSAL
        # lc and rc IS PROVIDED FORMULA FROM DESCRIPTION
        def solution_382_4_3(node, r, c):
            if not node: return
            
            result[r][c] = str(node.val)
            
            
            if node.left:
                lc = c - (2 ** (height - r - 1))
                solution_382_4_3(node.left, r+1, lc)
                
            if node.right:
                rc = c + (2 ** (height - r - 1))
                solution_382_4_3(node.right, r+1, rc)
                
        solution_382_4_3(root, r, c)

        return result