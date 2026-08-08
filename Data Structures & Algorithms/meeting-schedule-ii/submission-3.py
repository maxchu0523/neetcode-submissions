"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:

        intervals.sort(key = lambda interval:interval.start)
        res = 0
        pq = []
        for interval in intervals:
            while pq and pq[0][0] <= interval.start:
                heapq.heappop(pq)
            heapq.heappush(pq, (interval.end, interval.start))
            res = max(res, len(pq))
        return res






