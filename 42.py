class Solution:
    def trap(self, height: List[int]) -> int:
        leftArray = []
        rightArray = []
        leftMax, rightMax = 0,0
        for i in range(len(height)):
            if height[i] > leftMax:
                leftArray.append(height[i])
                leftMax = height[i]
            else:
                leftArray.append(leftMax)
        for i in range(len(height)):
            if height[len(height)-i-1] > rightMax:
                rightArray.append(height[len(height)-i-1])
                rightMax = height[len(height)-i-1]
            else:
                rightArray.append(rightMax)
        rightArray.reverse()
        ans = 0
        for i in range(len(height)):
            ans+= min(leftArray[i], rightArray[i]) - height[i]

        return ans
        