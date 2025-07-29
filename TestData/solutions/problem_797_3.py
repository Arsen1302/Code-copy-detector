class Solution:
    def solution_797_3(self, arr) :
        dict  = {}
        for i in arr:
            dict[i] = arr.count(i)
        return len(dict.values()) == len(set(dict.values()))