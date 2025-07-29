class Solution:
    def solution_504_2_1(self, s: str) -> List[str]:
        
        def solution_504_2_2(inputStr):
            # integer (no leading zeros or '0' itself)
            output = [inputStr] if inputStr[0] != '0' or inputStr == '0' else []
            # float
            for i in range(1, len(inputStr)):
                digit, decimal = inputStr[:i], inputStr[i:]
                # checking digit (left extra zeros)
                if len(digit) >= 2 and digit[0] == '0':
                    break
                # checking decimal (right extra zeros)
                if decimal[-1] == '0':
                    break
                output.append(f'{digit}.{decimal}')
            return output
        
        numStr = s[1:-1]
        output = []
        for i in range(1, len(numStr)):
            for x in solution_504_2_2(numStr[:i]):
                for y in solution_504_2_2(numStr[i:]):
                    output.append(f'({x}, {y})')

        return output