#include <iostream>
#include <map>
#include <string>

using std::string;
using std::map;
using std::cout;
using std::endl;

/*
 * This problem was asked by Google.
 *
 * Given an array of strictly the characters 'R', 'G', and 'B', 
 * segregate the values of the array so that all the Rs come first, 
 * the Gs come second, and the Bs come last. You can only 
 * swap elements of the array.
 *
 * Solution:
 * Use a two pointer approach and sort the array by letter. Start left 
 * pointer from the given starting index and the right pointer at the end.
 * When the left ptr encounters the given letter key, advance, and when the
 * right ptr encounters the key, swap the left and right elements. First,
 * sort by key 'R', then sort by key 'G' starting at where the left ptr 
 * left-off from sorting 'R'. Then it must be that the array is sorted.
 *
 * runs in O(n) time, constant space
 *
 */
class SortRGB {

  public:

  string colors;

  void swap(int i, int j) {
    char temp = colors[i];
    colors[i] = colors[j];
    colors[j] = temp;
  }

  int sort_by_letter(int start, char letter) {
    int l = start, r = colors.length() - 1, last = 0;
    while (l < r) {
      if (colors[l] == letter) {
        l++;
      } else if (colors[r] != letter) {
        r--;
      } else {
         swap(l, r);
      }
    }
    return l;
  }

  void sort() {
    int next = sort_by_letter(0, 'R');
    sort_by_letter(next, 'G');
  }

};


void printList(string colors) {
  cout << "[ ";
  for (int i = 0; i < colors.length(); i++) {
    cout << colors[i] << " ";
  }
  cout << "]" << endl;
}


bool testHandle(map<string, string> tests) {
  bool results = true;
  SortRGB sol;
  map<string, string>::iterator it;
  for (it = tests.begin(); it != tests.end(); it++) {
    sol.colors = it->first;
    sol.sort();
    results &= (sol.colors == it->second);
  }
  return results;
}


int main() {

  map<string, string> tests;
  tests["GR"] = "RG";
  tests["GBR"] = "RGB";
  tests["BGR"] = "RGB";
  tests["GBRRBRG"] = "RRRGGBB";
  tests["BGRBGRBGR"] = "RRRGGGBBB";
  
  if (testHandle(tests)) 
    cout << "Passed" << endl;
  else
    cout << "Failed" << endl;

  return 0;
}
