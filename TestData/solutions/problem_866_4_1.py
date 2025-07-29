class Solution:
    def solution_866_4_1(self, root: TreeNode) -> int:
        def solution_866_4_2(grandparent, parent, node):
            if not node:return
            if grandparent and grandparent.val%2 == 0:self.ans += node.val
            solution_866_4_2(parent, node, node.left)
            solution_866_4_2(parent, node, node.right)
        
        self.ans = 0
        solution_866_4_2(None, None, root)
        return self.ans