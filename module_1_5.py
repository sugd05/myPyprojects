immutable_var = 1,2,3,'gemini',6,False
print(immutable_var)
print(type(immutable_var))
#immutable_var.extend([4]) # кортежи не свойственны изменению
print(immutable_var)
mutable_list = ['84.7', 451, 'Backspace',88 ]
print(mutable_list)

print(mutable_list[0])
print(type(mutable_list[0]))
mutable_list.extend([2])
print(mutable_list)