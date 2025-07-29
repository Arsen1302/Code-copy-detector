class Solution:
    def solution_394_4(self, root: Optional[TreeNode]) -> int:
        stack = [root]
        my_set = set()
        while len(stack) > 0:
            node = stack.pop()
            
            my_set.add(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

        if len(my_set) == 1:
            return -1

		# Remove the first minimum element
        my_set.remove(min(my_set))
		# Return the second minimum element
        return min(my_set)