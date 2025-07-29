class Solution:
    def solution_1454_2(self, arr: List[int]) -> List[int]:
        n = len(arr)
        d = defaultdict(list)
        for i, v in enumerate(arr): d[v].append(i)
            
        
        res = defaultdict(list)
        for v, idx in d.items():
            ps = list(accumulate(idx, initial=0))
            vals = []
            idn = len(idx)
            for i, x in enumerate(idx):
                vals.append(i*x-ps[i] + ps[-1]-ps[i+1]-(idn-i-1)*x)

            res[v] = deque(vals)
            
        return [res[v].popleft() for v in arr]