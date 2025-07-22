my_dict = {}
my_dict = {1:"apple", 2:"ball" }
my_dict = {"name": "liza", 1:[2,4,3] }
my_dict = {"name": "Talika", "age": "10"}
print(my_dict["name"])
print(my_dict.get("age"))
my_dict["age"] = 11
print(my_dict)
my_dict["address"] = "Wonderland"
print(my_dict)
my_dict.pop("age")
print(my_dict)
print("Address :", my_dict.get("address"))
my_dict.clear()
print(my_dict)