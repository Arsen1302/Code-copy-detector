class Solution:
    def solution_1134_3(self, nums: List[int], k: int) -> int:
        sol = {}
        cnt = 0
        
        for el in nums: 
            if el < k:
                if el in sol:
                    sol[el] -= 1
                    cnt += 1
                    if sol[el] == 0:
                        sol.pop(el)
                else:
                    sol[k-el] = sol.get(k-el, 0) + 1
        
        return cnt