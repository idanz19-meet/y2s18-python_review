# Write your solution for 1.4 here!
a =0
def is_prime(x):
	for i in range(2,x):
		if x%(i) == 0:
			return False
	return True

print(is_prime(27))

for i in range(200):
	if is_prime(i):
		print(i)