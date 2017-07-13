import turtle
def star(n, k, size):
	angle = k*360/n
	for i in range(n):
		turtle.forward(size)
		turtle.right(angle)

def spiro(n, size):
	turtle.resetscreen()
	angle = 360/n
	for i in range(n):
		for j in range(36):
			turtle.forward(size)
			turtle.right(10)

		turtle.right(angle)
