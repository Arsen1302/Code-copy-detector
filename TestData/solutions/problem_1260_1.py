class Solution:
def solution_1260_1(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
    
    intervals.sort(key = lambda x:x[1]-x[0])
    q = sorted([qu,i] for i,qu in enumerate(queries))
    res=[-1]*len(queries)
	
    for left,right in intervals:
        ind = bisect.bisect(q,[left])
        while ind<len(q) and q[ind][0]<=right:
            res[q.pop(ind)[1]]=right-left+1
    return res