print("#1----------------")
def num():
    num = 2
    num2 = 3
    sum = num + num2
    print(sum)

num()
print("#2----------------")
def name(fname, lname):
    print(fname, lname)

name("Fernan", "Monton")
print("#3----------------")
def math_solve(num, num2, num3=2):
    calc = num * (num2 + num3)
    print(calc)
math_solve(num2=3, num=2)
print("#4----------------") #captilized or small letter
subject = ["Math", "Science", "English", "Filipino"]
grade = [89, 90, 77, 99]

def get_grade(subject_list=subject, grade_list=grade, get_index_sub=0, get_index_grad=0):
    sub = subject_list[get_index_sub]
    grd = str(grade_list[get_index_grad])
    conc = sub + " = " + grd
    print(conc)

get_grade()
print("#5----------------")
def my_func(*get_str):
    print(get_str[0] + " " + get_str[1] + " " + get_str[2])

my_func("Fernan", "Mari", "Monton")
print("#6----------------")
def my_func2(**get_name):
    arr = [get_name["name"], get_name["name3"], get_name["name2"]]
    print(arr)
my_func2(name="Tim", name2="Henry", name3="Sarah")
print("#7----------------")#error string
def get_num(num, num2):
    return num + num2

ent = input("Enter first number: ")
ent2 = input("Enter second number: ")
conv_ent = int(ent)
conv_ent2 = int(ent2)
g_num= get_num(conv_ent, conv_ent2)
print(g_num)