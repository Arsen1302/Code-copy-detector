class Solution:
    def solution_502_5(self, root: TreeNode) -> TreeNode:
        stack = [(root, False)]
        toprune = set()
        
        while stack:
            node, visited = stack.pop()
            if node:
                if visited:
                    if node.left in toprune:
                        node.left = None
                    if node.right in toprune:
                        node.right = None
                    if node.val == 0 and node.left is None and node.right is None:
                        toprune.add(node)
                else:
                    stack.extend([(node, True), (node.left, False), (node.right, False)])
        
        return root if root not in toprune else None