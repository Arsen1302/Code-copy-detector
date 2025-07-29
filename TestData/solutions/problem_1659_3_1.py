class Solution:
    def solution_1659_3_1(self, s):  # finds difference of indices
        result = dict()
        for letter in set(s):
            indices = []
            for idx, value in enumerate(s):
                if value == letter:
                    indices.append(idx)
            result[letter] = indices[1] - indices[0] - 1
        return result  # dict like {'a':1, 'b':0}

    def solution_1659_3_2(self, s, distance) -> bool:
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        for key, value in self.solution_1659_3_1(s).items():
            if distance[alphabet.index(key)] != value:
                return False
        return True