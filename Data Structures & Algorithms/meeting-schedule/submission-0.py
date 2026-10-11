"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        #intervals.sort()
        tab = []
        counter = 0
        #(intervals[0].start)
        for meet in intervals:
            tab.append((meet.start,1))
            tab.append((meet.end,-1))
        tab.sort()
        for i in range(len(tab)):
            counter += tab[i][1]
            if counter > 1:
                return False
        return True 
