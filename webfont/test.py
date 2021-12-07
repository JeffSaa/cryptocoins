with open('cryptocoins-colors.css') as f:
	lines = f.readlines()

for line in lines:
	data = line.split(" ")
	coin = data[0][1:]
	color = data[3][1:-1]
	print("\"{}\": \"{}\",".format(coin, color))