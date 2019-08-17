#include <iostream>
#include <string>
#include <map>
#include <algorithm>

using std::map;
using std::cout;
using std::endl;
using std::string;


string runLengthEncode(string str) {

  int i, j, count;
  string result = "";
  i = j = count = 0;

  if (str == "") return "";

  // use two pointers for keeping count to create the encoding
  while (j < str.length()) {
    if (str[i] == str[j]) {
      j++;
      count++;
    } else {
       result += (std::to_string(count) + str[i]);
       count = 0;
       i = j;
    }
  }
  return result + (std::to_string(count) + str[i]);
}


bool testHandle() {

  map<string, string> tests;
  tests["AAAABBBCCDAA"] = "4A3B2C1D2A";
  tests["AAAAAAAA"] = "8A";
  tests["abcdef"] = "1a1b1c1d1e1f";

  for (auto const& pair: tests) {
    if (runLengthEncode(pair.first) != pair.second) return false;
  }
  return true;
}


int main() {
  
  if (testHandle()) cout << "Passed" << endl;
  else cout << "Failed" << endl;
  
  return 0;
}
