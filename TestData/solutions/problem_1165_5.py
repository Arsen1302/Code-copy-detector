class Solution:
    def solution_1165_5(self, encoded: List[int], first: int) -> List[int]:
        encoded.insert(0, first)
        
        for i in range(1, len(encoded)):
            encoded[i] = encoded[i-1] ^ encoded[i] 
       
            
        return encoded