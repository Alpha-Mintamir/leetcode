class Solution {
public:
    int trailingZeroes(int n) {
        int result = 0;
        while (n >= 5) {
            n /= 5;
            result += n;
        }
        return result;
    }
};
