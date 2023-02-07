def edit_distance(first_string, second_string):
    n, m = len(first_string), len(second_string)
    arr = []
    subArr = []
    for i in range(m + 1):
        subArr.append(i)
    arr.append(subArr)
    
    for i in range(n):
        subArr = [0] * (m + 1)
        subArr[0] = i + 1
        arr.append(subArr)

    for i in range(1, n + 1):
        for j in range(1, m + 1):

            if(first_string[i-1] == second_string[j - 1]):
                arr[i][j] = arr[i-1][j-1]
            else:
                minValue = min(arr[i - 1][j - 1], arr[i][j - 1])
                minValue = min(minValue, arr[i - 1][j])
                arr[i][j] = 1 + minValue

    return arr[n][m]


if __name__ == "__main__":
    print(edit_distance(input(), input()))
