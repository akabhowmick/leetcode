// # https://leetcode.com/problems/running-sum-of-1d-array/
// # difficulty: easy
// # tags: prefix
// # problem
// # Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).

#include <vector>    // Include the vector header
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