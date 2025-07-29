class Solution:
	def solution_314_2(self, root: TreeNode) -> int:
		queue, result, diff = deque([root]), [], float("inf")

		while queue:
			curNode = queue.popleft()

			result.append(curNode.val)

			if curNode.left:
				queue.append(curNode.left)

			if curNode.right:
				queue.append(curNode.right)

		result.sort()
		for i in range(len(result)-1):
			if abs(result[i+1] - result[i]) < diff: diff = abs(result[i+1] - result[i])

		return diff