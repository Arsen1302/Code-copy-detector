class Solution:
    def solution_382_3_1(self, root: Optional[TreeNode]) -> List[List[str]]:
        def solution_382_3_2(node,c):
            if not node:
                return c
            return max(solution_382_3_2(node.left,c+1),solution_382_3_2(node.right,c+1))
        self.solution_382_3_2 = solution_382_3_2(root,-1)
        m = self.solution_382_3_2 + 1
        n = 2**(self.solution_382_3_2+1)-1
        self.mat = []
        for i in range(m):
            z = []
            for j in range(n):
                z.append("")
            self.mat.append(z)
        def solution_382_3_3(node,row,col,mat,solution_382_3_2):
            if node:
                if node.left:
                    mat[row+1][col-2**(solution_382_3_2-row-1)] = str(node.left.val)
                    solution_382_3_3(node.left,row+1,col-2**(solution_382_3_2-row-1),mat,solution_382_3_2)
                if node.right:
                    mat[row+1][col+2**(solution_382_3_2-row-1)] = str(node.right.val)
                    solution_382_3_3(node.right,row+1,col+2**(solution_382_3_2-row-1),mat,solution_382_3_2)
        self.mat[0][(n-1)//2] = str(root.val)
        solution_382_3_3(root,0,(n-1)//2,self.mat,self.solution_382_3_2)
        return self.mat