name = "Alice"
age = 20
weight = 65.5
likeCoding = True
foods = ["pizza","sushi","pasta","tacos"]
Location = ("Paris","France")
Info = {"goal" : "learn code", "dream_job" : "software engineer"}
Languages = {"Python","Java","C++"}

print("Name: ", name , " Type: ", type(name))
print("Age: ", age , " Type: ", type(age))
print("Weight: ", weight , " Type: ", type(weight))
print("Likes Coding: ", likeCoding , " Type: ", type(likeCoding))
print("Foods: ", foods , " Type: ", type(foods))
print("Location: ", Location , " Type: ", type(Location))
print("Info: ", Info , " Type: ", type(Info))
print("Languages: ", Languages , " Type: ", type(Languages))

foods.append("salad")
print("Updated Foods: ", foods)

print(Info.get("dream_job"))

Languages.add("Javascript")
print("Updated Languages: ", Languages)


