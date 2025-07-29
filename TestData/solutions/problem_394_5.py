class Solution:
	def solution_394_5(self, root: TreeNode) -> int:
		queue, result = deque([root]), []

		while queue:
			curNode = queue.popleft()

			result.append(curNode.val)

			if curNode.left:
				queue.append(curNode.left)

			if curNode.right:
				queue.append(curNode.right)

		result.sort()

		if result[-1] == result[0]:
			return -1

		else:
			for i in range(len(result)-1):
				if result[i] < result[i+1]:
					return result[i+1]