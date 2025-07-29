class Solution:
    def solution_20_5(self, root: Optional[TreeNode]) -> List[List[int]]:

        ans = []
        cur_level, cur_level_nodes = 0, []

		# initialise and add root in queue with level as 0
        q = deque()
        q.append((root, 0))

        while q:
			# get first element from the queue and its resp. level
            node, level = q.popleft()
            if node is None:
                continue

			# if level is same, append nodes value
			# else change level and append nodes value
            if level == cur_level:
                cur_level_nodes.append(node.val)
            else:
                ans.append(cur_level_nodes)
                cur_level = level
                cur_level_nodes = [node.val]

			# add left and right children in queue with level as parent's level + 1
            q.append((node.left, level+1))
            q.append((node.right, level+1))

        if len(cur_level_nodes):
            ans.append(cur_level_nodes)

        return ans[::-1]