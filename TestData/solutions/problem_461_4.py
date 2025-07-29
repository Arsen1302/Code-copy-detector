class Solution:
    def solution_461_4(self, s: str) -> str:
        count = Counter(s) # O(N)
        most_common_c = max(count.items(), key=itemgetter(1))[0] # O(N)
        if count[most_common_c] > (len(s)+1)//2:
            return ""
        
        output = ['']*len(s)        
        i = 0
        for _ in range(count[most_common_c]):
            output[i] = most_common_c
            i += 2
        
        count[most_common_c] = 0
        
        for k, v in count.items():
            for _ in range(v):
                if i >= len(s):
                    i = 1
                output[i] = k
                i += 2
                
        return "".join(output)