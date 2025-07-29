class Solution:
    def solution_1720_4_1(self, root: Optional[TreeNode]) -> int:
        return sum([self.solution_1720_4_3(level) for level in self.solution_1720_4_2(root)])

    def solution_1720_4_2(self, root: Optional[TreeNode]) -> list[list[int]]:
        nodes, levels, index = [root], [0], 0

        while index != len(nodes):
            for child in nodes[index].left, nodes[index].right:
                if child:
                    nodes.append(child)
                    levels.append(levels[index] + 1)
            index += 1

        values = [[] for _ in range(levels[-1] + 1)]
        for index in range(len(nodes)):
            values[levels[index]].append(nodes[index].val)

        return values

    def solution_1720_4_3(self, array: list[int]) -> int:
        sorted_indexes = sorted(range(len(array)), key=array.__getitem__)
        return len(array) - sum(self.solution_1720_4_4(sorted_indexes, index) for index in range(len(array)))

    def solution_1720_4_4(self, sorted_indexes: list[int], index: int) -> bool:
        had_cycle = False
        while sorted_indexes[index] != -1:
            sorted_indexes[index], next_index = -1, sorted_indexes[index]
            index, had_cycle = next_index, True
        return had_cycle