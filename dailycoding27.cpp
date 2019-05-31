#include <iostream>
#include <stack>
#include <string>
#include <map>

using std::map;
using std::cout;
using std::endl;
using std::string;
using std::stack;


map<char, char> getParenMap() {
  map<char, char> m;
  m[')'] = '(';
  m[']'] = '[';
  m['}'] = '{';
  return m;
}


bool validate(string str) {

  // initialize the stack to hold left facing parentheses
  stack<char> parenStack;
  map<char, char> parenMap = getParenMap();

  // base case: initially invalid
  if (parenMap.find(str[0]) != parenMap.end()) return false;
    
  /* 
  loop through the string and check if each char is in the map
    1) if so, check if it matches the top of the stack
    2) otherwise, add it to the stack 
  */
  for (char i: str) {
    if (parenMap.find(i) == parenMap.end()) {
      parenStack.push(i);  
    } else if (parenStack.top() == parenMap[i]) {
      parenStack.pop();
    } else {
      return false;
    }
  }

  // the string was valid if the stack ends up empty
  return parenStack.empty();
}


int main() {

  string tests[6] = {"([])[]({})", "([)]", "]{[()]}}", "[][]", "[(})]", "[{}](()"};
  int results[6] = {1, 0, 0, 1, 0, 0};
  
  bool test_result = true;
  for (int i = 0; i < 6; i++) {
    test_result &= (validate(tests[i]) == results[i]);
  }

  if (test_result) cout << "Passed" << endl;
  else cout << "Failed" << endl;

  return 0;
}
