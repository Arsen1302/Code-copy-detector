class Solution:
    def solution_857_4_1(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        def solution_857_4_2(root, arr):
            if root is None:
                return
            solution_857_4_2(root.left, arr)
            arr.append(root.val)
            solution_857_4_2(root.right, arr)
            return

        arr = []
        solution_857_4_2(root1, arr)
        solution_857_4_2(root2, arr)

        return sorted(arr)