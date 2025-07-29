class Solution:
    def solution_855_1(self, root: Optional[TreeNode]) -> int:
        q = [(root, 0)]
        ans = 0
        curr_level = 0 # Maintains the current level we are at
        while len(q) != 0: # Do a simple Level Order Traversal
            current, max_level = q.pop(0)
            if max_level > curr_level: # Update the ans as curr_level gets outdated
                curr_level = max_level # Update curr_level
                ans = 0 # Ans needs to be constructed for the new level i.e. max_level
            ans += current.val
            if current.left is not None:
                q.append((current.left, max_level + 1))
            if current.right is not None:
                q.append((current.right, max_level + 1))
        return ans