class Solution:
    def solution_717_1_1(self, root: TreeNode) -> TreeNode:
        s = 0
        def solution_717_1_2(root):
            if root is None: return
            nonlocal s
            solution_717_1_2(root.right)
            #print(s,root.val)
            s = s + root.val
            root.val = s
            solution_717_1_2(root.left)
        solution_717_1_2(root)
        return root