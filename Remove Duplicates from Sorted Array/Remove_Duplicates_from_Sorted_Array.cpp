#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        int count = 1;
        int curValue = nums[nums.size() - 1];

        for (int i = nums.size() - 2; i >= 0; i--)
        {
            if (curValue > nums[i])
            {
                curValue = nums[i];
                nums.push_back(curValue);
                count++;
            }
        }
        reverse(nums.begin(), nums.end());

        return count;
    }
};

int main()
{
    Solution s;
    vector<int> vec{ 1, 1, 2,2,2,3,4,5,5,6 };
    //vector<int> vec{1, 1, 2};
    int k = s.removeDuplicates(vec);

    return 0;
}
