class Solution {
public:
    string removeKdigits(string num, int k) {
        stack<char> stack;
        for (auto digit : num){
            while (!stack.empty() && stack.top() > digit && k > 0){
                k--;
                stack.pop();
            }
            stack.push(digit);
        }
        while (k > 0 && !stack.empty()){
            stack.pop();
            k--;
        }
        string stackString;
        while (!stack.empty()) {
            stackString += stack.top();
            stack.pop();
        }

        int endingIndex;
        for (int i= stackString.size() - 1; i>=0; i--){
            if (stackString[i] != '0'){
                endingIndex = i;
                break;
            }
        }

        stackString = stackString.substr(0, endingIndex+1);
        reverse(stackString.begin(), stackString.end());
        if (stackString.empty()) return "0";
        return stackString;
    }
};