class Solution:         # Here's the plan:
                        #   1) 1a: Initiate an array offsets with length len(s)+1. 
                        #      1b: Iterate through shifts and collect the endpts and the direction
                        #          of each shift. (Note that 2*(0)-1 = -1 and 2*(1)-1 = 1.)
                        #      1c: Accumulate the elements in offsets to determine the cummulative
                        #          offset for each char in s
                        # 
                        #   2) 2a: Write the letter index (1-26) of each char of s to a list chNums. 
                        #      2b: Add to each letter index its corresponding offset and determine 
                        #          its new letter index by applying %26.
                        #      2c: Return the result string from chNums. 

    def solution_1645_2(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)

        offsets = [0]*(n+1)                                     # <-- 1a
		
        for start, end, direction in shifts:                    # <-- 1b
            offsets[start]+= 2*direction-1
            offsets[end+1]-= 2*direction-1
			
        offsets = accumulate(offsets)                           # <-- 1c

        chNums = (ord(ch)-97 for ch in s)                       # <-- 2a
		
        chNums = ((chNum + offset)%26 for chNum,                # <-- 2b
                   offset in zip(chNums, offsets))

        return ''.join(chr(chNum+97) for chNum in chNums)       # <-- 2c