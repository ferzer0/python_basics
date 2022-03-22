import datetime
print("#1-------------")
num1 = 5
num2 = 10
sum = num1 + num2
print(sum)
print("#2-------------")
num3 = 3
num4 = 4
num5 = 2
calculated = num3 + num4 * (num3 + num5)
print(calculated)
print("#3-------------")
num6 = 9
number_to_increment = 3
num6 += number_to_increment
print(num6)
print("#4-------------")
name = input("Enter name: ").capitalize()
name1 = "Fernan"

if name == name1:
    print("you are authorized Mr.", name)
else:
    print("You are not authorized!")
print("#5-------------")
enter_num = input("Enter between 1-10 a number:")
entered = int(enter_num)

if 0 < entered <= 10:
    print("Entered the right number which is", entered)
elif entered > 10:
    print("The number you entered", entered, "exceeded to 10")
else:
    print("Numbers beyond 1 is not acceptable!")
print("#6-------------")
age = input("Enter your age: ")
conv_age = int(age)

if conv_age > 17 and conv_age <= 41:
    print("You are qualified!")
elif conv_age > 41:
    print("You\'re too old for this")
elif conv_age < 18:
    print("You\'re too young for this")
print("#7-------------")
age = input("Enter age: ")
conv_num = int(age)
place_resident = input("Enter Country:")
      
if (conv_num < 65 and conv_num >= 21) and place_resident == "Philippines":
    print("You're legally allowed travelling outside Philippines")
else:
    print("Sorry you're not allowed to travel")


