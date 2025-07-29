class Solution:
    def solution_317_5_1(self):
        self.arr = []
		
    def solution_317_5_2(self, node: Optional[TreeNode]):
        if not node:
            return
        self.solution_317_5_2(node.left)
        self.arr.append(node)
        self.solution_317_5_2(node.right)
    
    def solution_317_5_3(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.solution_317_5_2(root)      
        for i in range(len(self.arr)-2, -1, -1):
            self.arr[i].val += self.arr[i+1].val            
        return root