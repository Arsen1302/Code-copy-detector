class Solution:
    def solution_553_2_1(self, n: int) -> int:
        def solution_553_2_2(n):
            if n == 1: return False
            for i in range(2, int(n**0.5)+1):
                if n % i == 0: return False
            return True                
        
        n_str = str(n)
        l = len(n_str)        
        for k in range(max(0, l//2-1), 5):
            for i in range(10**k, 10**(k+1)):                            # odd length
                i_str = str(i)
                if k > 0 and i_str[0] in ['2','4','5','6','8']: continue # pruning
                cur = i_str + i_str[-2::-1]
                cur_int = int(cur)
                if cur_int >= n and solution_553_2_2(cur_int): 
                    return cur_int
                
            for i in range(10**k, 10**(k+1)):                            # even length
                i_str = str(i)
                if i_str[0] in ['2','4','5','6','8']: continue           # pruning
                cur = i_str + i_str[::-1]
                cur_int = int(cur)
                if cur_int >= n and solution_553_2_2(cur_int): 
                    return cur_int
        return -1