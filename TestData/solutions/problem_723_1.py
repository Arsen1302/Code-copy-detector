class Solution:
    def solution_723_1(self, s: str) -> str:
        length = len(s)
        l,r = 0, length-1        
        result = []
        while l<r:
            mid = (l+r)//2
            d = {}
            max_string = ""
            for i in range(length-mid):
                    if d.get(s[i:i+mid+1],0):
                        max_string = s[i:i+mid+1]
                        break
                    d[s[i:i+mid+1]] = 1
            if max_string:
                l = mid+1
                result.append(max_string)
            else:
                r = mid
        return max(result,key=len) if result else ""