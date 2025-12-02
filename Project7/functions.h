#ifndef FUNCTIONS_H
#define FUNCTIONS_H

#include <vector>

void question1();
void print_vector(const std::vector<int>& v);
void question3_fibonacci();
bool isprime(int n);
std::vector<int> factorize(int n);
std::vector<int> prime_factorize(int n);

void test_isprime();
void test_factorize();
void test_prime_factorize();

void pascal_triangle(int n);

#endif