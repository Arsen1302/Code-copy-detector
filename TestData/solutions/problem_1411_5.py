class Solution:
    def solution_1411_5(self, word: str) -> int:
        result = 0
        vowels = 'aeiou'
        # dictionary to record counts of each char
        mp = defaultdict(lambda: 0)

        for i, char in enumerate(word):
            # if the current letter is a vowel
            if char in vowels:
                mp[char] += 1
                # if the previous letter is not a vowel, set the current point to a left point and a pivot
                if i == 0 or word[i-1] not in vowels:
                    left = pivot = i
                # if all five vowels are founded,
                # try to calculate how many substrings that contain all five vowels using sliding window
                # window range is between the left point and the current i point
				# move the pivot to the right-side one by one, check if [pivot, i] contains all five vowels
                while len(mp) == 5 and all(mp.values()):
                    mp[word[pivot]] -= 1
                    pivot += 1
                result += (pivot - left)
            else:
                mp.clear()
                left = pivot = i+1
        
        return result