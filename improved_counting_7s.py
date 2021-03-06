import math

def countNumbersContaining7(n):
    '''
    Improved implementation of counting numbers containing a 7 from 1 to N. The idea is that the function
    builds on the previous calculations every time a digit is added or power of 10 reached. It's unnecessary
    to go through all of the numbers from 1 to n.

    First, take a look at how each power of 10 builds on each other:
    g(1) = 0
    g(10) = 1
    g(100) = g(10) + (8 * g(10)) + (10 * 1)
    g(1000) = g(100) + (8 * g(100)) + (100 * 1)

    When calculating g(100), we add 1 g(10) which represents 0-10, 8 g(10)'s representing 11-20, 21-30...
    EXCLUDING 70-79, and the final 10 numbers which do represent 70-79. We can do the same thing for g(1000)
    by summing 0-100, 101-200... 9 total times, and adding 100 for 700-799. The pattern derived 
    for a number that's a power of 10 is then:

    g(n) = 9 * g(10^digits-1) + 10^digits-1 

    Where "digits" is the power of n.

    This only solves half of the problem as we can calculate for powers of 10. However, we must handle 3 cases
    when generalizing for all of n.
    
    1. If the first digit is 7, such as 750, count from 1-699 and then 700-750
    2. If the first digit of n (most significant) is less than 7, such as 348, count everything from 1 to 300
    and then recursively count from 1 to 40, 1 to 8  
    3. If the first digit is greater than 7, such as 937, count from 1 to 699, 800 to 900, add 100 for
    700-799, and recursively count from 1 to 37, 1 to 7.

    This approach has a complexity of O(m) where m is the number of digits. We use the formula to
    store the result for each power of 10 up to 10^m-1 and then at most go through m digits recursively.
    '''

    result = 0

    # If number less than 7, return 0
    if n < 7:
        return result

    # First fill dp array with calculations for powers of ten using formula
    digits = int(math.log10(n))+1
    dp = [0 for i in range(digits)] 
    dp[0] = 0 # g(0) = 0

    for i in range(1, digits):
        dp[i] = 9 * dp[i-1] + pow(10, i - 1) # dp[i] == g(10^i)

    result += count7sHelper(n, digits, dp)

    return result

def count7sHelper(n, digits, dp):
    if n < 7 or digits < 1:
        return 0

    power = pow(10, digits - 1) # 10 ^ d-1
    mostSigDigit = n // power

    # Case 1
    if mostSigDigit == 7:
        return mostSigDigit * dp[digits - 1] + (n % power) + 1

    # Case 2
    if mostSigDigit < 7:
        return mostSigDigit * dp[digits - 1] + count7sHelper(n % power, digits-1, dp)

    # Case 3
    if mostSigDigit > 7:
        return (mostSigDigit - 1) * dp[digits - 1] + power + count7sHelper(n % power, digits-1, dp)


if __name__ == '__main__':
    print (f"g(0) = {countNumbersContaining7(0)}")
    print (f"g(7) = {countNumbersContaining7(7)}")
    print (f"g(20) = {countNumbersContaining7(20)}")
    print (f"g(70) = {countNumbersContaining7(70)}")
    print (f"g(100) = {countNumbersContaining7(100)}")
    print (f"g(1000) = {countNumbersContaining7(1000)}")
    
    # Test cases 1, 2, 3
    print (f"g(750) = {countNumbersContaining7(750)}")
    print (f"g(348) = {countNumbersContaining7(348)}")
    print (f"g(937) = {countNumbersContaining7(937)}")

    '''
    Results 
    g(0) = 0
    g(7) = 1
    g(20) = 2
    g(70) = 8
    g(100) = 19
    g(1000) = 271
    g(750) = 184
    g(348) = 62
    g(937) = 256
    '''
