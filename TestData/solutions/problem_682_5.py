class Solution:
    def solution_682_5(self, A: List[str]) -> List[str]:
        A.sort(key=lambda x: len(x))  # in-place sort by shortest to longest length
        letter_count = {letter: A[0].count(letter) for letter in A[0]}  # dict for shortest word: key = letter, value=count of letter 
        for letter in letter_count.keys():
            for word in A[1:]:  # No need to check A[0] as that is the reference point (i.e shortest word)
                tmp_count = word.count(letter)
                if tmp_count == 0:
					#  If letter not found in word, skip this letter 
                    letter_count[letter] = 0
                    break
                if tmp_count < letter_count[letter]:
                    letter_count[letter] = word.count(letter)

        return [letter for letter, count in letter_count.items() for _ in range(count)]