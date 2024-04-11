class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort()
        result = [0] * len(deck)
        idx = list(range(len(deck)))
        
        for card in deck:
            poppedIdx = idx.pop(0)  
            result[poppedIdx] = card   
            if idx:               
                idx.append(idx.pop(0))  
        
        return result