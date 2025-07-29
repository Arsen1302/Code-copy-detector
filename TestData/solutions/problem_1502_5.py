class Solution:
    def solution_1502_5(self, words: List[str], pref: str) -> int:
        
        pref_len=len(pref)
        count=0
        for i in words:
            if pref==i[:pref_len]:
                count+=1
        return count