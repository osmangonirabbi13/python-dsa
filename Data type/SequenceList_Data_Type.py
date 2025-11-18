students = ["osman" , "goni" , "rabbi" , "hello"]
print(students)
print(type(students))
#########
list2 = list(students)
print(list2)
############
list3 = list("osman goni")
print(list3)
##########
list4 = [1,2,3,4]
list4.append(5)
print(list4)
############
list4.insert(2,10)
print(list4)
##########

list5 = [1,2,3,4]
list6 = [5,6,7,8]
list5.extend(list6)
print(list5)

arr =[1,2,3,4,5,6]
arr.remove(3)
print(arr)

arr1 = [1,2,3,4,5]
arr1.pop(2)
print(arr1)

arr1[1:3] = 10,20,30
print(arr1)


arr1.reverse()
print(arr1)

ls1 = [5,6,4,1,2,3]

ls1.sort()
print(ls1)