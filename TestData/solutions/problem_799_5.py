class Solution(object):
    def solution_799_5(self, s, k):
        if k> len(s):
            return s
        i = 0
        while i <= len(s)-k:
            window = s[i:i+k]
            if(window.count(window[0]) == k):
                s = s[:i]+s[i+k:]
                i = 0
            else:
                i+=1
        return s