class Solution:
    def solution_244_5(self, chars):
        if len(chars) < 2: return len(chars)
        last_char, count, idx = chars[0], 1, 1

        for char in chars[1:]:
            if last_char == char: count += 1
            else:
                if count > 1:
                    chars[idx:idx+len(str(count))] = str(count)
                    idx += len(str(count))
                chars[idx], idx, count = char, idx + 1, 1
            last_char = char

        if count > 1:
            chars[idx:idx+len(str(count))] = str(count)
            idx += len(str(count))

        return idx