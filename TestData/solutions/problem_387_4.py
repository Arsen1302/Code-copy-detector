class Solution:
	def solution_387_4(self, root: Optional[TreeNode]) -> int:

		if not root:
			return None

		q=deque()
		q.append(root)

		level=deque()
		level.append(1)

		max_width=1

		while(len(q)!=0):

			max_width=max(max_width,max(level)-min(level)+1)

			for i in range(len(q)):
				r=level.popleft()
				node=q.popleft()

				if node.left:
					q.append(node.left)
					level.append(2*r)

				if node.right:
					q.append(node.right)
					level.append(2*r+1)



		return max_width 
		
#please upvote if it helps you in any manner regarding how to approach the problem