

with open(r'Dataset/test.txt', 'r', encoding='UTF-8') as f:
    for i in range(3):
        for line in f:
            print(line.strip('\n'))
        else:
            f.seek(0)





