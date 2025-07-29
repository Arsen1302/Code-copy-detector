class Solution:
    def solution_203_2(self, s: str, t: str) -> bool:
        i, j, n, m = 0, 0, len(s), len(t)
        while i < n and j < m: # Loop till any of the strings is fully traversed
			if s[i] == t[j]: # If char at i and j are equal then update i
				i += 1 
			# Could also write i += s[i]==t[j]
            j += 1 # Update j always.
        return i == n