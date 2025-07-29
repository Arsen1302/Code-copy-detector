class Solution:
	def solution_112_5_1(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

		queue=[root]
		while len(queue)>0:
			currentNode=queue.pop(0)

			if currentNode is None:
				continue
			self.solution_112_5_2(currentNode)
			queue.append(currentNode.left)
			queue.append(currentNode.right)
		return root

	def solution_112_5_2(self,currentNode):
		currentNode.left,currentNode.right=currentNode.right,\
                                        currentNode.left