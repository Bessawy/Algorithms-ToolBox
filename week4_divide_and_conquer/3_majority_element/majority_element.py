def majority_element_naive(elements):
    for e in elements:
        if elements.count(e) > len(elements) / 2:
            return 1

    return 0

def majority_element(elements):
    hashmap = {}
    for e in elements:
        if e in hashmap.keys():
            hashmap[e]+=1
        else:
            hashmap[e]=1
        
        if hashmap[e] > len(elements) / 2:
            return 1
    return 0

if __name__ == '__main__':
    input_n = int(input())
    input_elements = list(map(int, input().split()))
    assert len(input_elements) == input_n
    #print(majority_element_naive(input_elements))
    print(majority_element(input_elements))
