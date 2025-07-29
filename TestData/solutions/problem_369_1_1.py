class Solution:
    def solution_369_1_1(self, price: List[int], special: List[List[int]], needs: List[int]) -> int:
        n = len(price)
        @lru_cache(maxsize=None)
        def solution_369_1_2(needs):
            ans = sum([i*j for i, j in zip(price, needs)]) 
            cur = sys.maxsize
            for s in special:
                new_needs, ok = [], True
                for i in range(n):
                    need, give = needs[i], s[i]
                    if need < give:  # if over purchase, ignore this combination
                        ok = False
                        break
                    new_needs.append(need-give)    
                if ok: cur = min(cur, solution_369_1_2(tuple(new_needs)) + s[-1])
            return min(ans, cur)
        return solution_369_1_2(tuple(needs))