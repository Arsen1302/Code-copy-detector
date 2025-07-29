class Solution(object):
    def solution_1328_4(self, num, change):
        ans, flag = '', False
        for i in range(len(num)):
            if int(num[i]) == change[int(num[i])] and not(flag): 
                ans += num[i]
                continue
            if int(num[i]) <= change[int(num[i])]:
                ans += str(change[int(num[i])])
                flag = True
            else:
                if flag:
                    ans += num[i]
                    break
                ans += num[i]
        return ans + num[i+1:]