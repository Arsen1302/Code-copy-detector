class Solution:
    def solution_380_2_1(self, root: TreeNode, k: int) -> bool:
        def solution_380_2_2(node: TreeNode):
            if node:
                yield from solution_380_2_2(node.left)
                yield node.val
                yield from solution_380_2_2(node.right)
        
        arr = [x for x in solution_380_2_2(root)]
        i = 0
        j = len(arr) - 1
        
        while i < j:
            if arr[i] + arr[j] == k: return True
            if arr[i] + arr[j] < k: i += 1
            if arr[i] + arr[j] > k: j -= 1
            
        return False