class Solution:
    def solution_42_4_1(self, root: Optional[TreeNode]) -> int:
        ans = 0
        def solution_42_4_2(node, num):
            if node.left:
                solution_42_4_2(node.left, num*10 + node.left.val)
            if node.right:
                solution_42_4_2(node.right, num*10 + node.right.val)
            
            if not node.left and not node.right:
                nonlocal ans
                ans += num
            
        solution_42_4_2(root, root.val)
        return ans