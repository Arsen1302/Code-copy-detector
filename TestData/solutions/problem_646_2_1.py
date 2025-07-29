class Solution:
    def solution_646_2_1(self, R: TreeNode) -> bool:
        def solution_646_2_2(n):
            if n == None: return True
            if n.val != R.val: return False
            return solution_646_2_2(n.left) and solution_646_2_2(n.right)
        return solution_646_2_2(R)
		
		
- Junaid Mansuri
- Chicago, IL