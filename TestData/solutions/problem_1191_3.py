class Solution(object):
    def solution_1191_3(self, w1, w2):
        i=j=0
        s=""
		
        while i<len(w1) and j<len(w2):
		
            if w1[i] > w2[j]:
                s+=w1[i]
                i=i+1
				
            elif w1[i] < w2[j]:
                s+=w2[j]
                j=j+1
				
            elif w1[i:] > w2[j:]:
                s+=w1[i]
                i+=1
				
            else:
                s+=w2[j]
                j+=1
        
        while i<len(w1):
            s=s+w1[i]
            i=i+1
			
        while j<len(w2):
            s=s+w2[j]
            j=j+1
			
        return s