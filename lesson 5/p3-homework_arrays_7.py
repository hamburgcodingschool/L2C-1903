names = ["Martha", "Chris", "Joe", "Anthony", "Roberta", "Hall", "Donald"]

for i in range(0, len(names)):
    if i % 2 == 1:
        print("{}: {}".format(i, names[i]))