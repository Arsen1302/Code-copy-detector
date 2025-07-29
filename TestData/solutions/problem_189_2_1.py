class Solution:
    def solution_189_2_1(self, n):
                        # For an interval [l,r], we choose a num, which if incorrect still
                        # allows us to know whether the secret# is in either [l,num-1] or
                        # [num+1,r]. So, the worst-case (w-c) cost is
                        #
                        #      num + max(w-c cost in [l,num-1], w-c cost in [num+1,r])
                        # 
                        # We do this by recursion and binary search, starting with [1,n].

        @lru_cache(None)              # <-- we cache function results to avoid recomputing them
        def solution_189_2_2(l = 1, r = n)-> int:
            if r-l < 1: return 0      # <-- base case for the recursion; one number in [l,r]       
            ans = 1000                # <-- the answer for n = 200 is 952
            
            for choice in range((l+r)//2,r):
                ans = min(ans,choice+max(solution_189_2_2(l,choice-1),solution_189_2_2(choice+1,r)))

            return ans

        return solution_189_2_2()