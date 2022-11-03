#include <iostream>
#include <vector>
#include <map>
#include <algorithm>
#include <set>

using namespace std;

class Solution {
public:
    int romanToInt(string s) {
        map<char, int> m{
            { 'I', 1 },
            { 'V', 5 },
            { 'X', 10 },
            { 'L', 50 },
            { 'C', 100 },
            { 'D', 500 },
            { 'M', 1000 }};

        if (s.size() == 1)
            return m[s.at(0)];

        int buf = m[s.at(s.size() - 1)];
        for (int i = s.size() -1; i > 0; i--)
        {
            if (m[s.at(i - 1)] < m[s.at(i)])
                buf -= m[s.at(i - 1)];
            else
                buf += m[s.at(i - 1)];
        }
        return buf;
    }
};

int main()
{
    Solution s;
    bool b = s.romanToInt("MCMXCIV");
    return 0;
}