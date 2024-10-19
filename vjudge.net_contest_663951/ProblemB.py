def format_input():
	t, = list(map(int, input().split()))
	n, a, = [0] * t, [None] * t
	for i in range(t):
		n[i], = list(map(int, input().split()))
		a[i] = list(map(int, input().split()))

	return t, n, a,

def get_answer(t, n, a):

	possibilities = []
	for i in range(t):
		target = sum(a[i]) // n[i]
		res = sum(a[i]) % n[i]
		buffer = 0
		for j in range(n[i]):
			if j == n[i] - res:
				target += 1
			buffer += target - a[i][j]
			if buffer < 0:
				possible = False
				break
		else:
			possible = True

		possibilities.append(possible)

	return possibilities,

def print_answer(possibilities):
	for possible in possibilities:
		if possible:
			print("Yes")
		else:
			print("No")

if __name__ == '__main__':
	vals = format_input()

	ans = get_answer(*vals)
	print_answer(*ans)
