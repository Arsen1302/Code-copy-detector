class Solution:
    def solution_1133_3(self, command: str) -> str:
        for key, val in {"()":"o", "(al)":"al" }.items():
            command = command.replace(key, val)
        return command