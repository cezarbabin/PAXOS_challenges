import sys

class Task(object):
	def __init__(self, string, combination_format, nr, x_indexes):
		self.string = string
		self.format = combination_format
		self.nr = nr
		self.x_positions = x_positions

def get_x(s):
	indexes = []
	for i in range(len(s)):
		if s[i] == "X":
			indexes.append(i)
	return indexes

def f(task):
	combinations = []
	string = list(task.string)
	combination_format = task.format
	combination_range = task.nr
	x_positions = task.x_positions
	
	for i in range(2**(combination_range - 1), 2**combination_range):
		combinations.append(combination_format.format(i))

	for combination in combinations:
		for i in range(len(x_positions)):
			index = x_positions[i]
			char = combination[i]
			string[index] = char
		to_print = ""
		for char in string:
			to_print += char
		print to_print
	return

a = []
if __name__ == '__main__':
	string = sys.argv[1]
	x_positions = get_x(string)
	nr_of_x = len(x_positions)
	combination_format = "{0:0" + str(nr_of_x) + "b}"
	print string.replace('X', '0')
	for i in range(1,nr_of_x + 1):
		task = Task(string, combination_format, i, x_positions)
		f(task)