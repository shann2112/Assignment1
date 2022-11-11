with open('4654605.txt') as f:
    while True:
        line = f.readline()
        if not line:
            break
        print(line.strip())
