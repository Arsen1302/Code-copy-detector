class Solution:
  def solution_960_4(self, paths: List[List[str]]) -> str:
    srcs = {src for src, _ in paths}
    dests = {dest for _, dest in paths} 
    return (dests - srcs).pop()