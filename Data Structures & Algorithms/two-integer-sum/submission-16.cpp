class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        std::unordered_map<int, int> counter;
        std::vector<int> result;

        for (size_t i {}; i < nums.size(); ++i) {
            if (counter.find(target - nums[i]) != counter.end()) {
                result.push_back(counter[target - nums[i]]);
                result.push_back(i);
                return result;
            }
            else {
                counter[nums[i]] = i;
            }
        }
    }
};
