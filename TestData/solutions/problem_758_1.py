class Solution:
def solution_758_1(self, hours: List[int]) -> int:
    
    dic = defaultdict(int)
    dummy = [1 if hours[0]>8 else -1]
    for h in hours[1:]:
        c = 1 if h>8 else -1
        dummy.append(dummy[-1]+c)
    
    res = 0
    for i in range(len(dummy)):
        if dummy[i]>0:
            res = max(res,i+1)
        else:
            if dummy[i]-1 in dic:
                res = max(res,i-dic[dummy[i]-1])
            if dummy[i] not in dic:
                dic[dummy[i]] = i
    
    return res