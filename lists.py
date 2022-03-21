print("#1--------------------")
animals = ["dogs", "cats", "monkeys"]
print(animals[0] + " are cute!")
print("#2--------------------")
numbers = [1, 5]
c = len(numbers)
sum = numbers[0] + numbers[1] + c
print(sum)
print("#3--------------------")
dogs = ["Yin", "Yang", "Oreo"]
j = ",".join(dogs[i] for i in [0, 1])
cnt = len(dogs)
print("I have", cnt ,"dogs", j + " and", dogs[2])
print("#4--------------------")
city = ["Butuan City", "Davao City"]
city.insert(1, "Gensan City")
city.append("Surigao City")
print(city)
print('#5--------------------')
enter = input("Enter fruit you don't like: ")
fruits = ["apple", "mango", "jack fruit", "orange", "dragon fruit", "atis"]
fruits.pop(1)
fruits.remove(enter)
del fruits[0]
print(fruits)
print('#6--------------------')
subject = ["science", "computer", "english"]
subject2 = ["history", "math"]
subject.extend(subject2)
print(subject)
print('#7--------------------')
nba = ["warriors", "cavaliers", "mavericks"]
nba2 = ["lakers", "suns"]
nba.sort()
nba2.reverse()
print(nba, nba2)