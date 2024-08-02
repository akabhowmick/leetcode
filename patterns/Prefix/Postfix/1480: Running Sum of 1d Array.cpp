#include <vector>  // Include the vector header
using namespace std; // Use the std namespace

class Solution
{
public:
    vector<int> runningSum(vector<int> &nums)
    {
        vector<int> arrayOfSums;
        int currentSum = 0;
        for (int i = 0; i < nums.size(); i++)
        {
            currentSum += nums[i];
            arrayOfSums.push_back(currentSum);
        }
        return arrayOfSums;
    }
};