class Solution {
public:
    int reverse(int x) {
        int ans=0, rem;
        while(x!=0){
            rem = x%10;
            x/=10;
            if(ans>INT_MAX/10 || ans<INT_MIN/10){
                return 0;
            }
            ans = rem+ans*10;
        }
        return ans;
        }
        
};