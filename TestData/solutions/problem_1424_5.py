class Solution:
    def solution_1424_5(self, k: int, n: int) -> int:
        
        # start from single digit base k
        cands = [str(i) for i in range(1, k)]
        ans = 0
        
        while n > 0:
            # check current canddiates to see if base 10 is also mirroring
            for cand in cands:
                b10 = str(int(cand, k))
                if b10 == b10[::-1]:
                    ans += int(b10)
                    n -= 1
                    if n == 0: return ans

            # construct new candidates 
            # if previous cand length is even just insert number between 0 and k - 1 into the middle
            # if previous cand length is odd just insert number after len//2+1 and should be the same with left part end digit
            new_cands = []
            for cand in cands:
                m = len(cand)
                for i in range(k):
                    if m % 2 == 0:
                        new_cands.append(cand[:m//2] + str(i) + cand[m//2:])
                    else:
                        left, right = cand[:m//2+1], cand[m//2+1:]
                        if str(i) == left[-1]:
                            new_cands.append(left + str(i) + right)
            cands = new_cands

            
        
        return ans