class Solution:
    def solution_1688_4(self, s: str) -> str:
        st = []
        g = Counter(s)
        f = sorted(list(set(s)))
        f.append('z')
        cur = 0
        re = []
        for i in s:
            if i != f[cur]:
                st.append(i)
                g[i] -= 1
                while(g[f[cur]] == 0) and cur < len(f) - 1: cur+=1
            else:
                re.append(i)
                g[i] -= 1
                while(g[f[cur]] == 0) and cur < len(f) - 1: cur+=1
                while(st and st[-1] <= f[cur]):
                    re.append(st.pop())
                    
        while st: re.append(st.pop())
        # print(cur, f, g, re)
        return ''.join(re)