#include <iostream>
#include <queue>
#include <vector>
#include <functional>

using std::vector;
using std::greater;
using std::priority_queue;
using std::cout;
using std::endl;

/*
 * This problem was asked by Microsoft.
 *
 * Compute the running median of a sequence of numbers. 
 * That is, given a stream of numbers, print out the median 
 * of the list so far on each new element.
 *
 *
 * Solution: Use two heaps, one max heap and one min heap
 *
 * We know that we find the median using the middle number or middle
 * two numbers, so using the max heap we store the left middle num
 * and using the min heap we store the right middle num. We prioritize adding
 * to the max heap over the min heap but the solution would also work vice versa.
 * Whenever the max heap contains more elements, offer the max to the min heap,
 * and if the min heap contains more elements than the max heap, offer the min.
 *
 * After balancing the heaps, if the max heap ends up with one more element
 * than the min heap, the top is the median and we are done. If the heaps are
 * perfectly balanced (equal in size), then the median is the average of the
 * two tops.
 *
 * */
class RunningMedian {
  
  // min and max heaps
  priority_queue<int> lo;
  priority_queue<int, vector<int>, greater<int>> hi;

  public:

  // pushes next datastream element onto heaps
  void add_num(int k) {

    lo.push(k);   // always push to max heap first
    hi.push(lo.top());
    lo.pop();   // balance the heaps

    if (lo.size() < hi.size()) {  // makes sure that lo has the most elements only
      lo.push(hi.top());
      hi.pop();
    }
  }

  // finds the running median
  double find_median() {
    return (lo.size() > hi.size())? (double)lo.top() : (lo.top() + hi.top()) * 0.5;
  }

  // solve the problem
  template<typename T, size_t N>
  void run(T (&a)[N]) {
    cout << "Running medians of: [ ";
    for (int i = 0; i < N; i++) {
      cout << a[i] << " ";
    }
    cout << "]" << endl;

    for (int i = 0; i < N; i++) {
      add_num(a[i]);
      cout << find_median() << endl;
    }
  }
};


int main() {

  int test[6] = {41, 35, 62, 5, 97, 108};
  RunningMedian solution;
  solution.run(test);

  return 0;
}
