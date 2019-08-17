#include<iostream>
#include<map>
#include<array>

using std::cout;
using std::endl;

bool twoSum(int arr[], int size, int target) {
    if (!arr) return false;
    std::map<int,int> nums;
    for (int i = 0; i < size; i++) {
        if (nums.find(arr[i]) == nums.end()) {
            nums[target - arr[i]] = 1;
        } else {
            return true;
        }
    }
    return false;
}

int main() {

    // test case [1-4]
    int tc1_arr[4] = {10, 15, 3, 7};
    int tc1_target = 17;
    int tc2_arr[4] = {1,2,3,4};
    int tc2_target = 23;
    int tc3_arr[0];
    int tc3_target = 100;
    int tc4_arr[8] = {12,0,0,0,0,0,0,11};
    int tc4_target = 23;

    if (twoSum(tc1_arr, 4, tc1_target) &&
        !twoSum(tc2_arr, 4, tc2_target) &&
        !twoSum(tc3_arr, 0, tc3_target) &&
        twoSum(tc4_arr, 8, tc4_target))
        cout << "All test cases passed." << endl;
    else
        cout << "Failed" << endl;

    return 0;
}