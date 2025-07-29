class Solution:
def solution_919_3_1(self, root: TreeNode) -> TreeNode:
    
    arr = []
    def solution_919_3_2(root):
        if root is None:
            return 
        solution_919_3_2(root.left)
        arr.append(root.val)
        solution_919_3_2(root.right)
    
    def solution_919_3_3(i,j,arr):
        if i>j:
            return None
        if i==j:
            return TreeNode(arr[i])
        
        m = (i+j)//2
        root = TreeNode(arr[m])
        root.left = solution_919_3_3(i,m-1,arr)
        root.right= solution_919_3_3(m+1,j,arr)
        return root
    
    solution_919_3_2(root)
    i, j = 0, len(arr)-1
    return solution_919_3_3(i,j,arr