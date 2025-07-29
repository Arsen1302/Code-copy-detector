class Solution:
    def solution_771_4(self, text: str) -> int:
        begin, end = 0, len(text) - 1
        count = 0
        
        left, right = [], []
        
        for i in range(len(text)):
            left.append(text[i])
            right.append(text[len(text) - i - 1])
            
            if left == list(reversed(right)):
                count += 1
                left, right = [], []
        
        return count