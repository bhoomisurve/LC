class Solution {
public:
    string makeLargestSpecial(string s) {
        vector<string> units;
        int bal = 0;
        int start = 0;

        for (int i = 0; i < s.size(); i++){
            if (s[i] == '1') bal++;
            else bal--;

            if (bal == 0){
                string inner = s.substr(start + 1, i - start - 1);

                string Opinner = makeLargestSpecial(inner);

                units.push_back("1" + Opinner + "0");

                start = i + 1;
            }
        }

        sort(units.begin(), units.end(), greater<string>());

        string res;
        for (auto &b : units) res += b;
        return res;
    }
};