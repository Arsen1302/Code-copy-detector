class Solution:
    def solution_1503_4(self, s: str, t: str) -> int:
        count1 = [0]*26
        count2 = [0]*26
        for i in s:
            count1[ord(i)-ord('a')] += 1
        for i in t:
            count2[ord(i)-ord('a')] += 1
        
        steps = 0
        for i in range(26):
            steps += abs(count1[i]-count2[i])
        
        return steps