def countNumbersContaining7(n):
    '''
    Naive implementation of counting numbers containing a 7 from 1 to N. 
    Loop through each number from 1 to N and check if it contains a 7 by using modulus and division. 
    The complexity would be O(m * n) with m being the max number of digits and n being the number to count to. 
    '''

    result = 0

    for i in range(1, n + 1):
        # Check if the number contains a 7
        while (i != 0):
            if (i % 10 == 7):
                result += 1
                break
            i = i // 10

    return result

if __name__ == '__main__':
    print (f"g(0) = {countNumbersContaining7(0)}")
    print (f"g(7) = {countNumbersContaining7(7)}")
    print (f"g(20) = {countNumbersContaining7(20)}")
    print (f"g(70) = {countNumbersContaining7(70)}")
    print (f"g(100) = {countNumbersContaining7(100)}")
    print (f"g(1000) = {countNumbersContaining7(1000)}")
    
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