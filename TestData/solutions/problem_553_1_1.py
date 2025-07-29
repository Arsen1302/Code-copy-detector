class Solution:
    def solution_553_1_1(self, N: int) -> int:
        def solution_553_1_2(N):
            return N > 1 and all(N % d for d in range(2, int(N**0.5)+1))
        
        # N must be a palindrome with odd number of digits.
        # The return value will have odd number of digits too.
        def solution_553_1_3(N):
            if N in [999, 99999, 9999999]:
                return (N + 1) * 10 + 1
            n = str(N // 10 ** (len(str(N))//2) + 1)
            return int(n + n[-2::-1])
        
        if N <= 11: 
            while not solution_553_1_2(N):
                N += 1
            return N
        
        if (digits := len(str(N))) % 2 == 0:
            N = 10 ** digits + 1
        else:
            n = str(N // 10 ** (len(str(N))//2))
            if (p := int(n + n[-2::-1])) >= N:
                N = p
            else:
                N = solution_553_1_3(p)
                
        while not solution_553_1_2(N):
            N = solution_553_1_3(N)
        return N