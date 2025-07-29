class Solution:
    def solution_1510_4(self, s: str) -> List[str]:
        return [f"{chr(i)}{j}" for i in range(ord(s[0]), ord(s[3])+1) for j in range(int(s[1]), int(s[4])+1)]