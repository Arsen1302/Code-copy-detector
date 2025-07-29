class Solution:
    def solution_1592_5_1(self, cookies, k):
        if k == len(cookies):
            return max(cookies)

        self.min_val = float("inf")

        def solution_1592_5_2(idx,ans):
            if idx == len(cookies):
                self.min_val = min(self.min_val,max(ans))
                return

            seen = set()

            for i in range(k):
                if ans[i] in seen: continue
                if ans[i] + cookies[idx] >= self.min_val: continue
                seen.add(ans[i])
                
                ans[i] += cookies[idx]
                solution_1592_5_2(idx+1,ans)
                ans[i] -= cookies[idx]

        solution_1592_5_2(0, [0]*k)
        
        return self.min_val