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

