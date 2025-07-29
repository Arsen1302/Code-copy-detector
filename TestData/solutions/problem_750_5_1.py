class Solution:
    def solution_750_5_1(self, books, shelfWidth):
        @lru_cache(None)
        def solution_750_5_2(idx,cur_height,cur_width):
            if cur_width < 0:
                return float("inf")

            if idx == len(books):
                return cur_height

            thickness, height = books[idx]
            same_shelf = solution_750_5_2(idx+1,max(height,cur_height),cur_width-thickness)
            change_shelf = cur_height + solution_750_5_2(idx+1,height,shelfWidth-thickness)

            return min(same_shelf,change_shelf)

        return solution_750_5_2(0,0,shelfWidth)