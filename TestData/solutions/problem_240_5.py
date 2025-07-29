class Solution:
    def solution_240_5(self, s: str, p: str) -> List[int]:
        target = [0]*26
        for letter in p:
            target[ord(letter)-ord('a')] += 1
            
        count = [0]*26
        left = right = 0
        ret = []
        while right < len(s):
            count[ord(s[right])-ord('a')] += 1
            if right-left == len(p):
                count[ord(s[left])-ord('a')] -= 1
                left += 1
            if count == target:
                ret.append(left)
            right += 1
            
        return ret