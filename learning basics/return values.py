def allowed_dating_age(my_age):
    girls_age = my_age * 3 / 4 + 2
    return girls_age


for age in range(13, 31):
    print("age =", age, "limit =", allowed_dating_age(age))
