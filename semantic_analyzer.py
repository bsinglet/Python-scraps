class TreeNode:
        data = None
	parentNode = None
	leftChild = None
	rightChild = None

class Token:
	type = None
	value = None

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
