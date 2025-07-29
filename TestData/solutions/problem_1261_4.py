class Solution:
    def solution_1261_4(self, logs: List[List[int]]) -> int:
        dic={}
        logs.sort()
        initial=logs[0][0]
        final=logs[-1][1]
        for i in range(initial,final):
            dic[i]=0
            for j in logs:
                if(i>=j[0] and i<j[1]):
                    dic[i]+=1
        m=max(dic.values())
        for i in dic.keys():
            if(dic[i]==m):
                return i