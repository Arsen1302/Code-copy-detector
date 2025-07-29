class Solution:
    def solution_977_3(self, s: str, k: int) -> int:
 
        n = len(s)
        
        vowels = { 'a', 'e', 'i', 'o', 'u' }
        count = 0 
        # Step 1 : We will find number of vowels in the first substring of length k : from 0th index till (k-1)th index
        for i in range(0, k):
            if s[i] in vowels:
                count += 1
        
        
        # record for maximum vowel count in substring
        max_vowel_count = count
        
        
        # sliding window of size k
        # starts from k and window from [0, k-1] inclusive is already considered
        for tail_index in range(k, n):
            
            head_index = tail_index - k
            head_char, tail_char = s[head_index], s[tail_index]
            
            if head_char in vowels:
                count -= 1
                
            if tail_char in vowels:
                count += 1
                
            max_vowel_count = max(max_vowel_count, count)
            
        
        return max_vowel_count