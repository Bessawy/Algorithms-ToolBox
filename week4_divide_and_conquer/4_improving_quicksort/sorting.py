from random import randint


def partition3(array, left, right):
    l = left + 1
    mid = left + 1
    for j in range(left + 1, right + 1):
        if array[j] == array[left] :
            array[mid], array[j] = array[j], array[mid]
            mid+=1   
        elif array[j] < array[left]:
            array[j], array[mid] = array[mid], array[j]
            array[mid], array[l] = array[l], array[mid]
            mid+=1
            l+=1

    array[left], array[l - 1] = array[l - 1], array[left]
    return l - 1, mid - 1

        
def randomized_quick_sort(array, left, right):
    if left >= right:
        return
    k = randint(left, right)
    array[left], array[k] = array[k], array[left]
    m1, m2 = partition3(array, left, right)
    randomized_quick_sort(array, left, m1 - 1)
    randomized_quick_sort(array, m2 + 1, right)


if __name__ == '__main__':
    input_n = int(input())
    elements = list(map(int, input().split()))
    assert len(elements) == input_n
    randomized_quick_sort(elements, 0, len(elements) - 1)
    print(*elements)
