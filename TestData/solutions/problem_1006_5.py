class Solution:
    def solution_1006_5(self, arr: List[int], k: int) -> bool:
        d = {}
        
        for idx, val in enumerate(arr):
            mod = val % k
            if mod == 0:
                continue
                
            if k - mod in d and d[k - mod] != 0:
                d[k - mod] -= 1
                if d[k - mod] == 0:
                    del d[k - mod]
            else:
                if mod not in d:
                    d[mod] = 0
                d[mod] += 1
        
        return len(d) == 0