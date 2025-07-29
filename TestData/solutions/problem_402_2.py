class Solution:
    def solution_402_2(self, edges: List[List[int]]) -> List[int]:
        d=defaultdict(lambda:[])
        for i in range(len(edges)):
            d[edges[i][0]].append(edges[i][1])
            d[edges[i][1]].append(edges[i][0])

        while any([len(v)<2 for v in d.values()]):
            for k,v in [(k,v) for k, v in d.items() if len(v)<2]:
                for m in v:
                    d[m].remove(k)
                del d[k]
                
        for e in reversed(edges):
            if e[0] in d and e[1] in d:
                return e