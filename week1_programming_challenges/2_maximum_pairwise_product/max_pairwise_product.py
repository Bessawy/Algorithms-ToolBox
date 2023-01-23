def max_pairwise_product(numbers):
    n = len(numbers)
    max_ind = 0
    max_ind_2 = 0

    for i in range(1, n):
        if(numbers[max_ind] < numbers[i]):
            max_ind = i

    if(max_ind == 0):
        max_ind_2+=1
        
    for i in range(n):
        if(numbers[max_ind_2] < numbers[i] and max_ind != i):
            max_ind_2 = i        
        
    max_product = (numbers[max_ind])*(numbers[max_ind_2])
    return max_product


if __name__ == '__main__':
    _ = int(input())    
    input_numbers = list(map(int, input().split()))
    print(max_pairwise_product(input_numbers))
