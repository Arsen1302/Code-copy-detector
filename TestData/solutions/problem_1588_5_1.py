class Solution:
    def solution_1588_5_1(self, s: str, sub: str, mappings: List[List[str]]) -> bool:
        dic=defaultdict(set)
        for k,v in mappings:
            dic[k].add(v) # dic{'t':set{'l','3'}, 'e':set{'4'}} as an example
        
        def solution_1588_5_2(toCheck,sub): # Here len(toCheck) = len(sub)
            for char_check, char_sub in zip(toCheck, sub):
                if char_check != char_sub and char_check not in dic[char_sub]:
                    return False
            return True                   
            
        for start in range(len(s)-len(sub)+1):
            if solution_1588_5_2(s[start:start+len(sub)],sub): # solution_1588_5_2 sliding window with length of sub
                return True

        return False