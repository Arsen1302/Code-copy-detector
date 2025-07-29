class Solution:
def solution_249_4(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
    
    if root is None:
        return 
    
    if key<root.val:
        root.left = self.solution_249_4(root.left,key)
    
    elif key>root.val:
        root.right = self.solution_249_4(root.right,key)
    
    else:
        if root.left is None:
            return root.right
        
        if root.right is None:
            return root.left
        
        tmp = root.right
        mini= tmp.val
        while tmp.left!=None:
            tmp = tmp.left
            mini= tmp.val
        root.val = mini
        root.right = self.solution_249_4(root.right,root.val)
    
    return root