class Solution:
    def solution_647_1(self, wordlist: List[str], queries: List[str]) -> List[str]:
        
        # Convert words and vowels to sets for O(1) lookup times
        words = set(wordlist)
        vowels = set('aeiouAEIOU')
        
        # Create two maps.  
        # One for case insensitive word to all words that match "key" -> ["Key", "kEy", "KEY"]
        # The other for vowel insensitive words "k*t*" -> ["Kite", "kato", "KUTA"]
        case_insensitive = collections.defaultdict(list)            
        vowel_insensitive = collections.defaultdict(list)
        for word in wordlist:
            case_insensitive[word.lower()].append(word)
            key = ''.join(char.lower() if char not in vowels else '*' for char in word)
            vowel_insensitive[key].append(word)

        res = []
        for word in queries:

            # Case 1: When query exactly matches a word
            if word in words:
                res.append(word)
                continue

            # Case 2: When query matches a word up to capitalization
            low = word.lower()
            if low in case_insensitive:
                res.append(case_insensitive[low][0])
                continue

            # Case 3: When query matches a word up to vowel errors
            key = ''.join(char.lower() if char not in vowels else '*' for char in word)
            if key in vowel_insensitive:
                res.append(vowel_insensitive[key][0])
                continue

            res.append('')

        return res