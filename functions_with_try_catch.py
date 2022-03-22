import datetime
print("#1----------------")
def my_func(num):
    try:
        print(num2)
    except:
        print("Error")

my_func(2)
print("#2----------------")
def get_str():
    text = "Hi"
    try:
        print(text)
    except:
        print("The printed variable didn't exist")
    else:
        print("Everything's fine")

get_str()
print("#3----------------")
enter = input("Enter a word fun:" )
def get_in():
    if enter == "fun":
        x = enter
    try:
        print(x)
    except:
        print("Invalid, you didn't enter \"fun\"")
    else:
        print("It's", enter, "to code")
    finally:
        print("Hello World!")

get_in()
print("#4----------------") 
get_time = datetime.datetime.today()
time_diff = datetime.timedelta(days=10)
total_date = get_time + time_diff
def time():
    future = datetime.timedelta(days=11)
    total_date2 = get_time + future
    if total_date > total_date2:
        x = total_date
    try:
        print("The future date of event is at", x)
    except:
        print("date invalid")
    finally:
        print(total_date, " ", total_date2)
time()
print("#5----------------") 
enter_num = input("Enter number 1-5:")
convert_num = int(enter_num)
def func(nums):
    try:
        i = nums #iteration
        while i <= 5:
            print(i, "Hello")
            x = nums
            i += 1
        print("You entered",x)
    except:
        print("Error! You exceeded to 5!")
    else:
        print("The number you entered which is", nums, "is valid")
func(convert_num)
print("#6----------------")
a = 1
def func2():
    try:
        print(b)
    except NameError as e:
        print(e)
    except:
        print("ERROR!")
    finally:
        print(a)
func2()
print("#7----------------")
input_num = input("Enter a number:")
input_num2 = input("Enter a 2nd number:")


def input(num1, num2):
    try:
        sum = int(num1) + int(num2)
    except ValueError as x:
        print(x)
    else:
        print(sum)

input(input_num, input_num2)