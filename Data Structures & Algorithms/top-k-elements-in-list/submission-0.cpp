class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int, int> map;
        for (int &i: nums) map[i]++;

        int n = nums.size();
        vector<vector<int>> freq(n + 1);

        for (auto &pair: map){
            freq[pair.second].push_back(pair.first);
        }

        vector<int> result;
        for (int i = freq.size() - 1; i > 0; i--){
            for (int element: freq[i]){
                result.push_back(element);
                if (result.size() == k) return result;
            }
        }
        return result;
    }
};
