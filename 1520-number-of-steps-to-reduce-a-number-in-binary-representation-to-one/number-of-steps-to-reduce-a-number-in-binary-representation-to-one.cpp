class Solution {
public:
    int numSteps(string s) {
        int steps = 0;
        int carry = 0;

        int n = s.size();

        for (int i = n - 1; i > 0; --i){
            int digit = (s[i] - '0') + carry;
            if (digit == 1){
                steps += 2;
                carry = 1;
            }
            else {
                steps += 1;
                if (digit == 2){
                    carry = 1;
                }
            }
        }

        return steps + carry;
    }
};