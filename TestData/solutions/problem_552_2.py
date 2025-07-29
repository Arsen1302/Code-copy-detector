class Solution:
    def solution_552_2(self, root: TreeNode) -> TreeNode:
        fn = lru_cache(None)(lambda x: 1 + max(fn(x.left), fn(x.right)) if x else 0)
        
        node = root
        while node: 
            if fn(node.left) == fn(node.right): return node 
            elif fn(node.left) < fn(node.right): node = node.right
            else: node = node.left
        return node