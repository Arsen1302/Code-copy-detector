class Solution:
def solution_1117_1(self, forbidden: List[int], a: int, b: int, x: int) -> int:
    
    forbidden = set(forbidden)
    limit = max(x,max(forbidden))+a+b
    seen = set()
    q = [(0,0,False)]
    while q:
        p,s,isb = q.pop(0)
        if p>limit or p<0 or p in forbidden or (p,isb) in seen:
            continue
        
        if p==x:
            return s
        
        q.append((p+a,s+1,False))
        if not isb:
            q.append((p-b,s+1,True))
        seen.add((p,isb))
    
    return -1