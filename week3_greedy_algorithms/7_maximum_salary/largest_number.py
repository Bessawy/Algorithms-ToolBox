import functools
from itertools import permutations

def largest_number_naive(nums):
    def comparator(s1, s2):
            if int(s1+s2) < int(s2+s1):
                return -1
            if int(s1+s2) > int(s2+s1):
                return 1
            return 0
        
    nums = sorted(nums, key = functools.cmp_to_key(comparator),  reverse = True)
    ans = '0' if nums[0] == '0' else ''.join(nums)      # if the biggest number after sorting is 0 in first position, then rest all will also be 0's so return 0
    return ans


def largest_number_naive2(numbers):
    numbers = list(map(str, numbers))

    largest = 0

    for permutation in permutations(numbers):
        largest = max(largest, int("".join(permutation)))

    return largest


if __name__ == '__main__':
    _ = int(input())
    input_numbers = input().split()
    print(largest_number_naive(input_numbers))
  
