class Solution:
			def solution_857_5_1(self, root1: TreeNode, root2: TreeNode) -> List[int]:
				result = []

				def solution_857_5_2(root: TreeNode):
					if root:
						solution_857_5_2(root.left)
						result.append(root.val)
						solution_857_5_2(root.right)

				solution_857_5_2(root1)
				solution_857_5_2(root2)

				return sorted(result)