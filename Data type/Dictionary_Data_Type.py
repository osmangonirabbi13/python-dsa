student_details = {'name' : "osman",
                   'city' : "feni" ,
                   'country' : " Bangladesh"}

print(student_details)
print(type (student_details))

## Dictionary constructor methods

deict1 = dict(name = "osman" , age=10 , hi = "love")

print(deict1.keys())
print(deict1.values())
print(deict1.items())

deict1["country"] = "Bangladesh"
print(deict1)

del deict1["country"]

print(deict1)