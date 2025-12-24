
""""
grade = 50
if grade < 50:
    print("failed")
elif grade >= 50:
    print("good")
else:
    print("very good")
"""
# for loop............................
# for i in range(100):
#     print(i+1)

# while loop........................
#  count = 1
# while count < 5:
#     print(count)
#     count += 1

# list comprehension two ways accur:-
# tradional way#

# squares = {}
# for i in range(10):
#     squares.append(i*i)
# print(squares)

# comprehension list
# squares = {i*i for i in range(10)}
# print(squares)


# lists....................
# fruites = ["banana", "apple", "orange"]
# print(fruites[2])
# fruites.append("mango")
# print(fruites)

# tuple..................
# coordinates = (10, 20, 30, 40)
# print(coordinates[3])
# coordinates.append(50)
# print(coordinates) "ma aqabalaayo in wax lagu daro tuple"


# unique_numbers.............................
# unique_numbers = {1, 2, 3, 2, 4, 2, 1, 7}
# print(unique_numbers)

# dictionray..................................
# person = {"name": "Ahmed", "age": 25, "phone": 634067224, "city": "Burao"}
# print(person)
# person["gender"] = "male"
# print(person)
# person["village":] = "qasabka"
# print(person)


# concantination : markaad isku xidhaysid labo string aya la adeegsada.

# from ast import Return


# greeting = "Hello"
# name = "Timir"
# print(greeting+" "+name)

# message = f"{greeting} {name}"  # this the way of expression
# print(message)

# functions................................


# def greet(name):
#     return f"hello {name}"


# print(greet("mukhtar"))

# lambda...................
# def divider(a, b): return a/b

# print(divider(10, 4))

# import models.......................
# import math
# print(math.sqrt(100))


# date and time
# from datetime import date
# print(date.today())

# writing files....................................
# with open("example.text", "w") as file:
#     file.write("hello world")

# reading file..................................
# with open("example.txt", 'r') as file:
#     content = file.read()
#     print(content)
# with open("example.php", 'r') as file:
#     content = file.read()
#     print(content)

# with open("example.text", 'r') as file:
#     content = file.read()
#     print(content)

# erorr handalig....................................
# try:
#     number = int(input("Enter you number:"))
#     print(f"you Entered {number}")
# except ValueError:
#     print("That's not a valid number!")


# abstraction(inaad qarisid code ka badh ka mid ah).......
# class RemoteControl:
#     def change_channel(self, channel):
#         return f"changing channel to {channel}"

#     def adjust_valume(self, valume):
#         return f"setting valume to {valume}"


# if __name__ == "__main__":
#     remote = RemoteControl()
#     print(remote.change_channel("mmtv"))
#     print(remote.adjust_valume(40))
