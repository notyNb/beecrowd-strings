while True:
	try:
		x = input()
	except EOFError:
		break
	x = list(x)
	c = 0

	for i in range(len(x)):
		if ord(x[i]) != 32:
			if (c % 2) == 0:
				x[i] = x[i].upper()
				c += 1
			else:
				x[i] = x[i].lower()
				c += 1

	x = ''.join(x)
	print(x)
