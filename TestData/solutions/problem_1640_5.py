class Solution:
    def solution_1640_5(self, edges: List[int]) -> int:
        d=collections.defaultdict(list)
        for i in range(len(edges)):
            d[edges[i]].append(i)
        l=list()
        s=0
        c=0
        for u,v in d.items():
            if sum(v)>s:
                s=sum(v)
                c=u
            if sum(v)==s and u<c:
                c=u
        return c