class Solution:
    def solution_653_3_1(self, s: str, t: str) -> bool:
        
        def solution_653_3_2(s):
            """Return normalized string."""
            if "." not in s: return s # edge case - xxx 
            xxx, frac = s.split('.')
            if not frac: return xxx # edge case - xxx.
            if '(' in frac: 
                nonrep, rep = frac.split('(')
                rep = rep.rstrip(')')
                while nonrep and rep and nonrep[-1] == rep[-1]: # normalize repeating part 
                    nonrep = nonrep[:-1]
                    rep = rep[-1] + rep[:-1]
                    
                if len(rep) > 1 and len(set(rep)) == 1: rep = rep[0] # edge case (11)
                if rep[:2] == rep[2:]: rep = rep[:2] # edge case (1212)
                    
                if rep == "0": rep = "" # edge case - (0)
                if rep == "9": # edge case - (9)
                    rep = ""
                    if nonrep: nonrep = nonrep[:-1] + str(int(nonrep[-1]) + 1)
                    else: xxx = str(int(xxx) + 1)
                frac = ""
                if rep: frac = f"({rep})"
                if nonrep: frac = nonrep + frac
            if '(' not in frac: # remove trailing 0's
                while frac and frac[-1] == '0': frac = frac[:-1]
            return xxx + "." + frac if frac else xxx
        
        return solution_653_3_2(s) == solution_653_3_2(t)