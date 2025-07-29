class Solution:
    def solution_521_5(self, s: str, indices: List[int], sources: List[str], targets: List[str]) -> str:

        res = ''

        hashMap = {} #current -> mapping

        #current string

        zip_map = list(zip(indices, sources, targets))

        for index, source_string, target in zip_map:
        
            if s[index : index + len(source_string)] == source_string:
                hashMap[index] = target  


        i = 0

        indices_to_sources = {}
        for ind, source_string in list(zip(indices, sources)):
            indices_to_sources[ind] = source_string

        while i < len(s):
            print(i, res)
            if i in hashMap:
                res += hashMap[i]
                i += len(indices_to_sources[i])
                

            else:
                res += s[i]
                i += 1

        return res