class Solution:
    def solution_1717_3(self, message: str, limit: int) -> List[str]:
        prefix = b = 0 
        while 3 + len(str(b))*2 < limit and len(message) + prefix + (3+len(str(b)))*b > limit * b: 
            b += 1
            prefix += len(str(b))
        ans = []
        if 3 + len(str(b))*2 < limit: 
            i = 0 
            for a in range(1, b+1): 
                step = limit - (len(str(a)) + len(str(b)) + 3)
                ans.append(f"{message[i:i+step]}<{a}/{b}>")
                i += step 
        return ans