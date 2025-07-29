class Solution:
    def solution_804_5_1(self, n: int) -> int:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        self.adj = {
            '0': list(vowels),
            'a': ['e'],
            'e': ['a', 'i'],
            'i': list(vowels - {'i'}),
            'o': ['i', 'u'],
            'u': ['a']
        }
        @functools.cache
        def solution_804_5_2(prev, n):
            if n == 0: return 1
            res = 0
            for cur in self.adj[prev]:
                res = (res + solution_804_5_2(cur,n-1)) % (10**9+7)
            return res
    
        return solution_804_5_2('0', n)
    
    # LOG N is possible WOW https://leetcode.com/problems/count-vowels-permutation/discuss/398173/C%2B%2B-Bottom-up-Recursive-DPs-O(n)-and-Matrix-Exponentiation-O(logn)