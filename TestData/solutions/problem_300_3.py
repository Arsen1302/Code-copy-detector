class Solution:
		def solution_300_3(self, root: Optional[TreeNode]) -> List[int]:
			if root is None:
				return []

			queue = [root]
			level_order = []

			while queue:
				len_queue = len(queue)
				level = []

				for _ in range(len_queue):
					node = queue.pop(0)

					if node.left:
						queue.append(node.left)

					if node.right:
						queue.append(node.right)

					level.append(node.val)

				level_order.append(level)

			result = []
			for level in level_order:
				result.append(max(level))

			return result