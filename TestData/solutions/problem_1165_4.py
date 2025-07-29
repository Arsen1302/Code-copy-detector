class Solution:
    def solution_1165_4(self, encoded: List[int], first: int) -> List[int]:
		ans = [first]
        
        for i in range(len(encoded)):
            ans.append(encoded[i] ^ ans[-1]) 
       
            
        return ans