class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        return sum(map(lambda x: min(x,tickets[k]),tickets[:k])) + sum(map(lambda x: min(x,tickets[k]-1),tickets[k+1:])) + tickets[k]