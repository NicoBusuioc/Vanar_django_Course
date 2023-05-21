

class Node:
    def __init__(self, value):
        self.value = value
        self.next = []

    def __str__(self):
        if not self.next:
            result = f"[{self.value}]--"
        else:
            result = f"[{self.value}]-- next --> "
            for node in self.next:
                if node == self.next[-1]:
                    result += f"[{node}]"
                else:
                    result += f"[{node}]-- next --> "
        return result

    def insert_node(self, *args):
        if len(args):
            for node in args:
                self.next.append(node)


a = Node(100)
a.insert_node(200, 300, 400, 500)
print(a)
