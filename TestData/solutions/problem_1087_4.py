class Solution:
    def solution_1087_4(self, root: Optional[TreeNode]) -> bool:
        q = deque()
        q.append(root)
        levelCounter = 0
        while q:
            odd = False
            even = False
            if levelCounter % 2 != 0:
                odd = True
                prevVal = float("inf")
            else:
                even = True
                prevVal = float("-inf")
            for i in range(len(q)):
                node = q.popleft()
                if node:
                    if even and (node.val % 2 == 0 or node.val <= prevVal):
                        return False
                    elif odd and (node.val % 2 != 0 or node.val >= prevVal):
                        return False
                    prevVal = node.val   
                    q.append(node.left)
                    q.append(node.right)
            levelCounter += 1
        return True