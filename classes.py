
print("#1----------------")
class Sample:
    text = "Fernan"

print(Sample.text)
print("#2----------------")
class Name:
    def __init__(self, name, age):
        self.name = name
        self.age = age

person1 = Name("Sophia", 22)
person2 = Name("Henry", 24)
print(person1.name, "is", person1.age, "years old")
print(person2.name, "is", person2.age, "years old")
print("#3----------------")
class Name:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print_person(self):
        print(self.name, "is", self.age, "years old")

person1 = Name("Sophia", 22)
person2 = Name("Henry", 24)
person1.print_person()
person2.print_person()
print("#4----------------")
class Person:
    def __init__(self, age, gender):
        self.age = age
        self.gender = gender
    
def check_minor(person_age):
    if person_age < 18:
        print("This person is minor")
    else:
        print("This age is legal")

p1 = Person(19, "Male")
check_minor(p1.age)
print("#5----------------")
class Vote:
    def __init__(self, name, age, citizen):
        self.name = name
        self.age = age
        self.citizen = citizen 
    def check_age(self):
        if self.age > 18 and self.citizen == "Filipino":
            print("Congrats " + self.name + " you're now registered voter!")
        else:
            print("Sorry you have to wait until 18!")

enter_name = input("Enter Name: ")
conv_name = enter_name.capitalize()
enter_age = input("Enter age: ")
conv_age = int(enter_age)
enter_citizen = input("Enter Citizen: ")
conv_citizen = enter_citizen.capitalize()

v1 = Vote(conv_name, conv_age, conv_citizen)
v1.check_age()
print("#6----------------")
class Patient:
    def __init__(self, name, disease, age):
        self.name = name
        self.disease = disease
        self.age = age
    def edit_patient(self):
        print("Name: " + self.name + "\nDisease: " + self.disease + "\nAge: ", self.age)
        enter_input = input("Is this the right information? type yes or no:")
        conv_input = enter_input.casefold()
        if conv_input == "yes":
            print("All set!")
        if conv_input == "no":
            enter_name = input("Enter Name: ")
            convert_name = enter_name.title()
            enter_disease = input("Enter your disease: ")
            convert_disease = enter_disease.title()
            enter_age = input("Enter Age: ")
            convert_age = int(enter_age)

            self.name = convert_name
            self.disease = convert_disease
            self.age = convert_age

            print("Fields are now changed!\nName: " + self.name + "\nDisease: " 
                    + self.disease + "\nAge: ", self.age)


a1 = Patient("Josph", "Covd", 18)
a1.edit_patient()
print("#7----------------")
class Country:
    def __init__(self, city, country):
        self.city = city
        self.country = country 
    
    def print_this(self):
        print(self.city, "is located at", self.country)

class Continent(Country):
    def __init__(self, city, country, continent):
        super().__init__(city, country)
        self.continent = continent
    
    def Print_Continent(self):
        print(self.city, "is located at", self.country, "and belongs to continent", self.continent)

continent1 = Continent("Butuan City", "Philippines", "Asia")
continent1.Print_Continent()



