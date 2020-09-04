

with open(r'F:\暑期实训\原始数据\AMiner-Paper.txt', 'r') as f_author:
    count = 0
    for line in f_author:
        print(line)
        count = count+1
        if count > 100:
            break


