class Solution:
    def solution_499_4(self, cpdomains: List[str]) -> List[str]:
        result = []
        store = dict()
        for combination in cpdomains:
            spaceIndex = combination.index(" ")
            visitTime = int(combination[:spaceIndex])
            fullDomain = combination[spaceIndex + 1:]
            string = ""
            for i in reversed(range(-1, len(fullDomain))):
                if fullDomain[i] == "." or i == -1:
                    if string not in store:
                        store[string] = visitTime
                    else:
                        store[string] += visitTime
                if i == -1:
                    break
                string = fullDomain[i] + string

        for domain, time in store.items():
            result.append(f"{time} {domain}")

        return result