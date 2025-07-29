class Solution:
    def solution_1246_4(self, sentence: str) -> bool:
        
        # naive approach - 1
        # freq = {}
        # for i in sentence:
        #     freq[i] = freq.get(i, 0) + 1
        # if len(freq) == 26: return True
        # return False
        
        # optimized approach - 2
        occurred = 0
        for i in sentence:
            temp = ord(i) - ord('a')
            occurred |= (1 << temp)
        if occurred == (1 << 26) - 1:
            return True
        return False