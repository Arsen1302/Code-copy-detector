class Solution:
    def solution_290_3_1(self):
        self.d = {}
        self.m = 1
        self.ans = []
        
    def solution_290_3_2(self, x):
        if not x:
            return
        if x.val not in self.d:
            self.d[x.val] = 1    
        else:
            self.d[x.val] += 1
            self.m = max(self.m, self.d[x.val])
            
        self.solution_290_3_2(x.left)
        self.solution_290_3_2(x.right)
    
    def solution_290_3_3(self, root: Optional[TreeNode]) -> List[int]:
        self.solution_290_3_2(root)
        for x in self.d:
            if self.d[x] == self.m:
                self.ans.append(x)
        return self.ans