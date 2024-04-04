class Solution {
public:
    int maxDepth(string s) {
        int count = 0, maxAns = 0;
        for (char i : s)
        {
            if (i == '(')
            {
                count ++;
                if (count > maxAns) maxAns ++;
            }
            if (i == ')') count--;
        }
        return maxAns;
    }
};