class Solution:
    def solution_702_2(self, root: TreeNode) -> int:
        bfs = [root]
        l = []
        while bfs:
            node = bfs.pop(0)
            if node.left:
                x = node.left.val
                node.left.val = str(node.val) + str(x)
                bfs.append(node.left)
            if node.right:
                x = node.right.val
                node.right.val = str(node.val) + str(x)
                bfs.append(node.right)
            if not node.left and not node.right:
                l.append(str(node.val))
        return sum([int(i,2) for i in l])