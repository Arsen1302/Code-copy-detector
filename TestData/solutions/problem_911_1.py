class Solution:
    def solution_911_1(self, root: Optional[TreeNode]) -> int:
        
        LEFT = 0
        RIGHT = 1
            
        stack = []
        if root.left:
            stack.append((root.left, LEFT, 1))
        if root.right:
            stack.append((root.right, RIGHT, 1))
            
        longest = 0
        while stack:
            node, direction, count = stack.pop()
            
            longest = max(longest, count)
            if direction == LEFT:
                if node.left:
                    stack.append((node.left, LEFT, 1))
                if node.right:
                    stack.append((node.right, RIGHT, count+1))
            else:
                if node.right:
                    stack.append((node.right, RIGHT, 1))
                if node.left:
                    stack.append((node.left, LEFT, count+1))
        return longest