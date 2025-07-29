class Solution:
#     Runtime: 42ms 67.78% Memory: 13.9mb 19.81%
# O(n) || O(1)
    def solution_494_2(self, widths, s):
        newLine = 1
        
        width = 0
        
        for char in s:
            charWidth = widths[ord(char) - ord('a')]
            
            if charWidth + width > 100:
                newLine += 1
                width = 0
                
            width += charWidth
                
        return [newLine, width]