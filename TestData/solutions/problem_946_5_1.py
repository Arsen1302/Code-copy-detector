class Solution:
    def solution_946_5_1(self, n: int, k: int) -> str:
        answer = []
        alphabets = ['a','b','c']
        def solution_946_5_2(alphabets,n,s):
            if len(s) == n:
                answer.append(s)
                return
            for x in alphabets:
                if s and s[-1] == x:
                    continue
                solution_946_5_2(alphabets,n,s + x)
        solution_946_5_2(alphabets,n,"")
        if k > 3 * ( 2 ** ( n - 1)):
            return ""
        return answer[k - 1]