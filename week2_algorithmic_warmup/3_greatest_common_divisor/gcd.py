def gcd(a, b):

    if(a < b):
        a, b = b, a

    while(b):
        a, b = b, a%b
    return a


if __name__ == "__main__":
    a, b = map(int, input().split())
    print(gcd(a, b))
