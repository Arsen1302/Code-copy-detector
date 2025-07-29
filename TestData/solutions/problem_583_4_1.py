class Solution:  
    def solution_583_4_1(self,root):
        if not root:
            return
        self.solution_583_4_1(root.left)
		
        if self.result==None:
            self.result=TreeNode(root.val,None,None)
            self.curr=self.result
        else:
            self.curr.right=TreeNode(root.val,None,None)     
            self.curr=self.curr.right      #updating the current root of the new Tree
			
        self.solution_583_4_1(root.right)
        return
    def solution_583_4_2(self, root: TreeNode) -> TreeNode:
        self.result=None     #root of the new Tree
        self.curr=None       #current root of the new Tree
        self.solution_583_4_1(root)
        return self.result