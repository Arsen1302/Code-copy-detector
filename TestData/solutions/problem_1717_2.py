class Solution:
    def solution_1717_2(self, message: str, limit: int) -> List[str]:
        if limit <= 5: return []
        
        # Important: Determine number of digit of b. BS monotone holds for same digit-count  
        # This will fix the testcase like: message = "abbababbbaaa aabaa a", limit = 8
        nd = -1
        for dc in range(1, 7):
            remain = len(message)
            for d in range(1, dc+1): 
                if limit - 3 - d - dc < 0: break
                remain -= (limit - 3 - d - dc)*9*10**(d-1)
            if remain <= 0:
                nd = dc
                break
        if nd == -1: return []
        
        # binary search of b
        start, end = 10**(nd - 1), 10 ** nd
        while start != end:
            mid = (start + end) // 2
            dc = len(str(mid))
            remain = len(message) 
            for d in range(1, dc):
                remain -= (limit - 3 - d - dc)*9*10**(d-1)
            for i in range(10**(dc-1), mid + 1):
                remain -= limit - 3 - 2*dc 
                if remain < 0: break
            # print(start, end, mid, remain)
            if remain > 0: start = mid + 1
            else: end = mid

        # construct answer
        ans = []
        dc = len(str(start))
        cur = 0
        for d in range(1, dc + 1):
            for i in range(10**(d-1), 10**d):
                nxt = min(cur + limit - 3 - d - dc, len(message))
                ans.append(message[cur:nxt] + '<' + str(i) + '/' + str(start) + '>')
                cur = nxt
                if nxt >= len(message): break
                
        if cur < len(message): return []
        return ans