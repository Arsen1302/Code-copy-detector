class Solution:
    def solution_1065_3(self, s: str) -> str:
        # covert string to array, so we can replace letter in-place
        result = [w for w in s]
        N = len(result)
        
        for i in range(N):
            if result[i] == '?':
                pre = result[i-1] if i-1 >= 0 else ''
                nxt = result[i+1] if i+1 < N else ''
                
                # only need to check 3 letters to avoid consecutive repeating chars
                for w in ['a', 'b', 'c']:
                    if w != pre and w != nxt:
                        result[i] = w
                        break
            
        return ''.join(result)