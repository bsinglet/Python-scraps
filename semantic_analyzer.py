class TreeNode:
        data = None
	parentNode = None
	leftChild = None
	rightChild = None

class Token:
	type = None
	value = None

my_values = {}

def evaluate(parseTree):
	global my_value
	leftChild = parseTree.leftChild
	rightChild = parseTree.rightChild
	if parseTree.data.type == 'OPERATOR':
		# evaluate different operators
		if parseTree.data.value == '=':
			# evaluate right child, assign to left child in my_values
			if leftChild.data.type != 'IDENTIFIER':
				print "ERROR: Trying to assign to a non-variable: " + leftChild.data.value
				return -1
			if rightChild.data.type != 'CONSTANT':
				rightChild.data.value = evaluate(rightChild)
			my_values[leftChild.data.value] = rightChild.data.value
			return leftChild
		else:
			# all comparison operators require you to evaluate both the left and the right children first
			if leftChild.data.type != 'CONSTANT':
				leftChild.data.value = evaluate(leftChild)
			if rightChild.data.type != 'CONSTANT':
				rightChild.data.value = evaluate(rightChild)
			if parseTree.data.value == '>':
				# see if the value of the left child is greater than the value of the right child
				if leftChild.data.value > rightChild.data.value:
					return True
				else:
					return False
			elif parseTree.data.value == '<':
				# see if the value of the left child is less than the value of the right child
				if leftChild.data.value < rightChild.data.value:
					return True
				else:
					return False
			elif parseTree.data.value == '>=':
				# see if the value of the left child is greater than or equal to the value of the right child
				if leftChild.data.value >= rightChild.data.value:
					return True
				else:
					return False
			elif parseTree.data.value == '<=':
				# see if the value of the left child is less than or equal to the value of the right child
				if leftChild.data.value <= rightChild.data.value:
					return True
				else:
					return False
			elif parseTree.data.value == '!=':
				# see if the value of the left child is not equal to the value of the right child
				if leftChild.data.value != rightChild.data.value:
					return True
				else:
					return False
			elif parseTree.data.value == '==':
				# see if the value of the left child is equal to the value of the right child
				if leftChild.data.value == rightChild.data.value:
					return True
				else:
					return False
	elif parseTree.data.type == 'IDENTIFIER':
		return my_values[parseTree.data.value]

def example_match_rule(parseTree):
        if parseTree.data.type == 'OPERATOR':
                if parseTree.leftChild.data.type == 'IDENTIFIER' and parseTree.rightChild.data.type == 'CONSTANT':
                        print "Rule matched: Given a parse tree of the type"
                        print "         OPERATOR"
                        print "         /       \"
                        print "IDENTIFIER       CONSTANT"

def example_parse_tree():
	to1 = Token()
	to1.type = 'IDENTIFIER'
	to1.value = 'x'

	to2 = Token()
	to2.type = 'OPERATOR'

	to3 = Token()
	to3.type = 'CONSTANT'
	to3.value = '3'

	t1 = TreeNode()
	t1.data = to2

	t2 = TreeNode()
	t2.data = to1
	t2.parentNode = t1
	t1.leftChild = t2

	t3 = TreeNode()
	t3.data = to3
	t3.parentNode = t1
	t1.rightChild = t3
