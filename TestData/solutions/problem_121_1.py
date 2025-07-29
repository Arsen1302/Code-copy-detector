class Solution:
    def solution_121_1(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root==None or root.val==p.val or root.val==q.val:
            return root
        left=self.solution_121_1(root.left,p,q)
        right=self.solution_121_1(root.right,p,q)
        if left!=None and right!=None:
            return root
        elif left!=None:
            return left
        else:
            return right