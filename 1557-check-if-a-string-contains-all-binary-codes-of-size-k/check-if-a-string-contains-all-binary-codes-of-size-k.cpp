class Solution {
public:
    bool hasAllCodes(string s, int k) {
        int n = s.length();
        int tr = 1 << k;
        if (n < tr + k - 1){
            return false;
        }

        unordered_set<string> fc;
        for (int i = 0; i <= n - k; ++i){
            string sub = s.substr(i, k);
            
            fc.insert(sub);

            if (fc.size() == tr){
                return true;
            }
        }
        return fc.size() == tr;
    }
};