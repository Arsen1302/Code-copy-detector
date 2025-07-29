class Solution:
	def solution_702_5(self, root: TreeNode) -> int:
		queue, total = deque([(root, [root.val], 0)]), 0

		while queue:
			curNode, curpath, length = queue.popleft()

			if not curNode.left and not curNode.right:
				for val in curpath:
					if val == 1: 
						total += 2 ** length 
					length -= 1

			if curNode.left:
				queue.append((curNode.left, curpath + [curNode.left.val], length + 1))

			if curNode.right:
				queue.append((curNode.right, curpath + [curNode.right.val], length + 1))

		return total