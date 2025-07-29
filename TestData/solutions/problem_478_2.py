class Solution:
    def solution_478_2(self, N: int) -> int:
        d = {'0':'0','1':'1','2':'5','5':'2','6':'9','8':'8','9':'6'}
        count = 0
        for i in range(1,N+1):
            x = ''
            flag = True
            for j in str(i):
                if j not in d.keys():
                    flag = False
                    break
                else:
                    x += d[j]
            if flag and x != str(i):
                count += 1
        return count