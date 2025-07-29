class Solution:
    def solution_673_5(self, root: TreeNode, x: int, y: int) -> bool:
        ans = dict()
        stack = [(root, 0, None)]
        while stack: 
            node, k, parent = stack.pop()
            if not node: continue
            if node.val in (x, y): ans[node.val] = (k, parent)
            stack.append((node.left, k+1, node))
            stack.append((node.right, k+1, node))
        return ans[x][0] == ans[y][0] and ans[x][1] != ans[y][1]