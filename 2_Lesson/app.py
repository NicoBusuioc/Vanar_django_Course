from node import Node
from algo import traverse

n1 = Node("1. Solved it peacefull between two parts?")

n1.nextYes = Node("2. Success!")
n1.nextNo = Node("3. Reported and solved by superior")

n1.nextNo.nextYes = Node("4. Success!")
n1.nextNo.nextNo = Node("5. Solved by law!")

n1.nextNo.nextNo.nextYes = Node("6. Success!")
n1.nextNo.nextNo.nextNo = Node("7. Unsuccessful!")

# print(n1)

# TRAVERSING THE TREE
traverse(n1)
