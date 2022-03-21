import random
print("#1------------")
num = 5
print(num, "=", type(num))
print("#2------------")
num2 = float(3)
num3 = 5
conv = format(num3, '.3f')
print(num2, conv)
print("#3------------")
x = 5
num4 = complex(x)
print(num4, "=" , type(num4), complex(3))
print("#4------------")
num6 = "54"
num7 = int(num6)
print(num6, "=", type(num6), num7, "=", type(num7))
print("#5------------")
hexnum=0x12 #hex
print(hexnum)
print("#6------------")
num8 = random.randrange(1, 11)
if num8 > 5:
    converted = float(num8)
    print(converted, "=" , type(converted))
else:
    converted2 = str(num8)
    print(converted2, "=" , type(converted2))
print("#7------------")
arr = [1, 2, 3, "Fern"]
num9 = len(arr)
rand = random.randrange(2, 6)
if num9 <= rand:
    print(num9, "<=", rand)
else:
    print(num9, ">", rand)
