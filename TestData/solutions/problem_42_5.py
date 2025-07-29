class Solution:
    def solution_42_5(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        ans = 0
        row = [[root, []]]
        while row:
            new_row = []
            for node, lst_val in row:
                if not node.left and not node.right:
                    ans += int("".join(map(str, lst_val + [node.val])))
                if node.left:
                    new_row.append([node.left, lst_val + [node.val]])
                if node.right:
                    new_row.append([node.right, lst_val + [node.val]])
            row = new_row
        return ans