#include <iostream>
#include <utility>
#include <map>
#include <string>

using std::string;
using std::cout;
using std::endl;
using std::map;


/*
 * Helper to compute min of three numbers
 */
int min(int x, int y, int z) {
  return std::min(std::min(x, y), z);
}


/*
 * Find the minimum edit distance using dynamic programming
 * storing edit distances for every substring in a table and
 * building the table in a bottom up approach. Substitutions
 * cost 1 unit if the characters at the corresponding indices
 * are not equal.
 *
 * runs in O(m*n) time, O(m*n) space; m, n are the lengths of the strings
 */
int editDistance(string s1, string s2) {

  int m = s1.length(), n = s2.length();
  int tab[m + 1][n + 1];

  // build the distance table bottom up
  for (int i = 0; i <= m; i++) {
    for (int j = 0; j <= n; j++) {
      if (i == 0)
        tab[i][j] = j;
      else if (j == 0) 
        tab[i][j] = i;
      else 
        tab[i][j] = min(tab[i - 1][j] + 1,
                        tab[i][j - 1] + 1,
                        tab[i - 1][j - 1] + (s1[i-1] != s2[j-1]));
    }
  }
  return tab[m][n];
}


bool run_tests(map<int, std::pair<string, string>> tests) {
  bool result = true;
  for (std::pair<int, std::pair<string, string>> test: tests) {
    result &= (test.first == editDistance(test.second.first, test.second.second));
  }
  return result;
}


int main() {
 
  map<int, std::pair<string, string>> tests;
  tests[3] = std::make_pair("kitten", "sitting");
  tests[8] = std::make_pair("abcdefgh", "efghabcd");
  tests[1] = std::make_pair("price", "rice");
  tests[6] = std::make_pair("interleave", "ilnetaevre");
  tests[4] = std::make_pair("a", "abcde");

  if (run_tests(tests))
    cout << "Passed" << endl;
  else
    cout << "Failed" << endl;

  return 0;
}
