class Solution:
    def solution_1137_3(self, allowed: str, words: List[str]) -> int:
        
        """Brute Force
        Time complexity : O(n*m) where m = max(len(word) in words)
        Space complexity: O(1)
        """
        
        count = 0
         for word in words:
             for ch in word:
                 if ch not in allowed:
                     count += 1
                     break

         return len(words)-count
        
		
		
        """One liner
        Set operation

        """
        return sum(not set(word)-set(allowed) for word in words)


		"""Set operation by subset operation
		NOTE : SPACE COMPLEXITY INCREASES IN THIS APPROACH.
		"""
		allowed = set(allowed)
		n = 0
		for w in words:
			if set(w).issubset(allowed):
				n += 1
		return n