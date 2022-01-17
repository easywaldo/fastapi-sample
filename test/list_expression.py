def greaterThan(value, other):
   return value > other

def isOddNumber(value):
  return value % 2 == 0

list = [1,2,3]
list2 = list


list.insert(0, 100)
print(list)
print(list2)

list3 = list2.copy()

list2.insert(0, 201)

print(list2)
print(list3)



result = [i for i in list3 if greaterThan(i, 50) and not isOddNumber(i)]
result2 = [i for i in list3 if greaterThan(i, 50) and isOddNumber(i)]

print(result)
print(result2)