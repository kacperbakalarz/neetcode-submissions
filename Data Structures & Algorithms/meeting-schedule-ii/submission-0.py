"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        #intervals.sort()
        tab = []
        counter = 0
        #(intervals[0].start)
        for meet in intervals:
            tab.append((meet.start,1))
            tab.append((meet.end,-1))
        tab.sort()
        ans = 0
        for i in range(len(tab)):
            counter += tab[i][1]
            ans = max(ans,counter)
        return ans