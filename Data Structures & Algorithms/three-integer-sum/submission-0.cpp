#include<algorithm>
class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        vector<vector<int>> Myvector;

        for (int i {0}; i < nums.size(); i++){
            if ( i > 0 && nums[i] == nums[i-1]) continue;

            int *left_pointer = &nums[0] + i + 1;
            int *right_pointer = &nums[0] + nums.size() - 1;
            while (left_pointer < right_pointer) {
                int sum = nums[i] + *left_pointer + *right_pointer;

                if (sum > 0) {
                    right_pointer--;
                } else if (sum < 0) {
                    left_pointer++;
                } else {
                    Myvector.push_back({nums[i], *left_pointer, *right_pointer});

                    left_pointer++;
                    right_pointer--;

                    while (left_pointer < right_pointer && *left_pointer == *(left_pointer - 1)) {
                        left_pointer++;
                    }
                    while (left_pointer < right_pointer && *right_pointer == *(right_pointer + 1)) {
                        right_pointer--;
                    }
                }
            }
        }
        return Myvector;
    }
};
