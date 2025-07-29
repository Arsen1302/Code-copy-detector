class Solution:
    def solution_857_3_1(self, R1: TreeNode, R2: TreeNode) -> List[int]:
        A = []
        def solution_857_3_2(T):
            A.append(T.val)
            if T.left != None: solution_857_3_2(T.left)
            if T.right != None: solution_857_3_2(T.right)
        if R1 != None: solution_857_3_2(R1)
        if R2 != None: solution_857_3_2(R2)
        return sorted(A)
        
		
- Junaid Mansuri
- Chicago, IL