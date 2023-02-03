from sys import stdin
import enum

class Status(enum.Enum):
   Start = 1
   End = 2
   Point = 3


def points_cover(start, end, points):
    dataCount = [0]*len(points)
    data = []

    for i in range(0, len(start)):
        data.append((start[i], 0))
        data.append((end[i], 2))

    for i, p in enumerate(points):
        data.append((p, 1, i))

    data.sort(key=lambda x: (x[0], x[1]))
    count = 0
    for p in data:
        if p[1] == 0:
            count+=1
        elif p[1] == 2:
            count-=1
        else:
            dataCount[p[2]]=count
    return dataCount



def points_cover_naive(starts, ends, points):
    assert len(starts) == len(ends)
    count = [0] * len(points)
    for index, point in enumerate(points):
        for start, end in zip(starts, ends):
            if start <= point <= end:
                count[index] += 1

    return count


if __name__ == '__main__':
    data = list(map(int, stdin.
    read().split()))

    n, m = data[0], data[1]
    input_starts, input_ends = data[2:2 * n + 2:2], data[3:2 * n + 2:2]
    input_points = data[2 * n + 2:]

    #output_count = points_cover_naive(input_starts, input_ends, input_points)
    #print(*output_count)
    points_cover = points_cover(input_starts, input_ends, input_points)
    print(*points_cover)
