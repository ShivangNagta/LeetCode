class Solution {
public:
    int minOperations(vector<int>& nums, int k) {
        int count = 0;
        for (int bit = 0; bit <= 20; bit++){
            int xorVal = 0;
            for (auto i: nums){
                int bitVal = (1<<bit)&i;
                xorVal = xorVal ^ bitVal;
            }
            int kxorVal = ((1<<bit)&k);
            if (xorVal != kxorVal){
                count++;
            } 
        }
        return count;
    }
};