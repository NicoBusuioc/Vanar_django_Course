

class Cabinet():
    def __init__(self):  # Top, Middle, Bottom
        self.shelf = [None, None, None]

    def putOn(self, shelfName, thing):
        shelf_level = self._check_shelf_name_and_position(shelfName)
        if shelf_level == None:
            print(f"Unkown position name {shelfName}!")
            return

        if self.shelf[shelf_level]:
            print(f"Cannot place {thing} on top shelf, it is not empty!")
        else:
            self.shelf[shelf_level] = thing
            print(f"{thing} was placed on the {shelfName}")

    def takeFrom(self, shelfName):
        shelf_level = self._check_shelf_name_and_position(shelfName)
        if shelf_level == None:
            print(f"Unkown position name {shelfName}!")
            return

        if self.shelf[shelf_level]:
            print(
                f"The {self.shelf[shelf_level]} was taken from the {shelfName}")
            self.shelf[shelf_level] = None
        else:
            print(f"Nothing to take! The top shelf is empty")

    def printSchema(self):
        print("##############################")
        print(self._create_str_for_schema(self.shelf[0]))
        print("##############################")
        print(self._create_str_for_schema(self.shelf[1]))
        print("##############################")
        print(self._create_str_for_schema(self.shelf[2]))
        print("##############################")

    def _create_str_for_schema(self, shelf):
        if not shelf:
            return ("#                            #")
        new_shelf = list(shelf)
        if len(new_shelf) < 28:
            while True:
                if len(new_shelf) == 27:
                    new_shelf.insert(0, " ")
                    new_shelf.insert(0, "#")
                    new_shelf.append("#")
                    break
                elif len(new_shelf) == 28:
                    new_shelf.insert(0, "#")
                    new_shelf.append("#")
                    break
                else:
                    new_shelf.insert(0, " ")
                    new_shelf.append(" ")

            return ''.join(new_shelf)
        else:
            return shelf

    def _check_shelf_name_and_position(self, name):
        if name == 'top':
            return 0
        if name == "middle":
            return 1
        if name == "bottom":
            return 2
        return None


my_shelf = Cabinet()
my_shelf.putOn('top', 'book')
my_shelf.takeFrom('top')
my_shelf.putOn('bottom', 'my laptop')
my_shelf.printSchema()
