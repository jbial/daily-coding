/*
 * This problem was asked by Google.
 *
 * Given an array of integers where every integer occurs
 * three times except for one integer, which only occurs once,
 * find and return the non-duplicated integer.
 * 
 * solution:
 * Use bit tricks. For each bit in an assumed 32 bit integer array, check each
 * element in the array and sum the aligning bits in the ith position. If 
 * that sum is not modulo 3, then we know that the ith bit belongs to the 
 * duplicated element, and add (or) the bit to the result.
 *
 * Runs in O(n) time since we assume a constant 32 bits/int, constant space.
 */
#include <iostream>
#include <vector>
#include <map>

#define INT_SIZE 32

using std::map;
using std::cout;
using std::endl;
using std::vector;


int find_duplicate(vector<int> nums) {
  int result = 0, sum, x;
  for (int i = 0; i < INT_SIZE; i++) {
    // get the ith position bit
    x = 1 << i; sum = 0;
    for (int j = 0; j < nums.size(); j++) {
      // sum all the aligning bits
      if (nums[j] & x) 
        sum += 1;
    }
    // if the sum is not modulo three, then the ith bit belongs to the duplicate
    if (sum % 3) 
      result |= x;
  }
  return result;
}


bool run_tests(map<int, vector<int>> tests) {
  map<int, vector<int>>::iterator it;
  bool result = true;
  for (it = tests.begin(); it != tests.end(); it++) {
    result &= (find_duplicate(it->second) == it->first);
  }
  return result;
}


int main() {
  
  map<int, vector<int>> tests;
  vector<int> t1{1,2,3,4,1,2,3,1,2,3};
  tests[4] = t1;

  vector<int> t2{4,2,1,1,2,4,2,4,1,3};
  tests[3] = t2;

  vector<int> t3{1,3,3,3};
  tests[1] = t3;

  vector<int> t4{0,0,0,5,6,5,5};
  tests[6] = t4;
  
  if (run_tests(tests))
    cout << "Passed" << endl;
  else
    cout << "Failed" << endl;

  return 0;
}
