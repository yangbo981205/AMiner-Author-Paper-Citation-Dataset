import linecache


file_path = r'F:\暑期实训\原始数据\AMiner-Paper.txt'
with open(r'Dataset/Paper.txt', 'w', encoding='UTF-8') as f_paper:
    i = 1
    while True:
        one_line = linecache.getline(file_path, i).strip('\n')
        if one_line[0:6] == '#index':
            two_line = linecache.getline(file_path, i+1).strip('\n')
            three_line = linecache.getline(file_path, i+2).strip('\n')
            data = one_line[7:]+'--'+two_line[3:]+'--'+three_line[3:]+'\n'
            # print(data)
            f_paper.write(data)
        i = i+1
        if (i-1) % 10000 == 0:
            print("执行到第{}行".format(i-1))
        if one_line == '' and linecache.getline(file_path, i+1).strip('\n') == '':
            f_paper.close()
            break

