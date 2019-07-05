# Uses python3
import sys

def get_number_of_inversions(a, b, left, right):
	#write your code here
	_, number_of_inversions = mergesort(a)
	
	return number_of_inversions

def mergesort(a):
	if len(a) == 1:
		return a, 0
	m = len(a) // 2
	b, bi = mergesort(a[0:m])
	c, ci = mergesort(a[m:len(a)])
	a, i = merge(b, c)
	return a, bi+ci+i
	
def merge(a, b):
	r = []
	i = 0

	while a and b:
		if a[0] <= b[0]:
			r.append(a.pop(0))
		else:
			r.append(b.pop(0))
			i += len(a)

		if not b:
			r.append(a.pop(0))

	# append remaining elements to result array
	if a:
		r = r + a
	if b:
		r = r + b
	
	return (r, i)
	
if __name__ == '__main__':
	input = sys.stdin.read()
	n, *a = list(map(int, input.split()))
	b = n * [0]
	print(get_number_of_inversions(a, b, 0, len(a)))

