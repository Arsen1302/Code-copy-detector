class Solution:
    def solution_1527_5(self, queries: List[int], intLength: int) -> List[int]:
        if intLength == 1:
            return [ i if i < 10 else -1 for i in queries ]
        else:
            start = 10**(intLength//2-1)
            end   = 10**(intLength)
            res = []
            for q in queries:
                q -= 1
                if intLength%2:
                    temp = str(start+q//10 ) + str(q%10) + str(start+q//10 )[::-1]
                else:
                    temp = str(start+q) +str(start+q )[::-1]
                temp = int(temp) if int(temp) < end else -1
                res.append(temp)
        return res