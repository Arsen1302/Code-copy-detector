class Solution:
    def solution_646_5(self, root) -> bool:
        x=root.val
        q=[root]
        while q:
            node=q.pop(0)
            if node.val!=x:
                return False
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        return True