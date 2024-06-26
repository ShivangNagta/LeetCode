class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        sortedScore = sorted(score, reverse = True)
        medals = ["Gold Medal", "Silver Medal", "Bronze Medal"]
        ranks = {score : medals[i] if i < 3 else str(i+1) for i, score in enumerate(sortedScore)}
        return [ranks[score] for score in score]