class Solution:
    def solution_1258_1_1(self, s: str) -> bool:
        
        """
        Time = O(2^N)
        Space = O(N) space from stack
        
        """
        def solution_1258_1_2(index: int, last: int) -> bool:
            if index == len(s):
                return True
            
			# j: [index, len(s)-1]
            for j in range(index, len(s)):
				# cur: [index, index] ~ [index, len(s)-1]
                cur = int(s[index:j + 1])
				# last: [...,index-1]
				# cur: [index+1, j]
				# last = cur -> next: [j+1,...)
				# DFS condition: cur = last - 1 &amp;&amp; solution_1258_1_2(j+1, cur) == true
                if cur == last - 1 and solution_1258_1_2(j + 1, cur):
                    return True
            return False
        
        for i in range(len(s) - 1):
            last = int(s[:i+1])
            if solution_1258_1_2(i + 1, last):
                return True
        return False