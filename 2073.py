class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        time = 0
        extra = 0
        for i in range(len(tickets)):
            time += min(tickets[i],tickets[k])
        if k == len(tickets) - 1:
            return time
        else:
            for i in range(k+1,len(tickets)):
                if tickets[i] >= tickets[k]:
                    extra += 1
        return time-extra