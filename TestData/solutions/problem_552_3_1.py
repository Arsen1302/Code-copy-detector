class Solution:
    def solution_552_3_1(self, root: TreeNode) -> TreeNode:
        parent, depth = {root: None}, {root: 0}
        def solution_552_3_2(node):
            if node.right:
                parent[node.right] = node
                depth[node.right] = depth[node] + 1
                solution_552_3_2(node.right)
            if node.left:
                parent[node.left] = node
                depth[node.left] = depth[node] + 1
                solution_552_3_2(node.left)
        solution_552_3_2(root)
        
        max_depth = max(depth.values())
        deepest_nodes = set(node for node in parent.keys() if depth[node] == max_depth)
        while len(deepest_nodes) > 1:
            deepest_nodes = set(parent[node] for node in deepest_nodes)
        
        return deepest_nodes.pop()