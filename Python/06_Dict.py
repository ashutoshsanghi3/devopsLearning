#Dictionary is like a hash map
person = {
    "first name":"Ashutosh",
    "uid":291197,
    "years":[2024,2025],
    "skills":{
        "backend_tech":["nodejs","expressjs"],
        "databases":["mysql","postgress","h2"]
    }}
# print(len(person))
# print(person.get("skills").get("databases"))

# person["address"]="ganganagar"
# print(len(person))
# print("address" in person) #Check if something is there in dictionary
# print(person.pop("address")) #Remove and return the key value in dictionary
# print(len(person))
# del person["years"] #del is applied for anything like list,dict ,etc. and it deletes the element
# print(len(person))

# print(person["skills"]["databases"])
# person["skills"]["databases"].append("mongodb")
# print(person["skills"]["databases"])

# print(person.items()) # return each item in a dictionary, as tuples in a list.
# person_copy=person.copy()
# del person
# print(person_copy)
# print(person_copy.keys())
# print(person_copy.values())
# keys=person_copy.keys()
# for i in keys:
#     print(person_copy[i])