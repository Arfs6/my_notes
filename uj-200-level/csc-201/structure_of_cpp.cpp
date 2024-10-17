// This program converts miles to kilometers.
// From Problem Solving, Abstraction, & Design Using C++
#include <iostream>
using namespace std;

int main() {
  const float KM_PER_MILE = 1.609; // 1.609 kilometers in a mile.
  float miles,                     /// input: distance in miles
      kms;                         // output: distance in kilometers

  // Get the distance in miles
  cout << "Enter the distance in miles: ";
  cin >> miles;

  // convert the distance to kilometers and display it.
  kms = KM_PER_MILE * miles;
  cout << "The distance in kilometers is " << kms << endl;
  return 0;
}
