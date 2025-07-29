class Solution:
    def solution_946_1(self, n: int, k: int) -> str:
        
        char = ["a", "b", "c"]  
        
        # Edge case, n = 1
        if n == 1: return char[k - 1] if k <= 3 else ""
        
        # There will be $part$ number of strings starting with each character (a, b, c)
        part = 2 ** (n - 1)
        
        # If k is too large
        if k > part * 3: return ""
        
        res = []
        
        # Edge case is k = n * i, where i is an integer in range [1, 3]
        res.append(char[k // part if k % part != 0 else k // part - 1])
        k = k % part if k % part != 0 else part
        
        for i in range(n - 2, -1, -1):
            char = ["a", "b", "c"]  
            char.remove(res[-1])        # Make sure the adjacent characters will be different
            
            if len(res) + 1 == n:       # Edge case, assigning the last element
                if k == 1: res.append(char[0])
                elif k == 2: res.append(char[-1])
            elif k > 2 ** i:            # Go to the right side
                res.append(char[-1])
                k -= 2 ** i       
            else: res.append(char[0])   # Go to the left side
        
        return "".join(res)