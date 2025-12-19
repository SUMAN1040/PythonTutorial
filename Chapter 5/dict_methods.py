marks = {
    "Suman": 100, 
    "Suman": 10,
    "Kumar": 90,
    "Dey": 95,
    0: "Suman"
}
# print(marks.items())
# print(marks.keys())
# print(marks.values())
# marks.update({"Suman": 400,  "Auman": 4567})
# print(marks)

print(marks.get("Suman")) # prints none
print(marks["Suman"]) # KeyError if key not found
