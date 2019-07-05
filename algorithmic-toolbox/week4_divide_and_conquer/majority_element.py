# Uses python3
import sys


def get_majority_element(a, left, right):
	#write your code here
	a = mergesort(a)
	mid = len(a) // 2
	
	track = a[0]
	track_cnt = 1
	for v in a[1:]:
		if v == track:
			track_cnt += 1
			if track_cnt > len(a) / 2.:
				return 1
		else:
			track = v
			track_cnt = 1
		
	return -1

	
def mergesort(a):
	if len(a) == 1:
		return a
	m = len(a) // 2
	b = mergesort(a[0:m])
	c = mergesort(a[m:len(a)])
	a = merge(b, c)
	return a
	
def merge(a, b):
	r = []
	while a and b:
		if a[0] < b[0]:
			r.append(a.pop(0))
		else:
			r.append(b.pop(0))
	
	# append remaining elements to result array
	if a:
		r = r + a
	if b:
		r = r + b

	return r


	
if __name__ == '__main__':
	input = sys.stdin.read()
	n, *a = list(map(int, input.split()))
	if get_majority_element(a, 0, n) != -1:
		print(1)
	else:
		print(0)
