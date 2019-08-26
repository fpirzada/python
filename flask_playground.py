# class player:
#
#     name_of_player = "Adil"
#
#     def __init__(self):
#         self.name = "Farhan"
#         self.number = 1,2,3,4
#
#     def bentchPlayer(self, name):
#         return "list of the players {} {} {}".format(self.name, self.number, name)
#
#
# players = player()
# # print(players.name)
# # print("the player name is {}".format(players.__class__.name_of_player))
# print(players.bentchPlayer("adil"))

class Student:
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.marks = []

    def avg(self):
        return sum(self.marks)/len(self.marks)
# Farhan = Student("Farhan","GHS")
# print(Farhan.name, Farhan.school)
# Farhan.marks.append(29)
# Farhan.marks.append(1)
# print(Farhan.avg())


class Store:

    def __init__(self, name):
        self.name = name
        self.items =[]

    def add_item(self, name, price):

        item = {"name": name, "price": price}

        self.items.append(item)

    def stock_price(self):
        return sum([item["price"] for item in self.items])


test = Store("testt")
print(test.add_item("test",100))
print(test.add_item("test2",200))
print(test.stock_price())


