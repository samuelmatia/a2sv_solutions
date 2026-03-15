class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()

        merge = []

        for start, end in intervals:

            if not merge or start > merge[-1][1]:
                merge.append([start, end])
            else:
                merge[-1][1] = max(merge[-1][1], end)

        return merge
        
        