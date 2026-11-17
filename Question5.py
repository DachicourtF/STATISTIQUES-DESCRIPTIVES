temperatures = [22, 22.6, 21.1, 21.9, 18.3, 18.7, 21.7, 21.1, 23.6, 27.4,
                25.1, 24.9, 23.7, 28.9, 23.2, 26.1, 26.1, 29.8, 28.2,
                28.7, 25.9, 26.7, 30.3, 25.2, 21.8, 22, 20.9, 20.7,
                20.6, 19.5, 18.8]

minimum = 30.3
maximum = 18.3

for i in range(31):
    temp = temperatures[i]

    if temp < minimum:
        minimum = temp

    if temp > maximum:
        maximum = temp

etendue = maximum - minimum

print(etendue)