class Solution(object):
    def solution_874_4_1(self, root, target):
        def solution_874_4_2(root, t):
            flag = False
            if root.val == t and root.left is None and root.right is None:
                self.flag2 = True
                return False
            q = deque()
            q.append(root)
            while q:
                for _ in range(len(q)):
                    p = q.popleft()
                    if p.left:
                        if p.left.val == t and p.left.left is None and p.left.right is None:
                            p.left = None
                            flag = True
                        else:
                            q.append(p.left)
                    if p.right:
                        if p.right.val == t and p.right.left is None and p.right.right is None:
                            p.right = None
                            flag = True
                        else:
                            q.append(p.right)
            return flag
        self.flag2 = False    
        delete = True
        while delete:
            delete = solution_874_4_2(root, target)
            if self.flag2: return None
        return root