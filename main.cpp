#include <iostream>
#include <cassert>
#include <gmp.h>
#include <map>
#include <fstream>

using namespace std;
using big = mpz_t;

int main() {
    int iteration = 3;
    unsigned long interval_size = 10000000;
    int pow = 2048;

    big tested, p1, p2, res, two, l;
    mpz_init(res);
    mpz_init(p1);
    mpz_init_set_ui(two, 2);
    mpz_init_set_ui(l, interval_size);


    mpz_pow_ui(p1, two, pow);
    mpz_nextprime(p1, p1);
    mpz_init_set(p2, p1);
    mpz_add(p2, p2, l);

    big next, prev, diff;
    mpz_init_set(prev, p1);
    mpz_init_set(next, prev);
    mpz_init(diff);
    mpz_nextprime(next, next);
//    gmp_printf("%Zd\n", prev);
//    gmp_printf("%Zd\n", next);
    unsigned long d;
    std::map<unsigned long, int> data;
    data[0] += 1;

    while (mpz_cmp(next, p2) < 0) {
        mpz_sub(diff, next, prev);
        d = mpz_get_ui(diff);

        data[d] += 1;
        mpz_set(prev, next);
        mpz_nextprime(next, next);
    }

    ofstream f;
    f.open("../out4.csv");
    f << "difference,count" << endl;
    for (const auto& kv : data) {
        f << kv.first << "," << kv.second << endl;
//        std::cout << kv.first      << " has value " << kv.second << std::endl;
    }
    f.close();

    return 0;
}