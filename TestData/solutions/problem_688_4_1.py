class Solution:
	def solution_688_4_1(self, preorder: List[int]) -> Optional[TreeNode]:
		inorder = sorted(preorder)
		def solution_688_4_2(inorder):
			if len(inorder)==0:
				return

			val = preorder.pop(0)
			ind = inorder.index(val)
			root = TreeNode(val)

			root.left = solution_688_4_2(inorder[:ind])
			root.right= solution_688_4_2(inorder[ind+1:])
			return root
    
    return solution_688_4_2(inorder)