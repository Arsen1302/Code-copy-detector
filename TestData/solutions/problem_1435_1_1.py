class Solution:
    def solution_1435_1_1(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        
        def solution_1435_1_2(node): 
            """Return lowest common ancestor of start and dest nodes."""
            if not node or node.val in (startValue , destValue): return node 
            left, right = solution_1435_1_2(node.left), solution_1435_1_2(node.right)
            return node if left and right else left or right
        
        root = solution_1435_1_2(root) # only this sub-tree matters
        
        ps = pd = ""
        stack = [(root, "")]
        while stack: 
            node, path = stack.pop()
            if node.val == startValue: ps = path 
            if node.val == destValue: pd = path
            if node.left: stack.append((node.left, path + "L"))
            if node.right: stack.append((node.right, path + "R"))
        return "U"*len(ps) + pd