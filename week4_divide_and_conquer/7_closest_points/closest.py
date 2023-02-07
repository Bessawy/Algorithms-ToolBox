from collections import namedtuple
from itertools import combinations
from math import sqrt

Point = namedtuple('Point', 'x y')
def distance_squared(first_point, second_point):
    return (first_point.x - second_point.x) ** 2 + (first_point.y - second_point.y) ** 2

#def minimum_distance_squared(points):
def minimum_distance_squared_naive(points):
    min_distance_squared = float("inf")
    for p, q in combinations(points, 2):
        min_distance_squared = min(min_distance_squared,
                                   distance_squared(p, q))
    return min_distance_squared

import math
 
 
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
 
 
def compareX(a, b):
    p1 = a
    p2 = b
    return (p1.x - p2.x)
 
 
def compareY(a, b):
    p1 = a
    p2 = b
    return (p1.y - p2.y)
 
 
def dist(p1, p2):
    return math.sqrt((p1.x - p2.x)*(p1.x - p2.x) + (p1.y - p2.y)*(p1.y - p2.y))
 
 
def bruteForce(P, n):
    min_dist = float("inf")
    for i in range(n):
        for j in range(i+1, n):
            if dist(P[i], P[j]) < min_dist:
                min_dist = dist(P[i], P[j])
    return min_dist
 
 
def min(x, y):
    return x if x < y else y
 
 
def stripClosest(strip, size, d):
    min_dist = d
    strip = sorted(strip, key=lambda point: point.y)
 
    for i in range(size):
        for j in range(i+1, size):
            if (strip[j].y - strip[i].y) >= min_dist:
                break
            if dist(strip[i], strip[j]) < min_dist:
                min_dist = dist(strip[i], strip[j])
    return min_dist
 
 
def closestUtil(P, n):
    if n <= 3:
        return bruteForce(P, n)
    mid = n//2
    midPoint = P[mid]
    dl = closestUtil(P, mid)
    dr = closestUtil(P[mid:], n - mid)
    d = min(dl, dr)
    strip = []
    for i in range(n):
        if abs(P[i].x - midPoint.x) < d:
            strip.append(P[i])
    return min(d, stripClosest(strip, len(strip), d))
 
 
def closest(P, n):
    P = sorted(P, key=lambda point: point.x)
    return closestUtil(P, n)

if __name__ == '__main__':
    input_n = int(input())
    input_points = []
    for _ in range(input_n):
        x, y = map(int, input().split())
        input_point = Point(x, y)
        input_points.append(input_point)
    print("{0:.9f}".format(sqrt(minimum_distance_squared_naive(input_points))))
    print("{0:.9f}".format(sqrt(minimum_distance_squared_naive(input_points))))
