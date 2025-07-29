class Solution:
	def solution_335_2_1(self, root: TreeNode) -> int:
		return self.solution_335_2_2(root)[1]

	def solution_335_2_2(self,root):
		if not root:
			return 0,0
		'''
		lvsum &amp; rvsum --> Sum of **values** all left and right children nodes respectively
		ltsum &amp; rtsum --> Sum of **tilt** of all left and right children nodes respectively  
		'''
		lvsum,ltsum = self.solution_335_2_2(root.left)
		rvsum,rtsum = self.solution_335_2_2(root.right)
		val_sum = root.val+lvsum+rvsum
		tilt_sum = ltsum + rtsum + abs(lvsum - rvsum)
		return val_sum,tilt_sum