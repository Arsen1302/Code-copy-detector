class Solution:
    def solution_404_5_1(self,node):
        if not node:return 0
        if not node.left and not node.right:
            if self.ans==0:self.ans=1
            return 1
        l=self.solution_404_5_1(node.left)
        r=self.solution_404_5_1(node.right)
        if node.left and node.right and node.left.val==node.right.val==node.val:
            if self.ans<l+r+1:self.ans=l+r+1
            return l+1 if l+1>r+1 else r+1
        if node.left and node.left.val==node.val:
            if self.ans<l+1:self.ans=l+1
            return l+1
        if node.right and node.right.val==node.val:
            if self.ans<r+1:self.ans=r+1
            return r+1
        return 1
    def solution_404_5_2(self, root: Optional[TreeNode]) -> int:
        self.ans=0
        self.solution_404_5_1(root)
        return self.ans-1 if self.ans>0 else 0