"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        def isOverlap(a, b):
            return max(a.start,b.start) < min(a.end, b.end) 
        if not intervals:
            return True
        intervals.sort(key=lambda x: x.start)
        prev = intervals[0]
        for interval in intervals[1:]:
            if isOverlap(prev, interval):
                return False
            prev = interval
        return True
