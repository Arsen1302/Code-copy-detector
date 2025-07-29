class Solution:
    def solution_1643_4(self, blocks: str, k: int) -> int:
        #Simple-Approach (Sliding Window)
        #Runtime:32ms 
        minimum_change=k     #Worst Case scenario if all blocks are white minimum change required is k times
        for i in range(0,len(blocks)):
            count_b=blocks[i:i+k].count("B")  #Count Blacks
            if(count_b>=k):                   #If Count Blacks > desired number of consecutive black blocks return 0
                return 0
            minimum_change=min(minimum_change,k-count_b)     #updating the minimum change  
        return minimum_change