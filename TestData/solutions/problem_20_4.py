class Solution:
			def solution_20_4(self, root: Optional[TreeNode]) -> List[List[int]]:
				result = []
				if root is None:
					return result

				queue = [root]
				while queue:
					level = []
					size = len(queue)

					for _ in range(size):
						node = queue.pop(0)

						if node.left:
							queue.append(node.left)

						if node.right:
							queue.append(node.right)

						level.append(node.val)

					result.append(level)

				return result[::-1]