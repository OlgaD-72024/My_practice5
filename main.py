immutable_var = 1,2,3,"ball", "umbrella", True
print(immutable_var)
# immutable_var[0] = "sun"
# print(immutable_var) # ошибка - неизменяемый объект
mutable_list = ["sun", "ball", "umbrella"]
mutable_list[1] = "glasses"
print(mutable_list)