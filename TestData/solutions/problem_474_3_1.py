class Solution:
    def solution_474_3_1(self, s: str) -> List[str]:
        return self.solution_474_3_2(s, "", [])

    def solution_474_3_2(self, s: str, current: str, solution:List[str]) -> List[str]:
        if len(s)==0:
            solution.append(current)
            return solution
        if s[0].isalpha():
            self.solution_474_3_2(s[1:], current+s[0].lower(), solution)
            self.solution_474_3_2(s[1:], current+s[0].upper(), solution)
        else:
            self.solution_474_3_2(s[1:], current+s[0], solution)
        return solution