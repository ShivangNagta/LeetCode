class Solution {
public:
    bool checkValidString(string s) {
        int countAstrik = 0, countLeft = 0;
        vector<int> stackAstrik, stackleft;
        for (int i = 0; i < s.length(); i++) {
            char ch = s[i];
            if ((countAstrik == 0 && countLeft == 0) && ch == ')') {
                return false;
            } else if (ch == ')') {
                if (countLeft > 0) {
                    countLeft--;
                    stackleft.pop_back();
                } else {
                    countAstrik--;
                    stackAstrik.pop_back();
                }
            } else {
                if (ch == '(') {
                    ++countLeft;
                    stackleft.push_back(i);
                } else {
                    ++countAstrik;
                    stackAstrik.push_back(i);
                }
            }
        }
        while (!stackleft.empty()) {
            if (stackAstrik.empty()) {
                return false;
            } else if (stackleft.back() < stackAstrik.back()) {
                stackleft.pop_back();
                stackAstrik.pop_back();
            } else {
                return false;
            }
        }
        return true;        
    }
};