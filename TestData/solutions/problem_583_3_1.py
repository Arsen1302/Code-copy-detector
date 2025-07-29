class Solution(object):
    def solution_583_3_1(self, root):
        def solution_583_3_2(root, ans):
            if not root: return
            solution_583_3_2(root.left, ans)
            ans.append(root.val)
            solution_583_3_2(root.right, ans)
            return ans
        ans = solution_583_3_2(root, [])
        root = right = TreeNode(0)
        for i in range(len(ans)):
            right.right = TreeNode(ans[i])
            right = right.right
        return root.right