print("#1------------")
hi = "HelloW"
text = "fernan"
print(hi + " " + text)
print("#2------------")
hi1 = "HeLLO"
text1 = "ferns"
cap = text1.capitalize()
small = hi1.casefold()
print(small + " " + cap + " Monton")
print("#3------------")
text2 = "fernan mari"
upper = text.upper()
age = "age: {l}"
school = "School: {}".format("Ateneo de Davao University")
print(upper + " " + age.format(l = 23))
print(school)
print("#4------------")
cnt = "eating, eat food"
cnt2 = cnt.count("eat")
print(cnt.count("eat", 3, 13))
print(cnt2)
print("#5------------")
print("t\te\tx\tt".expandtabs(1))
print("#6------------")
tup = (hi, text, "Monton")
j = "!".join(tup)
word = "Asta Software"
print(j + " \ncompany:" + word.ljust(20, "s"))
print("#7------------")
replace = {108: 103}
rep = "lod of war vs "
txt = "Xeus"
sub = txt.maketrans("X", "Z")
print(rep.translate(replace) + txt.translate(sub))
