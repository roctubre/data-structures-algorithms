# python3
import sys



def compute_min_refills(distance, tank, stops):
    # write your code here
    stops.append(distance)
    stops_cnt = 0
    while True:
        next_stop = 0
        for stop_idx in range(len(stops)):
            if tank - stops[stop_idx] >= 0:
                next_stop = stops[stop_idx]
            else:
                break
                
        if next_stop != 0:
            stops_cnt += 1
            
            while True:
                if stops[0] <= next_stop:
                    stops.pop(0)
                    if len(stops) == 0:
                        return stops_cnt - 1
                else:
                    break
            
            for stop_idx in range(len(stops)):
                stops[stop_idx] -= next_stop
            
        else:
            break
                
    return -1

    
if __name__ == '__main__':
    d, m, _, *stops = map(int, sys.stdin.read().split())
    print(compute_min_refills(d, m, stops))
