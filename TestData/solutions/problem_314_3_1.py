class Solution:
	def solution_314_3_1(self):
		self.min = 10000
		self.l = []
	def solution_314_3_2(self, root: TreeNode) -> int:
		self.solution_314_3_3(root)
		self.l.sort()
		for i in range(len(self.l)-1):
			if self.l[i+1] - self.l[i] < self.min:
				self.min = self.l[i+1] - self.l[i]
		return self.min

	def solution_314_3_3(self, root: TreeNode):
		if root == None:
			return
		self.l.append(root.val)
		self.solution_314_3_3(root.left)
		self.solution_314_3_3(root.right)