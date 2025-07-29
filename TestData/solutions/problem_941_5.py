class Solution:
    def solution_941_5(self, queries: List[int], m: int) -> List[int]:
        ans = []
        p = []
        maxq = max(queries)
        for i in range(1,maxq+1):
            p.append(i)
        for ele in queries:
            ans.append(p.index(ele))
            p.remove(ele)
            p.insert(0,ele)
        return ans