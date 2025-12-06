# 5-misol
text = input("Matn kiriting: ")

i = 1
for char in text:
    print(f"{i} - {char}")
    i += 1

# 6-misol
name = input("Ism kiriting: ")

if len(name) <= 2:
    print(name)
else:
    masked = name[0] + "X" * (len(name) - 2) + name[-1]
    print(masked)

# 7-misol
my_tuple = ("a", "b", "c", "d")
temp = []
for i in range(len(my_tuple)):
    temp.append((i, my_tuple[i]))
result = tuple(temp)
print(result)
