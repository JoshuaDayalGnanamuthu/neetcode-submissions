class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        vector<int> Myvector;

        int prefix = 1;
        for (int i = 0; i < nums.size(); i++){
            Myvector.push_back(prefix);
            prefix *= nums[i];
        }

        int suffix = 1;
        for (int i = nums.size()-1; i >= 0 ; i--){
            Myvector[i] *= suffix;
            suffix *= nums[i];
        }

        return Myvector;


        
    }
};
