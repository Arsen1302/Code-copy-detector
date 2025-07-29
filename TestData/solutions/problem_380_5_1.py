class Solution:
    def solution_380_5_1(self, root: Optional[TreeNode], k: int) -> bool:
	    # isReverse: traversing in descending order.
        def solution_380_5_2(node, isReverse):
            l, r = node.left, node.right
            if isReverse:
                l, r = node.right, node.left
            if l:
                yield from solution_380_5_2(l, isReverse)
            yield node.val
            if r:
                yield from solution_380_5_2(r, isReverse)
		
        # Generator in ascending order 
        leftGen = solution_380_5_2(root, False)
		# Generator in descending order.
        rightGen = solution_380_5_2(root, True)
		
        left = leftGen.__next__()
        right = rightGen.__next__()

        while left < right:
            if left + right == k:
                return True
            if left + right > k:
                right = rightGen.__next__()
            else:
                left = leftGen.__next__()
        return False