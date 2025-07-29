class Solution:
    def solution_1246_1(self, sentence: str) -> bool:
        lst=[0]*26
        for i in sentence:
            lst[ord(i)-ord('a')]+=1
        return 0 not in lst