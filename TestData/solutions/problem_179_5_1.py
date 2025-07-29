class Solution:
    def solution_179_5_1(self, en: List[List[int]]) -> int:
        def solution_179_5_2(t,n,v):
            i = 0
            j = n-1
            while i<=j:
                m = (i+j)//2
                if t[m][1] == v:
                    return m
                elif v<t[m][1]:
                    j = m-1
                else:
                    i = m+1
            return i
        en.sort(key = lambda x:(x[0],-x[1]))
        t = [en[0]]
        c = 1
        for i in range(len(en)):
            if t[-1][1] < en[i][1]:
                t.append(en[i])
                c += 1
            else:
                x = solution_179_5_2(t,c,en[i][1])
                t[x] = en[i]
        return len(t)