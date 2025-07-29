class Solution:
    def solution_1405_4(self, s: str, queries: List[List[int]]) -> List[int]:
        """
        Use of Prefix Sum Logic and
        some additional memory to store closest plate to the left and right of given index
        """
        n = len(s)
        # finds next candle to Right of given Index
        nextCandle2R = [0]*n
        
        # finds next candle to Left of given Index
        nextCandle2L = [n]*n
        
        # prefix array storing cumulative plates upto given index i in string 's' at cumPlates[i+1]
        cumPlates = [0]*(n+1)
        
        candleL = -1
        count = 0
        for i in range(n):
            if s[i] == '*':
                count +=1
            cumPlates[i+1] = count
            if s[i] == '|':
                candleL = i
            nextCandle2L[i] = candleL
        
        candleR = n
        for i in range(n-1,-1,-1):
            if s[i] == '|':
                candleR = i
            nextCandle2R[i] = candleR
        """
        print("total length of s: ",n)
        print("nextcandle 2 left of given index: ",nextCandle2L)
        print("nextcandle 2 right of given index: ",nextCandle2R)
        print("prefix array: ",cumPlates)
        """
        ans = []
        
        for query in queries:
            start = query[0]
            end = query[1]
            #print(start,end)
			
			# find next closest plate to right of 'start' in s
            next_plateR = nextCandle2R[start]
			# find next closest plate to left of 'end' in s
            next_plateL = nextCandle2L[end]
            if next_plateL < next_plateR:
                ans.append(0)
            else:
                ans.append(cumPlates[next_plateL+1]-cumPlates[next_plateR+1])
            
        return ans