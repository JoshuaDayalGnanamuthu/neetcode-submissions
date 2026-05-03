class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int output {0};
        int min = prices[0];

        for (int &price: prices){
            if (price < min) min = price;
            else if (output < price - min) output = price - min;
        }
        return output;
    }
};