def main():
	expected_file_name = "test01-output.txt"  # Change this
	your_file_name = "mysol.txt"  # Change this
	d1 = readfile(expected_file_name)
	d2 = readfile(your_file_name)
	print("Expected file Total distance: ", d1)
	print("Your file Total distance: ", d2)
	if (d1 == d2):
		print("They are the same distance")
	else:
		print("Yours is off by: ", (d1 - d2))
	return


def readfile(file_name):
	f = open(file_name, "r")
	line1 = f.readline()
	line1 = line1.split(' ')
	l = line1[1][:-1]
	num_lines = int(l)
	distance = 0
	for i in range(0, num_lines):
		line = f.readline()
		line = line.split()
		if i != 0:
			d = abs(int(lineL[1]) - int(line[1])) + abs(int(lineL[2][:-1]) - int(line[2][:-1]))
			distance += d
		lineL = line
	f.close()
	return(distance)
main()
