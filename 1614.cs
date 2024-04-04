public class Solution {
    public int MaxDepth(string s) {
        int count = 0, maxAns = 0;
        foreach (char i in s){
            if (i == '(') maxAns = Math.Max(maxAns, ++count);
            if (i == ')') count--;
        }
        return maxAns;
    }
}