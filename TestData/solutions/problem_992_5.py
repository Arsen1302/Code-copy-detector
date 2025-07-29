class Solution:
def solution_992_5(self, arr: List[int], target: int) -> int:
    
    s,res,lsize = 0,float('inf'),float('inf')
    dic = dict()
    dic[0] = -1
    for i in range(len(arr)):
        s+=arr[i]
        dic[s] = i
    
    s=0
    for i,val in enumerate(arr):
        s+=val
        if s-target in dic:
            lsize = min(i-dic[s-target],lsize)
        
        if s+target in dic and lsize!=float('inf'):
            rsize = dic[s+target]-i
            res = min(res,lsize+rsize)
    
    return -1 if res==float('inf') else res