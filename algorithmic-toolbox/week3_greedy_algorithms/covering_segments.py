# Uses python3
import sys
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')

def optimal_points(segments):
    points = []
    
    segments = sorted(segments, key = lambda x: x[0])
    
    while True:
        if len(segments) == 0:
            break
            
        start = segments[0].start
        end = segments[0].end
        segments.pop(0)

        while True:
            if len(segments) == 0:
                break
            
            if segments[0].start <= end:
                if segments[0].end < end:
                    end = segments[0].end
                segments.pop(0)
            else:
                break
        
        points.append(end)
    
    return points

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(segments)
    print(len(points))
    for p in points:
        print(p, end=' ')
