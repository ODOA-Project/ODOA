#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        int count = 0;
        int len = nums.size();
        if (len == 0) return 0;
        
        for (int i = 0; i < len; i++)
        {
            if (nums[i] != val)
            {
                nums.push_back(nums[i]);
                count++;
            }
        }
        reverse(nums.begin(), nums.end());
        nums.resize(count);

        return count;
    }
};

int main()
{
    Solution s;
    vector<int> vec{ 0,1,2,2,3,0,4,2 };
    int k = s.removeElement(vec, 2);

    return 0;
}
