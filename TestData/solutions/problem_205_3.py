class Solution:
    def solution_205_3(self, s):
        # In python, List can be used as stack(by using pop()) and queue(by using pop(0))
        result = []
        for curr_char in s:
            if curr_char == "]":
                # Step2-1 : Find the (1)subStr and remove "[" in the stack
                sub_str = []
                while result[-1] != "[":
                    sub_str.append(result.pop())
                sub_str = "".join(sub_str[::-1])

                # Step2-2 : Find the (2)k and remove k in the stack
                result.pop()
                k = []
                while len(result) > 0 and result[-1] <= "9":
                    k.append(result.pop())
                k = int("".join(k[::-1]))

                # Step2-3 : Repeat sub_str k times after stack
                result += k*sub_str

            else:
                # Step1 : Put the char into the stack, except "]"
                result.append(curr_char)
        return "".join(result)