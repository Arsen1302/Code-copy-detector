class Solution:
    def solution_1133_5(self, command: str) -> str:
        command=command.replace("()","o")
        command=command.replace("(al)","al")
        return command