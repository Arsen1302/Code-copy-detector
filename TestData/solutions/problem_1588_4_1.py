class Solution:
    def solution_1588_4_1(self, s, sub, mappings):
        h = defaultdict(int)
        
		# put mappings in hashmap data structure. 
        for k, v in mappings:
            if k not in h:
                h[k] = {v: 1}
            else:
                h[k][v] = 1
                
        siter = 0
        subiter = 0
        jump = -1
        
        # Iterate through the string 's' and locate jump points as we go. 
        while siter < len(s):
			
			# two chars are equal if they are same in both strings or mapping / replacement equates them
            if s[siter] == sub[subiter] or (sub[subiter] in h and s[siter] in h[sub[subiter]]):
            
				# keep track of jump location of next string if we encounter a start char while in the middle of an evaluation.
				# abbabbc would have two 'a' chars to start evaluating substring 'abbc'
				jump = siter if (s[siter] == sub[0] and subiter > 0) else -1
                
				subiter += 1
                if subiter == len(sub):
                    return True
            else:
				# relocate the jump point to previously encoutered start character.
                siter = (jump-1) if jump != -1 else siter
                
                if s[siter] == sub[0] and jump == -1:
                    siter -= 1
                
                subiter = 0 
                jump = -1
                
            siter += 1
            
        return False
                
    def solution_1588_4_2(self, s, sub, mappings):
        h = defaultdict(dict)
        S = len(s)
        SU = len(sub)
        
        for k, v in mappings:
            if k not in h:
                h[k] = {v: 1}
            else:
                h[k][v] = 1
                        
        solution_1588_4_2 = [[0 for _ in range(S)] for _ in range(SU)]
        
        for subiter in range(SU):
            for siter in range(S):
                if sub[subiter] == s[siter]: 
                    solution_1588_4_2[subiter][siter] = solution_1588_4_2[subiter-1][siter-1] + 1
                elif solution_1588_4_2[subiter-1][siter-1]:
                    if (sub[subiter] in h and s[siter] in h[sub[subiter]]):
                        solution_1588_4_2[subiter][siter] = solution_1588_4_2[subiter-1][siter-1] + 1
                        
                if solution_1588_4_2[subiter][siter] == len(sub):
                    for d in solution_1588_4_2:
                        print ("".join([str(i) for i in d]))                    
                    return True
            
        return False
    
    def solution_1588_4_3(self, s: str, sub: str, mappings: List[List[str]]) -> bool:
        return self.solution_1588_4_1(s, sub, mappings)