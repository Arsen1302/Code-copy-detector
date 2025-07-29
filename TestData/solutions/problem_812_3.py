class Solution:
    def solution_812_3(self, s: str) -> int:
        n , start , count , req , cur, index , ans = len(s) , 0 ,defaultdict(int) ,[0]*4 , [0]*4 , {'Q':0,'W':1,'E':2,'R':3} , len(s)
        for i in s:count[i] += 1
        for i in count:
            if count[i] > n // 4:req[index[i]] = count[i] - n // 4
        if req == [0,0,0,0]: return 0
        for i,val in enumerate(s):
            cur[index[val]] += 1
            if cur[0] >= req[0] and cur[1] >= req[1] and cur[2] >= req[2] and cur[3] >= req[3]:
                while True:
                    if s[start] in "QWER":
                        if cur[index[s[start]]] > req[index[s[start]]]:
                            cur[index[s[start]]] -= 1
                            start += 1
                        else:
                            break
                    else:
                        start += 1
                ans = min(ans,i - start + 1)
        return ans