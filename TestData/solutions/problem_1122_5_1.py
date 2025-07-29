class Solution:
    def solution_1122_5_1(self, word1, word2):
        """
        The below solutions take O(n + m) time and space, as we are 
            * Iterating through both list (Time complexity : O(n+m))
            * Adding strings each time. In the backend a new string is created 
                with increased size. (Space complexity O(n+m))

        However, we can optimized it. Suppose if the first character doesnot match than the whole
        concatenation was unecessary. 
        So the Idea is to compare the character in the strings on the fly.

        We can skip building the strings and only compare the individual characters using space O(1).
        It also saves time as we will not be going through the whole list if any characters mismatched.

        We can use a generator or a pointer approach to solve this problem.
		Time complexity : O(n) if n<m else O(m)
		Space complexity: O(1)
        """
        def solution_1122_5_2(word):
            for w in word:
                for c in w:
                    yield c

            yield None
            
            
        for c1, c2 in zip(solution_1122_5_2(word1), solution_1122_5_2(word2)):
            if c1 != c2:
                return False
        return True


        
        """Brute Force approach
        Time complexity : O(n^2 + m^2)
        Space complexity: O(n+m) #debatable
        """
#         str1 = str2 = ""
        
#         for s in word1:
#             str1 += s
#         for s in word2:
#             str2 += s
            
#         return str1==str2
    
        """One liner
        Time complexity : O(n+m)
		Space complexity : O(1)
        """
        # return ''.join(word1) == ''.join(word2)