class Solution:
    def solution_1684_2(self, num1: int, num2: int) -> int:
        numBitsToSet = 0
        while num2:
            numBitsToSet += num2 &amp; 1
            num2 = num2 >> 1
        
        num1Str = bin(num1)[2:]
        num1Len = len(num1Str)
        
        outLen = max(num1Len, numBitsToSet)
        out = ['0' for i in range(outLen)]
        
        num1Str = '0'*(outLen-num1Len) + num1Str
        
        #print('numBitsToSet', numBitsToSet, 'num1Len', num1Len, 'num1Str', num1Str, 'outLen', outLen)
        
        # Match the 1s of num1
        for i in range(outLen):
            if numBitsToSet == 0:
                break
            if num1Str[i] == '1':
                out[i] = '1'
                numBitsToSet -= 1
        
        # Set minimal bits that are 0
        for i in range(outLen-1, -1, -1):
            if numBitsToSet == 0:
                break
            if out[i] == '0':
                out[i] = '1'
                numBitsToSet -= 1
        
        #print('Modified out', out)
        return int(''.join(out), 2)