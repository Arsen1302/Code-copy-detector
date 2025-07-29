class Solution:
    
    def solution_1031_3_1(self):
        self.sol = 0
    
    def solution_1031_3_2(self, root: TreeNode, distance: int) -> int:
        def solution_1031_3_3(node):
            if not node:
                return []
            if not node.left and not node.right:
                # node, depth
                return [[0, 0]]
            else:
                cur = []
                l = solution_1031_3_3(node.left)
                r = solution_1031_3_3(node.right)
                for n in l: n[1] += 1
                for n in r: n[1] += 1
                for n in r:
                    for n1 in l:
                        if n[1] + n1[1] <= distance: self.sol += 1
                return l+r
        solution_1031_3_3(root)
        return self.sol