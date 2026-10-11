class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        sweep = []
        for i in range(len(intervals)):
            sweep.append((intervals[i][0],1))
            sweep.append((intervals[i][1],-1))
        sweep.sort(key = lambda x:(x[0], -x[1]))
        new = []
        new_start = 0 
        new_end = 0
        curr = 0
        #print(sweep)
        for i in range(len(sweep)):
            #print(curr)
            if curr + sweep[i][1] == 1 and curr == 0:
                new_start = sweep[i][0]

            if curr + sweep[i][1] == 0:
                new_end = sweep[i][0]
                new.append((new_start,new_end))

            curr += sweep[i][1]
            #print(new_start,new_end)
        return new
            