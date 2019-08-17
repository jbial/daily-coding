/*
 * This problem was asked by Two Sigma.
 * Using a function rand7() that returns an integer from 1 to 7 (inclusive) with
 * uniform probability, implement a function rand5() that returns an integer from 
 * to 5 (inclusive).
 *
 * solution
 * Transform the standard normal distribution and cast it to int.
 */
#include <iostream>
#include <random>
#include <ctime>

using std::cout;
using std::endl;
using std::uniform_real_distribution;


// initialize mersenne twister prng with time as random seed 
namespace rand_gen {
	std::mt19937 mersenne(static_cast<std::mt19937::result_type>(std::time(nullptr)));
}
 

// get random numbers in [0, 1.)
double randu(){
  std::uniform_real_distribution<double> uniform(0.0, 1.0);
	return uniform(rand_gen::mersenne); 
}


// returns random integers from [ min, max ) inclusive
int randint(int min, int max) {
  return (int)((max - min + 1) * randu() + min);
}


// returns random numbers from [1,5)
int rand5() {
  return randint(1, 5);
}


// returns random numbers from [1,7)
int rand7() {
  return randint(1, 7);
}


int main() {

  for (int i=1; i<=100; i++) {
    cout << rand7() << ' '; 
    if (i % 10 == 0) cout << '\n';
  }

  return 0;
}
