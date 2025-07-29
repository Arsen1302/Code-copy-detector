class Solution:
    def solution_1691_4(self, n: int, queries: List[List[int]]) -> List[int]:
        MOD = (10**9)+7
        powers, res = [], []
        
        binary_list = [int(i) for i in bin(n)[2:]] # convert n to binary
        
        for i, n in enumerate(binary_list[::-1]): # create powers list
            if n: 
                powers.append(pow(2, i))
                
        for i in range(1, len(powers)): # prefix product
            powers[i] = powers[i] * powers[i-1]   
            
        for l, r in queries:
            if l == 0: 
                res.append(powers[r] % MOD)
            else: 
                res.append((powers[r] // powers[l-1]) % MOD)
                
        return res