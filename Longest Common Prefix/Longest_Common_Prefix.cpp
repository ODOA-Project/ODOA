#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        if (strs.size() == 1) return strs[0];

        char* buf1 = new char[strs[0].size() + 1];
        memcpy(buf1, strs[0].c_str(), strs[0].size() + 1);
        int size = strs[0].size();

        for (int idx = 1; idx < strs.size(); idx++)
        {
            char* buf2 = new char[strs[idx].size() + 1];
            memcpy(buf2, strs[idx].c_str(), strs[idx].size() + 1);
            
            for (int p = 0; p < size; p++)
            {
                if (buf1[p] != buf2[p])
                {
                    size = p;
                    break;
                }
            }
            delete[] buf2;
        }
        delete[] buf1;
        
        return strs[0].substr(0, size);
    }
};

int main()
{
    Solution s;
    //vector<string> vec{ "flower", "flow", "flight" };
    vector<string> vec{"dog", "racecar", "car"};
    string str = s.longestCommonPrefix(vec);
    return 0;
}