print("#1----------------")
class Checker:
    def __init__(self, enter):
        self.enter = enter

    def check(self):
        validator = {"y":"yes", "n":"no"}
        try:
            
            x = validator[self.enter]
            print(x)
        except KeyError:
            print("Invalid input")


enter_confirm = input("choose between y or n:").lower()
e1 = Checker(enter_confirm)
e1.check()


print("#2----------------")
class Sum:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2 
    
    def calc(self):
        
        try:
            a = int(self.num1)
            b = int(self.num2)
            sum = a + b
            if sum <= 100:
                result = sum
            print("Result: ", result)
        except ValueError:
            print("Invalid Input")
        except:
            print("Number exceeded to 100")

enter = input("Input first number:")

enter2 = input("Input second number:")


solve = Sum(enter, enter2)
solve.calc()
print("#3----------------")
class Array:
    def __init__(self, array):
        self.f_array = array

    def check_array(self):
        
        animals = ["cat", "dog", "bird"]
        
        for animal in animals:
            if animal == self.f_array:
                get_search = self.f_array
            
        try:
            print(get_search, "is Available")
        except:
            print(self.f_array, "Didn't exist")
            

find = input("Search for animals if it's available: ").casefold()
a1 = Array(find)
a1.check_array()
print("#4----------------")
class Subjects:
    def __init__(self, name, sub, grade):
        self.name = name
        self.sub = sub
        self.grade = grade

    def get_card(self):
        name = self.name
        grade = self.grade
        sub = self.sub           
         
        try:
            if 100 >= grade >= 92:
                print(name, "Grade A at subject", sub)
            elif 91 >= grade >= 86:
                print(name, "Grade B at subject", sub)
            elif 85 >= grade >= 81:
                print(name, "Grade C at subject", sub)
            elif 80 >= grade >= 75:
                print(name, "Grade D at subject", sub)
            else:
                print("invalid input!")
        except :
            print("Grade Failed!")          
        finally:
            print("final grade:", grade)
              
input_name = input("Enter Name: ")
input_sub = input("Enter Subject: ")
input_grade = input("Enter grade: ")

sub1 = Subjects(input_name.title(), input_sub.title(), int(input_grade))
sub1.get_card()
print("#5----------------")
