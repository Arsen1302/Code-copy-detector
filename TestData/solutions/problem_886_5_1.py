class Solution:
    def solution_886_5_1(self, root: Optional[TreeNode]) -> int:
        def solution_886_5_2(root):
            if root.left:
                x=solution_886_5_2(root.left)
            else:
                x=0
            if root.right:
                y=solution_886_5_2(root.right)
            else:
                y=0
            root.val=x+y+root.val
            return root.val
            
        total=solution_886_5_2(root)
        queue=[root.left,root.right]
        ans=0
        while queue:
            node=queue.pop(0)
            if node:
                ans=max((total-node.val)*node.val,ans)
                queue.append(node.left)
                queue.append(node.right)
        return ans%(10**9 +7)