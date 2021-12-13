

v = float(input("vazn ra vard kon(kg)"))

g = float(input("gad ra vard kon(m)"))

h = (g / 100)

mbi = v / (h * h)

if mbi < 18.5: 
    result = "underweight"

if 18.5 <= mbi >= 24.9: 
    result = "normal"

if 25 <= mbi >= 29.9: 
    result = "overweight"

if 30 <= mbi >= 34.9: 
    result = "obese"

if 35 < mbi: 
    result = "extremely obese"

print (result)
