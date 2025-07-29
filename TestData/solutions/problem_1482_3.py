class Solution:
    def solution_1482_3(self, s: str, power: int, modulo: int, k: int, hashValue: int) -> str:
        p=0
        mul=1
        for i in range(k):
            p=p+(ord(s[i])-ord('a')+1)*mul
            mul=mul*power
        mul=mul//power
        for j in range(len(s)-k+1):
            if p%modulo==hashValue:
                return s[j:j+k]
            if j<len(s)-k:
                p=(p-(ord(s[j])-ord('a')+1))//power+(ord(s[j+k])-ord('a')+1)*mul