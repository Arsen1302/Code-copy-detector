class Solution:
    def solution_1500_5(self, s: str, repeatLimit: int) -> str:
        hmap = OrderedDict(Counter(s))
        hmap = dict(sorted(hmap.items(), key = lambda x: x[0], reverse=True))
        result = ""
        
        while len(hmap) > 0:
            keys = list(hmap.keys())
            first = keys[0]
            
            if hmap[first] > repeatLimit:
                result += first * repeatLimit
                hmap[first] -= repeatLimit
                if len(hmap) == 1:
                    return result
                result += keys[1]
                hmap[keys[1]] -= 1
                
                if hmap[keys[1]] == 0:
                    del hmap[keys[1]]
            else:
                result += first * hmap[first]
                del hmap[first]
        return result