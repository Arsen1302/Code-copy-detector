class Solution:
    def solution_576_2(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        mp = {x: i for i, x in enumerate(inorder)} # relative position 
        root = None
        stack = []
        for x in reversed(postorder): 
            if not root: root = node = TreeNode(x)
            elif mp[x] > mp[stack[-1].val]: stack[-1].right = node = TreeNode(x)
            else: 
                while stack and mp[stack[-1].val] > mp[x]: node = stack.pop() # retrace 
                node.left = node = TreeNode(x)
            stack.append(node)
        return root