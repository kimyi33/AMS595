#include <iostream>
#include <vector>
#include "functions.h"
using namespace std;

int main() {
    // Question 1
    question1();
    cout << "\n\n";

    // Question 2 test
    vector<int> v = {1, 2, 3, 4, 5};
    print_vector(v);
    cout << "\n\n";

    // Question 3
    question3_fibonacci();
    cout << "\n\n";

    // Question 4 test
    test_isprime();
    test_factorize();
    test_prime_factorize();
    cout << "\n";


    // Question 5 test
    pascal_triangle(6);
    return 0;
}


