class Solution:
    # Time: O(n)
    # Space: O(n)
    def solution_857_2_1(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        l1 = self.solution_857_2_2(root1, [])
        l2 = self.solution_857_2_2(root2, [])
        res = []
        while l1 or l2:
            if not l1:
                res.append(l2.pop(0))
            elif not l2:
                res.append(l1.pop(0))
            else:
                res.append(l1.pop(0) if l1[0] < l2[0] else l2.pop(0))
        return res
        
    def solution_857_2_2(self, node, vals):
        if not node:
            return
        self.solution_857_2_2(node.left, vals)
        vals.append(node.val)
        self.solution_857_2_2(node.right, vals)
        return vals