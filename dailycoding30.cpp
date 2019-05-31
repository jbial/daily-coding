#include <iostream>
#include <vector>
#include <cmath>
#include <map>

using std::map;
using std::min;
using std::max;
using std::cout;
using std::endl;
using std::vector;

/* 
 * For every position, find the max wall on the left and right sides
 * and add the minimum of those walls minus the current height to 
 * the result. 
 *
 * runs in O(n^2) time, constant space
 */
int trap_brute_force(vector<int>& walls, int size, int ans) {
  for (int i = 1; i < size - 1; i++) {
    int left_max = 0, right_max = 0;
    for (int j = i; j < size; j++) {
      right_max = max(right_max, walls[j]);
    }
    for (int j = i; j >= 0; j--) {
      left_max = max(left_max, walls[j]);
    }
    ans += min(left_max, right_max) - walls[i];
  }
  return ans;
}


/*
 * Extend the brute force approach by storing the maxes at 
 * every index. Build up left and right max vectors and update
 * answer the same way as in the brute force approach.
 *
 * runs in O(n) time, O(n) space
 */
int trap_dp(vector<int>& walls, int size, int ans) {
  vector<int> left_max(size, walls[0]);
  for (int i = 1; i < size; i++) {
    left_max[i] = max(left_max[i - 1], walls[i]);
  }
  vector<int> right_max(size, walls[size - 1]);
  for (int i = size - 2; i >= 0; i--) {
    right_max[i] = max(right_max[i + 1], walls[i]);
  } 
  for (int i = 1; i < size - 1; i++) {
    ans += min(left_max[i], right_max[i]) - walls[i];
  }
  return ans;
}


/*
 * Extend the DP approach by using two ptrs to find the left
 * and right maxes. Iterate from one side until the wall for
 * that side is larger than the opposite side wall, at which
 * point start iterating the ptr from the other side. 
 * 
 * runs in O(n) time, constant space
 */
int trap_two_ptrs(vector<int>& walls, int size, int ans) {
  int left = 0, right = size - 1;
  int right_max = 0, left_max = 0;
  while (left < right) {
    if (walls[left] < walls[right]) {
      if (walls[left] >= left_max) left_max = walls[left];
      else ans += left_max - walls[left];
      left++;
    } else {
      if (walls[right] >= right_max) right_max = walls[right];
      else ans += right_max - walls[right];
      right--;
    }
  }
  return ans; 
}


int trap(vector<int>& walls) {
  return trap_two_ptrs(walls, walls.size(), 0);
}


bool run_tests(map<int, vector<int>> tests) {
  bool passed = true;
  for (map<int, vector<int>>::iterator it = tests.begin(); it!=tests.end(); it++){ 
    passed &= (trap(it->second) == it->first);
  }
  return passed;
}


int main() {
  
  map<int, vector<int>> tests;
  vector<int> test1{0, 5, 0, 1, 0, 0, 2, 3, 0, 1};
  tests[13] = test1;
  vector<int> test2{2, 1, 2};
  tests[1] = test2;
  vector<int> test3{3, 0, 1, 3, 0, 5};
  tests[8] = test3;
  vector<int> test4{1, 2, 3, 4};
  tests[0] = test4;
  vector<int> test5{4, 0, 1, 5, 4, 3, 2, 0, 1, 2};
  tests[10] = test5;

  if (run_tests(tests)) {
    cout << "Passed" << endl;
  } else {
    cout << "Failed" << endl;
  }

  return 0;
}
