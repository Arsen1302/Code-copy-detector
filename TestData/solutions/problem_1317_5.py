class Solution:
    def solution_1317_5(self, s: str) -> int:
        indices = {}
        for i in range(len(s)):
            if s[i] in indices:
                indices[s[i]][1] = i
            else:
                indices[s[i]] = [i, i]
        count = 0
		
		#indices[char] denotes first and last occurrence of char in the given string 
		
        for c in indices:
            if indices[c][0] == indices[c][1]:
				#if the character occurs only once in the given string
                pass
            else:
                tempAdded = set()
                for i in range(indices[c][0]+1, indices[c][1], 1):
					#counts the number of distinct middle character in the three lettered palindrome that could be formed with c at either ends
                    tempAdded.add(s[i])
                count += len(tempAdded)
        return count