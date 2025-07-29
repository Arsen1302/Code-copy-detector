class Solution:
    def solution_811_4(self, folder: List[str]) -> List[str]:
		# Sort, will guarantee the "/a" will comes before "/a/b" and they appear in sequence
        folder.sort()
        res = []
        res.append(folder[0])
        for i in range(1, len(folder)):
            # Append "/" to the previous is for the case: ["/a/b/c","/a/b/ca"]
            if folder[i].startswith(res[-1] + "/"):
                continue
            res.append(folder[i])
        return res