class Solution:
    def solution_1133_4(self, command: str) -> str:
        return command.replace('()','o').replace('(al)','al')