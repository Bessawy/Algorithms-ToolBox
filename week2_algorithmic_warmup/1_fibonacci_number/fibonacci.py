def fibonacci_number(n):
    if(n <= 1):
        return n

    prev = 0
    prev2 = 1
    for i in range(2, n+1):
        f = prev + prev2
        prev = prev2
        prev2 = f

    return prev2


if __name__ == '__main__':
    input_n = int(input())
    print(fibonacci_number(input_n))
