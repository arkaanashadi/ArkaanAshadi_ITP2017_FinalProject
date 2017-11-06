import random

temp = [0] + [x for x in range(1, 11)] + [11]
temp2 = [x for x in range(11, 21)]
temp3 = temp+temp2
temp4 = [0] + [x for x in range(1, 11)]

inside = [[1,1,2], [1,3,4]]

num = 1
num2 = 3

print(temp[-1:])
print([num] + [num2])
print(temp2)
print(temp3)
print(random.choice(temp3))
print(temp4[1:-1])
print(random.choice(random.choice(inside)))

