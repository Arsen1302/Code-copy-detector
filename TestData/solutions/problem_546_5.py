class Solution:
    def solution_546_5(self, A: str, B: str) -> bool:
        
        if len(A)!=len(B) or set(A)!=set(B):
            return False
        
        if A==B: #must have atleast 1 rep char
            return len(A)!=len(set(A))
        
        
        #A and B now same length, lets swap
        firstMissMatch=0
        flagOK=0
        
        for a,b in zip(A,B):
            if a==b: continue  #if letters are qual just continue
            if not firstMissMatch:  #if this is the firstMistMatch, flip firstMissMatch flap to 1 and store the chars
                swapA,swapB=a,b
                firstMissMatch=1
            elif flagOK==0: #i.e: this is the 2nd mismatch, need to check if the chars to be swapped are equal to the previous mismatch
                flagOK=1 if a==swapB and b==swapA else 2
            else:
                return False #meaning more than 1 mismatch appeared
        return flagOK==1 #if flag=0 (no swap) or flag=2 (swap but letters dont match i.e: A=abcaa and B=abcbb) return False