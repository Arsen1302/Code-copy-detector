class Solution:
    def solution_37_4_1(self, root: Optional[TreeNode]) -> int:
        if not root: return
        self.res = root.val  
        
        def solution_37_4_2(root):
            # Base case
            if not root: return 0
             
            # l and r store maximum path sum going through left and right child of root respectively
            l = solution_37_4_2(root.left)
            r = solution_37_4_2(root.right)
            
            # Max path for parent call of root. This path must include at most one child of root
            temp = max(root.val + max(l, r), root.val)
            # ans  represents the sum when the node under consideration is the root of the maxSum path and no ancestor of root are there in max sum path
            ans = max(temp, root.val + l + r)
            self.res = max(self.res, ans) # max across the whole tree
            
            return temp # for considering other subtrees also
        
        solution_37_4_2(root)
        return self.res
    
    
# Time Complexity: O(n) where n is number of nodes in Binary Tree.
# Space Complexity: O(1)