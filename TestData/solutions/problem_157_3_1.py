class Solution:
    def solution_157_3_1(self, n_1: List[int], n_2: List[int], k: int) -> List[int]:
        def solution_157_3_2(maxum,s1,s2):
            n1, n2 = -1, -1
            if M - s1 > maxum: n1 = max(n_1[s1:s1+maxum])
            elif s1 < M: n1 = max(n_1[s1:])
                
            if N - s2 > maxum: n2 = max(n_2[s2:s2+maxum])
            elif s2 < N: n2 = max(n_2[s2:])
            return n1,n2

        M, N = len(n_1), len(n_2)
        r, l = [], [[0,0]]
        for x in range(k):
            n_l, n_r = [], []
            for st in l:
                n1, n2 = solution_157_3_2(M + N - st[0] - st[1] - k + 1 + x , st[0], st[1])
                if n1 > n2:
                    n_r.append(n1)
                    n_l.append([st[0]+n_1[st[0]:].index(n1)+1,st[1]])
                elif n1 < n2:
                    n_r.append(n2)
                    n_l.append([st[0],st[1]+n_2[st[1]:].index(n2)+1])
                elif n1 == n2 and n1 != -1:
                    n_r.append(n1)
                    n_l.append([st[0]+n_1[st[0]:].index(n1)+1,st[1]])
                    n_r.append(n2)
                    n_l.append([st[0],st[1]+n_2[st[1]:].index(n1)+1])
            nr = -1
            for i in range(len(n_r)):
                if n_r[i] > nr: n_n_l = set(); n_n_l.add((n_l[i][0],n_l[i][1])); nr = n_r[i]
                elif n_r[i] == nr: n_n_l.add((n_l[i][0],n_l[i][1]))
            r.append(nr)
            l = n_n_l
        return r