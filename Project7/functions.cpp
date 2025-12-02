#include <iostream>
#include <vector>
#include "functions.h"
#include <cmath>
using namespace std;

// Question 1: Conditional Statements
void question1() {
    int n;
    cout << "Enter a number: ";
    cin >> n;

    switch (n) {
        case -1:
            cout << "negative one\n";
            break;

        case 0:
            cout << "zero\n";
            break;

        case 1:
            cout << "positive one\n";
            break;

        default:
            cout << "other value\n";
    }
}

// Question 2: Printing a Vector
void print_vector(const std::vector<int>& v) {
    for (int x : v) {
        cout << x << " ";
    }
    cout << endl;
}

// Question 3: While Loops
void question3_fibonacci() {
    const int BOUND = 4000000;

    long long f1 = 1;    // first Fibonacci number
    long long f2 = 2;    // second Fibonacci number

    // Print all Fibonacci numbers by 4,000,000
    while (f1 <= BOUND) {
        cout << f1 << " ";

        long long next = f1 + f2;
        f1 = f2;
        f2 = next;
    }
    cout << "\n";
}

// Question 4.1: Is Prime
bool isprime(int n) {
    bool result = true;
    // If n in less than 2, it is not prime
    if (n<2) {
        result = false;
    }
    //It is enough to check the dividers between 2 and sqrt(n)
    //This is because once the number n has a divider between [sqrt(n),n],
    //it also has a divider between [2, sqrt(n)]
    for (int d = 2; d <= sqrt(n); d++) {
        if (n % d == 0) {
            result = false;
        }
    }
    return result;
}

// Question 4.1: Simple test function for isprime
void test_isprime() {
    cout << "isprime(2) = " << isprime(2) << '\n';
    cout << "isprime(10) = " << isprime(10) << '\n';
    cout << "isprime(17) = " << isprime(17) << '\n';
}

// Question 4.2: Factorize
vector<int> factorize(int n) {
    vector<int> answer;

    // Loop from 1 to n
    for (int factor = 1; factor <= n; factor++) {
        if (n % factor == 0) {
            answer.push_back(factor);
        }
    }

    return answer;
}

// Question 4.2: Simple test function for factorize
void test_factorize() {
    print_vector(factorize(2));
    print_vector(factorize(72));
    print_vector(factorize(196));
}

// Question 4.3: Prime Factorization
vector<int> prime_factorize(int n) {
    vector<int> answer;

    int d = 2;
    while (d * d <= n) {
        while (n % d == 0) {
            answer.push_back(d);
            n = n / d;
        }
        d++;
    }
    if (n>1) {
        answer.push_back(n);
    }
    return answer;
}

// Question 4.3: Simple test function for prime factorization
void test_prime_factorize() {
    print_vector(prime_factorize(2));
    print_vector(prime_factorize(72));
    print_vector(prime_factorize(196));
}

// Question 5: Recursive Functions and Loops
// I will use recursion
void pascal_triangle(int n) {
    vector<int> row = {1};   // First row is [1]

    for (int iter = 0; iter < n; iter++) {
        // 1. Print the current row
        print_vector(row);

        // 2. Build next row using padding
        vector<int> padded;
        padded.reserve(row.size() + 2);
        padded.push_back(0);
        for (int x : row) padded.push_back(x);
        padded.push_back(0);

        vector<int> next_row;
        next_row.reserve(padded.size() - 1);
        for (size_t i = 0; i + 1 < padded.size(); i++) {
            next_row.push_back(padded[i] + padded[i + 1]);
        }
        
        row = next_row; // move to the next row
    }
}