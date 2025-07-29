class Solution:
    def solution_1113_3(self, s: str) -> int:
        freqs=[0]*26 # capture count of all lowercase characters
        
        for c in s:
            freqs[ord(c)-ord('a')]+=1
        
        freqs.sort(reverse=True) # reverse sort: O(nlogn)
        
        deletions=0
        
        #initialize with max allowed frequency
        # eg: if 5 is taken, then the next best frequency count is 4
        # hence, max_freq = 5 - 1 = 4        
        max_freq=freqs[0]-1  # set max frequency upper limit
        
        for freq in freqs[1:]:
            # if a character frequency is above freq, it means it needs to be reduced
            # eg: if max_freq=4, then it means all counts above 4 has been already allotted
            # So we need to reduce the current frequency
            
            if freq>max_freq:
                deletions+=freq-max_freq # update the deletions count
                freq=max_freq
            max_freq=max(0, freq-1) # update the max frequency upper limit
        
        return deletions