from sys import stdin
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')

def optimal_points(segments):
    points = []
    # write your code here
    i = 0
    m = len(segments)
    segments.sort(key= lambda x: x.end)

    while(i < m):
        end_point = segments[i].end

        while(i < m and end_point >= segments[i].start):
            i+=1
        
        points.append(end_point)

    return points

if __name__ == '__main__':
    input = stdin.read()
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(segments)
    print(len(points))
    print(*points)
