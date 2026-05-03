#include <algorithm>

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        std::unordered_set<int> numbers;

        for (int num: nums){
            if (numbers.count(target - num)){
                vector<int> Myvector;
                
                auto it1 = std::find(nums.begin(), nums.end(), num);
                int index1 = it1 - nums.begin();
                auto it2 = std::find(nums.begin(), nums.end(), target - num);
                int index2 = it2 - nums.begin();
                
                if (index1 > index2) {
                    Myvector = {index2, index1};
                } 
                else if (index1 == index2) {
                    auto it3 = std::find(++it2, nums.end(), target - num);
                    int index3 = it3 - nums.begin();
                    Myvector = {index2, index3};
                }
                else {
                    Myvector = {index1, index2};
                }
                return Myvector;
            }
            numbers.insert(num);
        }
        
    }
};
