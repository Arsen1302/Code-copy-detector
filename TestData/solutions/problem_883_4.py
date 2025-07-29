class Solution:
    def solution_883_4(self, diff: List[int], d: int) -> int:
        n = len(diff)
        if n < d:
            return -1

        today = [None] * n
        yesterday = [diff[0]] + [None] * (n - 1)
        # Solution for day 0 is just the running maximum
        for i in range(1, n):
            yesterday[i] = max(yesterday[i - 1], diff[i])
        
        for day in range(1, d):
            # stack contains all index i where today[i] has a solution with diff[i]
            # as the biggest
            stack = []
            for i in range(day, n):
                today[i] = yesterday[i - 1] + diff[i]
                # Each iteration of the while loop we either add or remove an item.
                # Since each job is added and/or removed at most once for each day, 
                # the time complexity is still O(d*n)
                while stack:
                    # If the last job in the stack is less difficult than job i
                    # then we can have the option to add job j+1 -> i to today[i]
                    # Because solution at today[j] has diff[j] as the biggest, 
                    # so after add job j+1 -> i, the new biggest is diff[i], 
                    # thus the total diff is inceaseed by (diff[i] + diff[j])
                    if diff[stack[-1]] < diff[i]:
                        j = stack.pop()
                        today[i] = min(today[i], today[j] - diff[j] + diff[i])
                    else:
                        # If we find a better solution at job i 
                        # then in this solution diff[i] is the biggest.
                        # add it to the stack
                        if today[i] < today[stack[-1]]:
                            stack.append(i)
                        # else job i is a part of the solution at today[stack[-1]]
                        else:
                            today[i] = today[stack[-1]]
                        break
                else:
                    # If stack is empty then of course we have a new solution at job i
                    stack.append(i)

            yesterday = today.copy()
        
        return yesterday[-1]