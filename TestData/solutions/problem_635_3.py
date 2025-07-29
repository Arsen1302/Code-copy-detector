class Solution:
def solution_635_3(self, arr: List[int]) -> bool:
    dic = Counter(arr)
    res = []
    
    for n in sorted(arr):
        if dic[n]>0:
            dic[n]-=1     # This is to check 0 if it present take e.g. : [4,0]
            if 2*n in dic and dic[2*n]>0:
                dic[2*n]-=1
                res.append((n,2*n))
            else:
                dic[n]+=1

    return len(res)*2==len(arr)