class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& temperatures) {
        vector<int> Myvector;

        for (int i {0}; i < temperatures.size(); i++){
            vector<int> stack = {};
            bool found = false; 
            for (int j {i + 1}; j < temperatures.size(); j++){
                stack.push_back(temperatures[j]);
                if (temperatures[j] > temperatures[i]) {
                    Myvector.push_back(stack.size());
                    found = true;
                    break;
                }
            }
            if (!found) {
                Myvector.push_back(0);
            }
        }
        return Myvector;
    }
};
