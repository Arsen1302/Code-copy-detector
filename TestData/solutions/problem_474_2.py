class Solution:
    def solution_474_2(self, S: str) -> List[str]:
        output = [""]
        for ch in S:
            for i in range(len(output)):
                if ch.isalpha():
                    output.append(output[i]+ch.lower())
                    output[i] = output[i]+ch.upper()
                else:
                    output[i] = output[i]+ch
        return output