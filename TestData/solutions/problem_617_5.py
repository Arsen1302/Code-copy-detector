class Solution:
    def solution_617_5(self, stamp: str, target: str) -> List[int]:
        l_s, l_t = len(stamp), len(target)
        s = '?'*l_t
        res = []

        perm = set()
        for i in range(l_s):
            for j in range(l_s-i):
                perm.add('?'*i + stamp[i:l_s-j] + '?'*j)

        while target != s:
            found = False
            for i in range(l_t-l_s, -1, -1):
                if target[i:i+l_s] in perm:
                    target = target[:i]+'?'*l_s+target[i+l_s:]
                    res.append(i)
                    found = True
            if not found:
                return []

        return res[::-1]