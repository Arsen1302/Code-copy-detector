class Solution:
    def solution_981_3(self, s: str, k: int) -> bool:             
        required_count=1<<k  # same as 2 ^ k
        seen=[False] * required_count
        mask=required_count-1
        hash_code=0
        
        for i in range(len(s)):
            hash_code = ((hash_code<<1) &amp; mask) | (int(s[i]))
            if i>=k-1 and not seen[hash_code]:
                seen[hash_code]=True
                required_count-=1
                if required_count==0:
                    return True
                                
        return False