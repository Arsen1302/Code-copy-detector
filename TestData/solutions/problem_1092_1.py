class Solution:
    def solution_1092_1(self, a: str, b: str) -> bool:
        
        fn = lambda x: x == x[::-1] # check for palindrome 
        
        i = 0
        while i < len(a) and a[i] == b[~i]: i += 1
        if fn(a[:i] + b[i:]) or fn(a[:-i] + b[-i:]): return True 
        
        i = 0
        while i < len(a) and a[~i] == b[i]: i += 1
        if fn(b[:i] + a[i:]) or fn(b[:-i] + a[-i:]): return True 
        
        return False