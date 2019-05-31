#include <iostream>
#include <cmath>

using std::cout;
using std::endl;
using std::log;

/*
 * The currency exchange rate table can be represented as a complete
 * graph, with currencies as the nodes and exchange rates as the edges.
 * To detect arbitrage, we are interested in a cycle of exchanges that 
 * return a number greater than we started with e.g. a*b*c*d > 1. Take
 * the negative log of the exchange -> -(log(a) + log(b) + log(c)) < 0.
 * This problem then reduces to detecting a negative sum cycle which
 * can be done with the Bellman-Ford Algorithm. 
 * https://en.wikipedia.org/wiki/Bellman%E2%80%93Ford_algorithm
 *
 * runs in O(N^3) time, O(N^2) space
 */
template<int N>
bool arbitrage(double (&arr)[N][N]) {

  // first log transform the exchange rate table
  double graph[N][N];
  for (int i = 0; i < N; i++) {
    for (int j = 0; j < N; j++) {
      graph[i][j] = -log(arr[i][j]);
    }
  }

  // initialize an array to hold the minimum distances on the graph
  // and initialize the source node to have zero cost
  double minDists[N];
  for (int i = 0; i < N; i++) {
    minDists[i] = (double)INT_MAX;
  }
  minDists[0] = 0;

  // Relax the edges of the graph N - 1 times
  for (int i = 0; i < N - 1; i++) {
    for (int v = 0; v < N; v++) {
      for (int w = 0; w < N; w++) {
        if (minDists[v] + graph[v][w] < minDists[w])
          minDists[w] = minDists[v] + graph[v][w]; 
      }
    }
  }

  // After the relaxation, if the cost can be further reduced,
  // then we know there is a node in a negative sum cycle in 
  // the source nodes path
  for (int v = 0; v < N; v++) {
    for (int w = 0; w < N; w++) {
      if (minDists[v] + graph[v][w] < minDists[w])
        return true;
    }
  }

  return false;
}


int main() {
  
  double test[4][4] = {
    {    1.0,   0.82, 106.4, 1276.25},
    {   0.82,    1.0, 129.7,  1556.4},
    {  106.4,  129.7,   1.0,    12.0},
    {1276.25, 1556.4,  12.0,     1.0},
  }; 

  if (arbitrage(test))
    cout << "Passed" << endl;
  else
    cout << "Failed" << endl;


  return 0;
}
