class Solution:
    def solution_1031_4_1(self, root: TreeNode, distance: int) -> int:
        self.distance = distance
        self.ans = 0
        self.solution_1031_4_2(root)
        return self.ans

    def solution_1031_4_2(self, root):
        if not root:
            return []
        if not root.left and not root.right:
            return [1]
        
        l, r = self.solution_1031_4_2(root.left), self.solution_1031_4_2(root.right)
        
        for i in l:
            for j in r:
                if i + j <= self.distance:
                    self.ans += 1
        l = [i+1 for i in l]
        r = [j+1 for j in r]
        
        return l+r