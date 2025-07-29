class Solution(object):
    def solution_474_1_1(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        def solution_474_1_2(sub="", i=0):
            if len(sub) == len(S):
                res.append(sub)
            else:
                if S[i].isalpha():
                    solution_474_1_2(sub + S[i].swapcase(), i + 1)
                solution_474_1_2(sub + S[i], i + 1)
                
        res = []
        solution_474_1_2()
        return res