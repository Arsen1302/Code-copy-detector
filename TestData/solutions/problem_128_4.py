class Solution:
    def solution_128_4(self, root: Optional[TreeNode]) -> List[str]:
        if not root: return None
        
        q=[(root, str(root.val))]
        res = []
        
        while q:
            
            node, path_upto_node = q.pop()
            
            if not any([node.left, node.right]):
                res.append(path_upto_node)
            
            else:
                q.append((node.left, path_upto_node + '->' + str(node.left.val))) if node.left else None
                q.append((node.right, path_upto_node + '->' + str(node.right.val))) if node.right else None
                
        return res