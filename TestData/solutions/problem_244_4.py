class Solution:
    def solution_244_4(self, chars):
        if len(chars) < 2: return len(chars)
        outputs, last_char, count = [chars[0]], chars[0], 1

        for char in chars[1:]:
            if last_char == char: count += 1
            else:
                if count > 1: outputs.append(str(count))
                outputs.append(char)
                count = 1
            last_char = char

        if count > 1: outputs.append(str(count))

        out = list(''.join(outputs))
        for i in range(len(out)): chars[i] = out[i]

        return len(out)