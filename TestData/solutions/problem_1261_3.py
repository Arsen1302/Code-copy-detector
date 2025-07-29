class Solution:
    def solution_1261_3(self, logs: List[List[int]]) -> int:
        b=[logs[i][0] for i in range(len(logs))]
        d=[logs[i][1] for i in range(len(logs))]
        m=0 #max population
        a=0 #alive
        r=1950
        for i in range(1950,2051):
            a+=b.count(i)-d.count(i)
            if a>m:
                m=a
                r=i    
        return r