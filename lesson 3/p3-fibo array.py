fibo = [0, 1]

counter = 2
while counter < 20:
    res = fibo[counter-1] + fibo[counter-2]
    fibo.append(res)

    counter += 1

print(fibo)

