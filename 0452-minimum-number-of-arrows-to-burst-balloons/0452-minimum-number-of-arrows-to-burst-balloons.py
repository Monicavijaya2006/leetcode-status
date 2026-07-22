class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: x[1])
        prev_end = points[0][1]

        # number of non-overlapping intervals
        arrows = 1

        for i in range(1, len(points)):
            if prev_end < points[i][0]:
                arrows += 1
                prev_end = points[i][1]

        return arrows
        