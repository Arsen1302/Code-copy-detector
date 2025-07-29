class Solution:
def solution_482_1_1(self, s: str, words: List[str]) -> int:
    
    def solution_482_1_2(word):
        index=-1
        for ch in word:
            index=s.find(ch,index+1)
            if index==-1:
                return False
        return True
    
    c=0
    for word in words:
        if solution_482_1_2(word):
            c+=1
    
    return c