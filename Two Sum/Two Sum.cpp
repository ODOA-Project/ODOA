#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        vector<int> arr;
        bool b = false;

        for (int i = 0; i < nums.size() - 1; i++)
        {
            for (int j = 1; j <= nums.size() - 1; j++)
            {
                if (target == (nums[i] + nums[j]))
                {
                    arr.push_back(i);
                    arr.push_back(j);
                    b = true;
                    break;
                }
            }
            if (b)  break;
        }
        return arr;
    }
};

int main()
{
    vector<int> arr{ 1, 2, 3, 4, 5 };
    Solution s;
    vector<int> ret = s.twoSum(arr, 5);

    return 0;
}