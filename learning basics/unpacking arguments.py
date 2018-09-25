def health_score(age, apples, cigs):
    score = 100 - age + apples * 3 - cigs * 5
    print(score)


data1 = [18, 5, 0]
data2 = [30, 5, 3]

health_score(*data1)
health_score(*data2)

