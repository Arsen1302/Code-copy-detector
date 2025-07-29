class Solution:
    def solution_1649_4(self, root: Optional[TreeNode], start: int) -> int:
        neighbors = defaultdict(set)
        row = {root}
        while row:
            new_row = set()
            for node in row:
                if node.left:
                    neighbors[node.val].add(node.left.val)
                    neighbors[node.left.val].add(node.val)
                    new_row.add(node.left)
                if node.right:
                    neighbors[node.val].add(node.right.val)
                    neighbors[node.right.val].add(node.val)
                    new_row.add(node.right)
            row = new_row

        level = {start}
        seen = set()
        ans = -1
        while level:
            ans += 1
            new_level = set()
            for node in level:
                new_level.update(neighbors[node])
                seen.add(node)
            level = new_level - seen
        return ans