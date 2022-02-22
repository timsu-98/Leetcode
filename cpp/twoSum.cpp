#include <vector>
#include <string>
#include <unordered_map>
#include <map>

using namespace std;

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> residual {};
        for (int i=0; i<nums.size(); i++) {
            if (residual.find(nums[i]) != residual.end()) {
                return vector<int>{residual[nums[i]], i};
            }
            residual.insert({target - nums[i], i});
        }
        return vector<int> {};

        /* -------------------- SOLUTION ------------------ */
        // map<int, int> mp;
        
        // for(int i=0; i<nums.size(); i++)
        // {
        //     int temp = target - nums[i];
        //     if(mp.count(temp))
        //     {
        //         return vector<int>{mp[temp], i};
        //     }
        //     mp.insert({nums[i], i});
        // }
        // return vector<int>{};
    }
};