#include <iostream>
#include <vector>
#include <map>
#include <algorithm>

using namespace std;

class Solution {
public:
    bool isPalindrome(int x) {
        bool ret = false;
        vector<int> vec;
        int num = x;
        double reverse = 0;
        if (x >= 10)
        {
            while (num >= 10)
            {
                vec.push_back(num % 10);
                num = num / 10;
                if (num < 10)
                    vec.push_back(num);
            }

            int p = vec.size();
            for (int i = 0; i < vec.size(); i++)
            {
                reverse += (vec[i] * pow(10, p - 1));
                if (reverse > INT_MAX) return false;
                p--;
            }
        }

        if ((x > 0 and x < 10) || reverse == x)
            ret = true;

        return ret;
    }
};

int main()
{
    Solution s;
    bool b = s.isPalindrome(1234567899);
    return 0;
}