class Solution:
    def solution_26_1_1(self, R: TreeNode, S: int) -> List[List[int]]:
        A, P = [], []
        def solution_26_1_2(N):
            if N == None: return
            P.append(N.val)
            if (N.left,N.right) == (None,None) and sum(P) == S: A.append(list(P))
            else: solution_26_1_2(N.left), solution_26_1_2(N.right)
            P.pop()
        solution_26_1_2(R)
        return A
		
		
- Junaid Mansuri
- Chicago, IL