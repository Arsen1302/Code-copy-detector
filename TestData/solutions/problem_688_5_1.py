class Solution:
	def solution_688_5_1(self, preorder: List[int]) -> Optional[TreeNode]:

		inorder = sorted(preorder)
		dic = {val:i for i,val in enumerate(inorder)}

		def solution_688_5_2(l,r):
			if l>=r:
				return
			
			val = preorder.pop(0)
			ind = dic[val]
			root = TreeNode(val)
			
			root.left = solution_688_5_2(l,ind)
			root.right= solution_688_5_2(ind+1,r)
			return root

		return solution_688_5_2(0,len(inorder))