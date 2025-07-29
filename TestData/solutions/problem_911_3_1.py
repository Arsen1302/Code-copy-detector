class Solution:
	def solution_911_3_1(self, root: Optional[TreeNode]) -> int:
		if not root: return 0
		self.res=0
		def solution_911_3_2(root,count,a):
			if root:
				if a=='r':
					if root.left:
						solution_911_3_2(root.left,count+1,'l')
					if root.right:
						solution_911_3_2(root.right,1,'r')
				else:
					if root.left:
						solution_911_3_2(root.left,1,'l')
					if root.right:
						solution_911_3_2(root.right,count+1,'r')
			self.res=max(self.res,count)

		if root.right:solution_911_3_2(root.right,1,'r');
		if root.left:solution_911_3_2(root.left,1,'l');
		return self.res