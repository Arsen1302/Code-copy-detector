class Solution:
    def solution_557_3(self, A: List[int], B: List[int]) -> List[int]:
        B, key = zip(*sorted(zip(B, list(range(len(B)))))) # sort it ascending 
        adv, rem = [], [] # advantage &amp; remaining 
        i = 0
        for x in sorted(A): 
            if x > B[i]: 
                adv.append(x)
                i += 1
            else: rem.append(x)
        return list(zip(*sorted(zip(key, adv+rem))))[1] # sort it back