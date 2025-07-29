class Solution:
    def solution_387_1(self, root: TreeNode) -> int:
        Q = collections.deque()
        Q.append((root,0))
        ans = 0
        while Q:
            length = len(Q)
            _, start = Q[0]
            for i in range(length):
                node, index = Q.popleft()
                if node.left:
                    Q.append((node.left, 2*index))
                if node.right:
                    Q.append((node.right, 2*index+1))
            ans = max(ans, index-start+1)
        return ans