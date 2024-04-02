class Solution {
public:
    bool isIsomorphic(string s, string t) {
        vector<int> sIndex(200,0);
        vector<int> tIndex(200,0);

        int sLength = s.length();

        if (sLength != t.length()) return false;

        for ( int i = 0; i<sLength; i++){
            if (sIndex[s[i]] != tIndex[t[i]]) return false;
            sIndex[s[i]] = i+1;
            tIndex[t[i]] = i+1;
        }
        return true;
    }
};