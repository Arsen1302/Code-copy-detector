class Solution:
    def solution_911_5_1(self, root: Optional[TreeNode]) -> int:
        # Time : O(n)
        longest = 0
        def solution_911_5_2(node, next_direction, traveled_distance):
            nonlocal longest
            longest = max(longest, traveled_distance)
            
            if node.right:
                if next_direction == "right":
                    solution_911_5_2(node.right, "left", traveled_distance + 1)
                else:
					# If not supposed to go right but still want to, start over again
                    solution_911_5_2(node.right, "left", 1)

            
            if node.left:
                if next_direction == "left":
                    solution_911_5_2(node.left, "right", traveled_distance + 1)
                else:
                    solution_911_5_2(node.left, "right", 1)
                    
        if root.left:
            solution_911_5_2(root.left, "right", 1)
        if root.right:
            solution_911_5_2(root.right, "left", 1)
        if not root.left and not root.right: 
            return 0
            
        return longest