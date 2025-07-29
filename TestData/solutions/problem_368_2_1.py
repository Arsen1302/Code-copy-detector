class Solution:
    def solution_368_2_1(self, root: Optional[TreeNode]) -> List[float]:
        
		#starting here, the next ~8 lines are how I do solution_368_2_2 recursively.
        levels = []
        def solution_368_2_2(node, level):
            if node:
                if len(levels) == level: levels.append([])
                levels[level] += [node.val]
                solution_368_2_2(node.left, level+1)
                solution_368_2_2(node.right, level+1)
        
        solution_368_2_2(root, 0)
	# after that, just return the averages in a list.
        return [sum(i)/len(i) for i in levels]