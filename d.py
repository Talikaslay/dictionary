my_dict = {}
my_dict = {1:"number", 2:"range- 1-10" }
my_dict = {"name": "liza", 1:[1,5,10] }
my_dict = {"name": "Talika", "number": "10"}
print(my_dict["name"])
print(my_dict.get("number"))
my_dict["age"] = 11
print(my_dict)
my_dict["address"] = "math"
print(my_dict)
my_dict.pop("number")
print(my_dict)
print("Address :", my_dict.get("address"))
my_dict.clear()
print(my_dict)