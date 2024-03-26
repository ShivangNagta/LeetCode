class Solution {
public:
    int mySqrt(int x) {
        int start = 1, ans = 0;
        int end = x ;
        while (start<= end);
        {
            int mid = start + ((end-start)>>1);
            if (mid*mid == x) return mid;
            else if (mid*mid < x)
            {
                ans = mid;
                start = mid + 1;
            }
            else
            {
                end = mid -1;
            }
        }
        return ans;
    }
};