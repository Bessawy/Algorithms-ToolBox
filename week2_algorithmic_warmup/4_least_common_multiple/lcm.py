def lcm(a, b):
    if(a < b):
        a, b = b, a
    dom = a*b
    while(b):
        a, b = b, a%b
    return int(dom/a)


if __name__ == '__main__':
    a, b = map(int, input().split())
    print(lcm(a, b))
    print(lcm2(a, b))

