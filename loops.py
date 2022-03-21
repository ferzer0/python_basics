print("#1----------------")
animals = ("dog", "cat", "bird")
for animal in animals:
    print(animal)
print("#2----------------")
a = 0
while a <= 10:
    a += 1
    if a == 5:
        continue
    print(a)
print("#3----------------")
animals2 = ("dog", "cat", "bird")
colors = ("white", "black", "orange")
for check_a in animals2:
    for check_c in colors:
        print(check_a, check_c)
print("#4----------------") #add capital or small letter
mindanao = ["Butuan City", "Davao City", "Gensan City", "Surigao City"]
check_city = input("Enter a city: ")
for city in mindanao:
    if check_city == city:
        print(check_city, "is one of the cities in mindanao")
        break
else:
    print("Not one of mindanao")
        
print("#5----------------")
outer = 0
inner = 0
num = [1, 3, 5]
num2 = [2, 4]
for num_check in num:
    outer += 1
    for num2_check in num2:
        inner += 1
        if num_check == 3 and num2_check == 4:
            print(outer + inner)
print("#6----------------")
enter_name = input("Enter subject for grade results: ")
grade = {"Math":74, "Science": 91, "Computer": 99}

for check_grade in grade:
    if check_grade== enter_name:
        print(grade[check_grade])
        break
else:
    print("Wrong input!")
print("#7----------------")
enter_num = input("How many times you want to print Hello?")
conv_num = int(enter_num)
i = 1 #iteration
while i <= conv_num:
    
    print("Hello!", i)
    i=i+1
    