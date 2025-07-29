class Solution:
    def solution_919_5_1(self, root: TreeNode) -> TreeNode:
        # convert BST tree to a sorted array:
        def solution_919_5_2(root, arr):
            if root is None:
                return
            solution_919_5_2(root.left, arr)
            arr.append(root.val)
            solution_919_5_2(root.right, arr)
            return
        
        def solution_919_5_3(arr):
            if not arr:
                return None
            
            mid = len(arr) // 2

            root = TreeNode(arr[mid])
            root.left = solution_919_5_3(arr[:mid])
            root.right = solution_919_5_3(arr[mid+1:])
            
            return root

        arr = []
        solution_919_5_2(root, arr)
        
        return solution_919_5_3(arr)