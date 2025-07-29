class Solution:
    def solution_1703_5(self, queries: List[str], dictionary: List[str]) -> List[str]:
        # input: queries, dict
        # both have words with same length
        # e.g.: ["word", "note", "ants", "wood"]
        #       ["wood", "joke", "moat"]
        #   word -> wood: edit r -> o
        #   note -> joke: edit n -> j, t -> k
        #   ants -> ...: more than 2 edits
        #   wood -> wood: 0 edits
        # loop through both queries and dictionary
        # we have counters for number of different letters between 2 words
        # and because they all have the same length, counters should work for every comparison
        output = []

        # nested for loop
        for query in queries:
            for word in dictionary:
                i = 0
                counter = 0
                while i < len(word):
                    if counter > 2:
                        break
                    if query[i] != word[i]:
                        counter += 1
                    i += 1
                if counter > 2:
                    continue
                elif counter <= 2:
                    break
                    

            if counter <= 2:
                output.append(query)


        return output