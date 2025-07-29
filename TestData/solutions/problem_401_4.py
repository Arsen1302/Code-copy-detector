class Solution:
    def solution_401_4(self, ops: List[str]) -> int:
        i = j = 0
        while j < len(ops):
            if ops[j] == "C":
                i -= 2
            elif ops[j] == "D":
                ops[i] = int(ops[i-1])*2
            elif ops[j] == "+":
                ops[i] = int(ops[i-1]) + int(ops[i-2])
            else:
                ops[i] = int(ops[j])
            i += 1
            j += 1
        return sum(ops[:i])