class Solution:
    def solution_1133_1(self, command: str) -> str:
        return command.replace('()','o').replace('(al)','al')