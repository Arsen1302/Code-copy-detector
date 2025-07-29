class Solution:
    def solution_723_4(self, S: str) -> str:
        hi, lo = len(S) - 1, 0
        ans = ''
        while lo <= hi:
            mid = (hi + lo) // 2 
            substring_set = set()
            M = memoryview(S.encode('utf-8'))
            for i in range(mid, len(S) + 1):
                sub = M[i-mid:i]
                if sub in substring_set:
                    ans = str(sub, 'utf-8')
                    lo = mid+1
                    break
                else:
                    substring_set.add(sub)
            else:
                hi = mid - 1
                
        return ans