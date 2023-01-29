from sys import stdin
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')

def optimal_points(segments):
    points = []
    # write your code here
    for s in segments:
        points.append(s.start)
        points.append(s.end)
    return points

def lay_chu_ki(list_time):
    list_time.sort(key=lambda x: x[1])
    idx = 0
    selected_points = []
    
    while idx != len(list_time):
        selected_point = list_time[idx][1]
        
        while idx != len(list_time) and list_time[idx][0] <= selected_point:
            idx += 1
        
        selected_points.append(selected_point)
    
    return selected_points


if __name__ == '__main__':
    input = stdin.read()
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(segments)
    print(len(points))
    print(*points)
