def add(x):
    listt1=[ {
    "name":"Kanat",
    "last_name":"Erbolov",
    "Age":20},
    {"name":"Askar",
     "last_name":"Erzhanov",
     "Age":15},
    {"name":"Kairat",
     "last_name":"Zhandosov",
     "Age":45}
]
    listt1.append(x)
    return listt1

print(add({"name":"Aslan",
           "last_name":"Askarovich",
           "Age":"19"}))
