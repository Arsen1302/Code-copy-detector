class Solution:
    def solution_199_5(self, input: str) -> int:
        """
        We split string by \n and than check the level of each subdirectory/file.
        If level bigger than previus one we add to the stack tuple with it( cur_level, directory(file_name) ), else pop from it.
        Before pop we check if the current stack values contains filepath and compare with longest value.
        We put tuple (level_size, path_name) in the stack on each iteration.
        """
        s = []
        longest = 0
        for dir in input.split("\n"):
            cur_level = dir.count('\t')
            while s and s[-1][0] >= cur_level:
                #Before pop element check if this a file path
                if '.' in s[-1][1]:
                    longest = max(longest, len("/".join([dir_file_name for _, dir_file_name in s])))
                s.pop()
            s.append((cur_level, dir.replace('\t',''))) #(level_size, path_name)
        if s and '.' in s[-1][1]:
            longest = max(longest, len("/".join([dir_file_name for _, dir_file_name in s])))
        return longest