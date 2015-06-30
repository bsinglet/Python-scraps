def to_matrix(text):
	my_matrix = []
	for y in range(0, 5):
		my_row = []
		for x in range(0, 5):
			if ((y*5)+x >= len(text)):
				my_row.append("")
			else:
				my_row.append(text[(y*5)+x])
		my_matrix.append(my_row)
	return my_matrix

# reads from columns first instead of rows.  The following code
# has the same output as its input:
#	by_columns(to_matrix(by_columns(to_matrix(text))))
def by_columns(matrix):
	out_text = ""
	for x in range(0, 5):
		for y in range(0, 5):
			out_text += matrix[y][x]
	return out_text

# Will turn an unscrambled matrix back to plaintext
# e.g.:
#           text = "Hello, World!"
#           text = by_rows(to_matrix(text))
#           print text # gives "Hello, World!"
def by_rows(matrix):
	out_text = ""
	for y in range(0, 5):
    for x in range(0, 5):
			out_text += matrix[y][x]
	return out_text

# swaps two specified rows of a given matrix
def swap_rows(matrix, i, j):
	# do nothing if given invalid row numbers
	if (i < 0 or j < 0 or i > len(matrix) or j > len(matrix)):
		return matrix
	temp = matrix[i]
	matrix[i] = matrix[j]
	matrix[j] = temp
	return matrix

# swaps each row in a matrix with an even number of rows.  In a matrix
# with an odd number of rows, leaves the middle row un-moved.
# E.g.,
#	1 2 3		7 8 9
#	4 5 6	->	4 5 6
#	7 8 9		1 2 3
def swap_all_rows(matrix):
	if (len(matrix) < 2):
		return matrix
	for i in range(0, len(matrix)/2):
		matrix = swap_rows(matrix, i, (len(matrix)-1)-i)
	return matrix

# split text into five-character "words"
def wordize(text):
	out_text = ""
	for x in range(0, len(text)):
		if (x % 5 == 0):
			out_text += " "
		out_text += text[x]
	return out_text

# takes two matrices of equal size and merges them into a matrix
# of twice the dimensions, interleaving values.
# E.g.,
#	1 2 3		A B C
#	4 5 6		D E F
#	7 8 9		G H I
#
#	1 A 2 B 3 C
#	A 1 B 2 C 3
#	4 D 5 E 6 F
#	D 4 E 5 F 6
#	7 G 8 H 9 I
#	G 7 H 8 I 9
def merge_lattice(matrix1, matrix2):
	out_matrix = []
	if (len(matrix1) != len(matrix2) or len(matrix1) == 0):
		return out_matrix
	size = len(matrix1) * 2
	for y in range(0, size):
		my_row = []
		for x in range(0, size):
			my_row.append('')
		out_matrix.append(my_row)
	
	for y in range (0, len(matrix1)):
		for x in range(0, len(matrix1)):
			out_matrix[(y*2)][x*2] = matrix1[y][x]
			out_matrix[(y*2)][(x*2)+1] = matrix2[y][x]
			out_matrix[(y*2)+1][(x*2)+1] = matrix1[y+1][x]
			out_matrix[(y*2)+1][(x*2)] = matrix2[y+1][x]
	return out_matrix
