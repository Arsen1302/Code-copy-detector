class Solution:
	def solution_646_4(self, root: TreeNode) -> bool:
		queue, Unival = deque([root]), root.val

		while queue:
			curNode = queue.popleft()

			if curNode.val != Unival: return False

			if curNode.left: 
				queue.append(curNode.left)

			if curNode.right:
				queue.append(curNode.right)

		return True