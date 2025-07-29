class Solution:
    def solution_128_1_1(self, R: TreeNode) -> List[str]:
        A, P = [], []
        def solution_128_1_2(N):
            if N == None: return
            P.append(N.val)
            if (N.left,N.right) == (None,None): A.append('->'.join(map(str,P)))
            else: solution_128_1_2(N.left), solution_128_1_2(N.right)
            P.pop()
        solution_128_1_2(R)
        return A
		
		
- Junaid Mansuri
- Chicago, IL