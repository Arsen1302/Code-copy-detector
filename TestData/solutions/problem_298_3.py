class Solution:
    def solution_298_3(self, root: TreeNode) -> int:
        queue = [root]
        while queue: # bfs 
            tmp = []
            ans = None
            for node in queue: 
                if ans is None: ans = node.val 
                if node.left: tmp.append(node.left)
                if node.right: tmp.append(node.right)
            queue = tmp 
        return ans