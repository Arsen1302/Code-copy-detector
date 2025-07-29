class Solution:
    def solution_45_5(self, s: str) -> int:
        
        n = len(s)
		# mp denotes how many min cuts needed till ith index.
        mp = {
            i:i
            for i in range(-1,n)
        }
        
        for i in range(n):
            mp[i] = min(mp[i],1+mp[i-1]) # if not palindrome add one more partition in i-1th count of partition
            
			# take the ith index as mid of palindrome for both even and odd length of palindrome
			# and test if this makes a palindrome if indexes j and k travel both sides. capture the
			# minimum length comes in the process.
            for j,k in [[i,i+1],[i-1,i+1]]:                
                while j>=0 and k<n and s[j]==s[k]:
                    mp[k] = min(mp[j-1]+1,mp[k])
                    j-=1
                    k+=1
        return mp[k-1]