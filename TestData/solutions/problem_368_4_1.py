class Solution:
	def solution_368_4_1(self, root: TreeNode) -> List[float]:
		if root is not None:
			output = []
			depth = 0
			def solution_368_4_2(node, depth):
				depth += 1
				if len(output) < depth:
					output.append([])
				output[depth - 1].append(node.val)
				if node.left is not None:
					solution_368_4_2(node.left, depth)
				if node.right is not None:
					solution_368_4_2(node.right, depth)
			solution_368_4_2(root, depth)
			return [sum(x)/len(x) for x in output]
		else:
			return []