// Last updated: 08/07/2026, 20:49:16
bool isPowerOfThree(int n) {
    if (n <= 0) return false;

    while (n % 3 == 0) {
        n /= 3;
    }

    return n == 1;
}
