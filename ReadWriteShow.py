

f = open("kroA150.tsp", "r")
print(f.read())
f = open("kroB150.tsp", "r")
print(f.read())

with open("kroA150.tsp") as f:
    with open("kroA150-out.csp", "w") as f1:
        for line in f:
            f1.write(line)

with open("kroB150.tsp") as f:
    with open("kroB150-out.csp", "w") as f1:
        for line in f:
            f1.write(line)
