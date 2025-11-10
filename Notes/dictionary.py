#IC dictionary 1st notes

#Key parts

person ={
    #key:value
    "name":"Xavier",
    "age":22,
    "job":"Maverick",
    "sibling": ["Alex","Katie","Andrew","Vienna","Tia","Treyson","Jake"]
}

print(f"Name is {person["name"]}")
print(person.keys())
for key in person.keys():
    if key == "sibling":
        for name in key:
            print(f"{person['name']} has a sibling named {name}")
    else:
        print(f"{key} is {person[key]}")