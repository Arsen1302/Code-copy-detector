class Solution(object):
    def solution_53_1_1(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        def solution_53_1_2(i):
            if i == len(s):
                return [""]
            ans = []
            for j in range(i+1, len(s)+1):
                if s[i:j] in wordDict:
                    for tail in solution_53_1_2(j):
                        if tail != '':
                            ans.append(s[i:j] + " " + tail) 
                        else:
                            ans.append(s[i:j])
            return ans
        return solution_53_1_2(0)