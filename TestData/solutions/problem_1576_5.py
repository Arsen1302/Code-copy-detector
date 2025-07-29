class Solution:
    def solution_1576_5(self, num: str) -> bool:
        leng = len(num)
        freq = {}
        
        for i in range(leng):
            freq[str(i)] = 0
            
        for i in range(leng):
            if num[i] in freq:
                freq[num[i]] += 1
        
        for i in range(leng):
            if num[i] == str(freq[str(i)]):
                continue
            else:
                return False
            
        return True