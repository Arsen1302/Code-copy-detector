class Solution:
def solution_1325_4(self, segments: List[List[int]]) -> List[List[int]]:
    
    dic = defaultdict(int)
    for s,e,c in segments:
        dic[s]+=c
        dic[e]-=c
    
    st=None
    color=0
    res = []
    for p in sorted(dic):
        if st is not None and color!=0:
            res.append([st,p,color])
        color+=dic[p]
        st = p
    
    return res