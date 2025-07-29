class Solution:
    def solution_576_3(self, pre: List[int], post: List[int]) -> TreeNode:
        mp = {x: i for i, x in enumerate(post)}
        root = None 
        stack = []
        for x in pre: 
            if not root: root = node = TreeNode(x)
            elif mp[x] < mp[stack[-1].val]: stack[-1].left = node = TreeNode(x)
            else: 
                while mp[stack[-1].val] < mp[x]: stack.pop() # retrace 
                stack[-1].right = node = TreeNode(x)
            stack.append(node)
        return root