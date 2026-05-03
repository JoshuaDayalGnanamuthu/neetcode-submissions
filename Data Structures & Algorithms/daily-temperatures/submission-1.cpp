class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& temperatures) {
        vector<int> Myvector (temperatures.size(), 0);
        stack <pair<int, int>> stack1;

        for (int i {0}; i < temperatures.size(); i++){
            int temp = temperatures[i];
            while (!stack1.empty() && temp > stack1.top().first ){
                auto pair = stack1.top();
                Myvector[pair.second] = i - pair.second;
                stack1.pop();
            }
            stack1.push({temp, i});
        }
        return Myvector;
    }
};
