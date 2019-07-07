# Uses python3
import sys
import random

def randomized_quick_sort(a, l, r):
	if l >= r:
		return
	k = random.randint(l, r)
	a[l], a[k] = a[k], a[l]
	#use partition3
	m1, m2 = partition3(a, l, r)
	randomized_quick_sort(a, l, m1);
	randomized_quick_sort(a, m2 + 1, r);	

def partition3(a, l, r):
    #write your code here
	x = a[l]
	m1 = l
	m2 = l
	for i in range(l + 1, r + 1):
		if a[i] < x:
			m2 += 1
			a[i], a[m2] = a[m2], a[i]
			a[m1], a[m2] = a[m2], a[m1]
			m1 += 1
		elif a[i] == x:
			m2 += 1
			a[i], a[m2] = a[m2], a[i]
	
	return m1, m2

def binary_search(a, x, left, right):
    
    if left == right:
        if a[left] > x:
            return left - 1
        else:
            return left
    
    
    mid = left + ((right - left) // 2)
    
    if a[mid] == x:# or left == right:
        return mid
    elif a[mid] > x:
        return binary_search(a, x, left, mid)
    elif a[mid] < x:
        return binary_search(a, x, mid+1, right)
    
def fast_count_segments(starts, ends, points):
    cnt = [0] * len(points)
    
    #write your code here
    randomized_quick_sort(starts, 0, len(starts)-1)
    randomized_quick_sort(ends, 0, len(ends)-1)
    
    for idx in range(len(points)):
        a = binary_search(starts, points[idx]+0.5, 0, len(starts)-1)
        b = binary_search(ends, points[idx]-0.5, 0, len(ends)-1)

        cnt[idx] = a - b
        
    return cnt

def naive_count_segments(starts, ends, points):
    cnt = [0] * len(points)
    for i in range(len(points)):
        for j in range(len(starts)):
            if starts[j] <= points[i] <= ends[j]:
                cnt[i] += 1
    return cnt

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[1]
    starts = data[2:2 * n + 2:2]
    ends   = data[3:2 * n + 2:2]
    points = data[2 * n + 2:]
    #use fast_count_segments
    cnt = fast_count_segments(starts, ends, points)
    for x in cnt:
        print(x, end=' ')
