from node import Node


def traverse(node):
    ## HW1 ##
    if type(node) is not Node:
        raise TypeError("'node' must be an instance of Node class")
    print(node.subject)

    ## HW2 ##
    if type(node.nextYes) is Node or type(node.nextNo) is Node:
        answer = input("yes/no..?...")

        if answer == 'yes':
            traverse(node.nextYes)
        if answer == 'no':
            traverse(node.nextNo)
