class Solution:
    def solution_1184_3_1(self, s: str) -> bool:
		# Add bogus characters to s, so we only have to worry about odd palindromes.
        s = "|" + "|".join(s) + "|"
        
		# p[i] is the length of the longest palindrome centered at i, minus 2.
        p = [0] * len(s)
        
		# c is the center of the longest palindrome found so far that ends at r.
		# r is the index of the rightmost element in that palindrome; c + p[c] == r.
        c = r = 0
        
        for i in range(len(s)):
			# The mirror of i about c.
            mirror = c - (i - c)
            
			# If there is a palindrome centered on the mirror that is also within the
			# c-palindrome, then we dont have to check a few characters as we
			# know they will match already.
            p[i] = max(min(r - i, p[mirror]), 0)
			
			# We expand the palindrome centered at i.
            a = i + (p[i] + 1)
            b = i - (p[i] + 1)
            while a < len(s) and b >= 0 and s[a] == s[b]:
                p[i] += 1
                a += 1
                b -= 1
            
			# If the palindrome centered at i extends beyond r, we update c to i.
            if i + p[i] > r:
                c = i
                r = i + p[i]
		
		@lru_cache(None)
        def solution_1184_3_2(i, k):
            # can s[i:] be decomposed into k palindromes
            mid = i + ((len(p) - i) // 2)
            if k == 1:
				# s[i:] itself must be a palindrome
                return p[mid] == mid - i
            
            for j in range(mid, i - 1, -1):
				# p[j] == j - i means s[i:j + p[j]] is a palindrome
                if p[j] == j - i and solution_1184_3_2(j + p[j], k - 1):
                    return True
            return False
            
        return solution_1184_3_2(0, 3)