class Solution:
    def solution_275_2(self, n: int) -> int:
        ref = "122112"
        actual = ""
        start = 0
        one = True
        
        while(len(ref) < n):
            for i in range(start, len(ref)):
                if(one):
                    actual += int(ref[i]) * "1"
                    one = False
                else:
                    actual += int(ref[i]) * "2"
                    one = True
                    
            if(len(actual) > len(ref)):
                start = len(ref)
                ref = actual
        
        return ref[:n].count("1")