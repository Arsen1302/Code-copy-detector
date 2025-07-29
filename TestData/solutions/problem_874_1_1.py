class Solution:
    def solution_874_1_1(self, R: TreeNode, t: int) -> TreeNode:
        def solution_874_1_2(R):
            if R == None: return None
            R.left, R.right = solution_874_1_2(R.left), solution_874_1_2(R.right)
            return None if R.val == t and R.left == R.right else R
        return solution_874_1_2(R)
		
		
- Junaid Mansuri
- Chicago, IL