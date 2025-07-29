class Solution(object):
    def solution_1673_5(self, root):
        flag = False
        q = deque()
        q.append(root)
        while q:
            temp = []
            if flag:
                for i in range(len(q)):
                    temp.append(q[i].val)
                temp = temp[::-1]
            for i in range(len(q)):
                p = q.popleft()
                if flag:
                    p.val = temp[i]
                if p.left: q.append(p.left)
                if p.right: q.append(p.right)
            flag = not(flag)
        return root