import linecache


file_path = r'F:\暑期实训\原始数据\AMiner-Author.txt'
with open(r'Dataset/Author.txt', 'w', encoding='UTF-8') as f_author:
    i = 1
    while True:
        index = linecache.getline(file_path, i).strip('\n')
        author = linecache.getline(file_path, i+1).strip('\n')
        write_str = index[7:] + '--' +author[3:] + '\n'
        # print(write_str)
        f_author.write(write_str)
        i = i+10
        if (i-1) % 100000 == 0:
            print(i-1)
        if index == '' and author == '':
            f_author.close()
            break




