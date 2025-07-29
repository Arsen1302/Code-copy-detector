class Solution:
	def solution_776_5(self, root: Optional[TreeNode]) -> int:
		if not root: 
			return None

		q=deque() 

		max_sum=-10**18       #assume the max_level_sum to be -10**18
		level=0                         #this is current level
		level_ans=0                 #this will store the level at which the max_sum has occured

		q.append(root)           #start our bfs with the root node obviously

		while len(q)!=0:          #do the bfs as long as the queue is not empty
			level+=1                #update the level after each while loop
			#start from level 1
			
			curr_sum=0                    #store the levelwise sum
			for i in range(len(q)):      #traverse through each node of current level
				curr_sum+=q[i].val    #store the sum of val of each node of the current level

			if curr_sum>max_sum:        #check if the current_level_sum is greater than the max_level_sum
				max_sum=curr_sum        #update the max_sum
				level_ans=level                #update the level at which max_sum is found
			
			# now take the node from left to right of each level
			#below is typical bfs traversal
			
			for i in range(len(q)):
				node=q.popleft()

				if node.left:
					q.append(node.left)

				if node.right:
					q.append(node.right)

		return level_ans
		
		#pls upvote if it helps you in any manner regarding understanding the solution