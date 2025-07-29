class Solution:
    def solution_404_4_1(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        def solution_404_4_2(node,value):
            if node:
                left,right = solution_404_4_2(node.left,node.val),solution_404_4_2(node.right,node.val)
                self.ans = max(self.ans,left+right)
                if value == node.val: return max(left,right)+1
            return 0
        solution_404_4_2(root,None)
        return self.ans