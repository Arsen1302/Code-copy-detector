class Solution:
    def solution_1515_2(self, n: int, artifacts: List[List[int]], dig: List[List[int]]) -> int:
        pos_to_artifacts = {} # (x, y) => artifact unique index
        artifacts_to_remaining = {} # artifact unique index to remaining spots for artifact to dig up
        results = 0
        
		# Each artifact is identified by a unique index.
        for id, artifact in enumerate(artifacts):
            start, end = (artifact[0], artifact[1]), (artifact[2], artifact[3])
            size = 0
            for x in range(start[0], end[0] + 1):
                for y in range(start[1], end[1] + 1):
                    pos_to_artifacts[(x, y)] = id
                    size += 1
            artifacts_to_remaining[id] = size
        
        for pos in dig:
            if tuple(pos) not in pos_to_artifacts:
                continue
            id = pos_to_artifacts[tuple(pos)]
            artifacts_to_remaining[id] = artifacts_to_remaining[id] - 1
            if artifacts_to_remaining[id] == 0:
                results += 1

        return results