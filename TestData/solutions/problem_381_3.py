class Solution:
    def solution_381_3(self, nums: List[int]) -> TreeNode:
        stack = []
        for x in nums: 
            node = TreeNode(x)
            while stack and stack[-1].val < x: node.left = stack.pop()
            if stack: stack[-1].right = node 
            stack.append(node)
        return stack[0]