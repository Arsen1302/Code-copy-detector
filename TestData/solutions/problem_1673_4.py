class Solution:
    def solution_1673_4(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        row = [root]
        odd = False
        while row:
            if odd:
                values = [node.val for node in row]
                values.reverse()
                for node, value in zip(row, values):
                    node.val = value
            odd = not odd
            new_row = []
            for node in row:
                if node.left:
                    new_row.append(node.left)
                if node.right:
                    new_row.append(node.right)
            row = new_row
        return root