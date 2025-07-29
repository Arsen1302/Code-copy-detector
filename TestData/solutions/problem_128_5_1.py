class Solution:
    def solution_128_5_1(self, root: Optional[TreeNode]) -> List[str]:
        ans=[]           # resultant list containing all paths.
        def solution_128_5_2(root,s):
            if not root.left and not root.right:        # If leaf node occurs then path ends here so append the string in 'ans'.
                ans.append(s+str(root.val))
                return
            s+=str(root.val)        # concatenate value of root in the path 
            if root.left:                # If there is any node in left to traverse
                solution_128_5_2(root.left,s+"->")
            if root.right:             # If there is any node in right to traverse
                solution_128_5_2(root.right,s+"->")
            return
			
        solution_128_5_2(root,"")         # main calling of preOrder with empty string
        return ans