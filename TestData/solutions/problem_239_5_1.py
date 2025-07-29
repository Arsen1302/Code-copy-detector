class Solution:
    def solution_239_5_1(self):
        self.ans = 0
    def solution_239_5_2(self,root: Optional[TreeNode], targetSum: int,summ: int) ->None:
        if root is None:
            return
        if summ==targetSum:
            self.ans+=1
        if root.left:
            self.solution_239_5_2(root.left, targetSum, summ + root.left.val)
        if root.right:
            self.solution_239_5_2(root.right, targetSum, summ + root.right.val)
    def solution_239_5_3(self, root: Optional[TreeNode], targetSum: int) -> int:
        if root is None:
            return 0
        self.solution_239_5_2(root,targetSum,root.val)
        self.solution_239_5_3(root.left,targetSum)
        self.solution_239_5_3(root.right,targetSum)
        return self.ans