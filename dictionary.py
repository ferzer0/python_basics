print("#1----------------")
pets = {
    "dog": "Husky",
    "cat": "Persian",
    "bird": "Macaw",
}
print(pets)
print("#2----------------")
val = ("number", "number2")
arr = [1]
arr.append(3)
assign = dict.fromkeys(val, arr)
print(assign,)
print("#3----------------")
search = input("Available: fruit, soup, appetizer \n Search:").casefold()
food = {
    "fruit": ["mango", "apple"],
    "soup": "Sinigang",
    "appetizer": "Spaghetti",
}
get_food = food.get(search)
if search == "fruit" or "soup" or "appetizer":
    print("Availalbe: ", get_food)
print("#4----------------")
mydata = {
    "Name": "fernan mari montOn",
    "School": "addU",
    "year": 1998,
}
mydata.pop("year")
get_name = mydata.get("Name")
get_school = mydata.get("School")
print(mydata)
print(get_name.title(), get_school.upper())
print("#5----------------")
enter_model = input("What model you would like to get?").capitalize()
laptop = {
    "brand": "HP",
    "year": 2017,
}

ship = laptop.setdefault("model", enter_model)
print("Your HP", ship, "will be shipped soon \n Detail:", laptop)
print("#6----------------")
laptop = {
    "brand": "HP",
    "model": "Omen",
    "year": 2017,
}
get_model = laptop.get("model")
if get_model == "Omen":
    laptop.update({"model": "Pavillion"})
    get_new_model = laptop.get("model")
    print(get_new_model)
print("#7----------------") #if maka add
laptop2 = {
    "brand": "HP",
    "model": "Omen",
    "year": 2017,
}

get_value = laptop2.values()
print(get_value)
