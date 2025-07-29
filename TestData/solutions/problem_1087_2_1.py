class Solution:
		def solution_1087_2_1(self, root: Optional[TreeNode]) -> bool:
			if root is None:
				return False

			solution_1087_2_2 = self.solution_1087_2_2(root)

			# check level 0
			if solution_1087_2_2[0][0] % 2 == 0:
				return False

			# check level 1 ~ end
			for i, level in enumerate(solution_1087_2_2[1:], 2):
				if i % 2 == 0:
					# even and decreasing order
					previous_element = level[0]
					if previous_element % 2 != 0:
						return False

					for element in level[1:]:
						if element % 2 != 0 or previous_element < element:
							return False
						previous_element = element

				else:
					# odd and increasing order
					previous_element = level[0]
					if previous_element % 2 == 0:
						return False

					for element in level[1:]:
						if element % 2 == 0 or element < previous_element:
							return False
						previous_element = level

			return True

		def solution_1087_2_2(self, root: Optional[TreeNode]) -> List[List[int]]:
				queue = [root]
				solution_1087_2_2 = []
				while queue:
					size = len(queue)
					level = []
					for _ in range(size):
						node = queue.pop(0)

						if node.left:
							queue.append(node.left)

						if node.right:
							queue.append(node.right)

						level.append(node.val)

					solution_1087_2_2.append(level)

				return solution_1087_2_2