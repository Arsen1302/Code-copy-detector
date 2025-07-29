class Solution:
    def solution_430_2(self, source: List[str]) -> List[str]:
        ans = []
        comment = False # True for block comment 
        
        for line in source: 
            if not comment: ans.append([]) # if not started as comment
            i = 0
            while i < len(line): 
                if comment: 
                    if line[i:i+2] == "*/": 
                        comment = False 
                        i += 1
                else:  
                    if line[i:i+2] == "//": break 
                    elif line[i:i+2] == "/*": 
                        comment = True 
                        i += 1
                    else: ans[-1].append(line[i])
                i += 1
        return filter(None, map("".join, ans))