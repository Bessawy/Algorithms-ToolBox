def binary_search(keys, query):
    r = -1
    h = len(keys) - 1
    l = 0
    while(l <= h):
        m = (h - l + 1)//2 + l
        if(keys[m] == query):
            r = m
            break
        elif(query > keys[m]):
            l = m + 1
        else:
            h = m - 1
            
    return r

if __name__ == '__main__':
    num_keys = int(input())
    input_keys = list(map(int, input().split()))
    assert len(input_keys) == num_keys

    num_queries = int(input())
    input_queries = list(map(int, input().split()))
    assert len(input_queries) == num_queries

    for q in input_queries:
        print(binary_search(input_keys, q), end=' ')
