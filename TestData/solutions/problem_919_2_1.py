class Solution:
    def solution_919_2_1(self, root: TreeNode) -> TreeNode:
        def solution_919_2_2(root):
            if root is None: return None
            solution_919_2_2(root.left); lst.append(root); solution_919_2_2(root.right)
        
        lst = []
        solution_919_2_2(root)
        
        def solution_919_2_3(arr):
            if len(arr) == 0:return 
            mid = len(arr)//2;   root = arr[mid]
            root.left = solution_919_2_3(arr[:mid]);   root.right = solution_919_2_3(arr[mid+1:])
            return root
        
        return solution_919_2_3(lst)