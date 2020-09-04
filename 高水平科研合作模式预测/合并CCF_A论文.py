

with open(r'Dataset/CCF_A_ALL.txt', 'w', encoding='UTF-8') as f_all:
    message_all = ''
    for i in range(85):
        print("正在合并第{}个文件".format(i+1))
        file_one = open(r"CCF_A/CCF-A" + str(i+1) + ".txt", "r", encoding='UTF-8')
        message_one = file_one.read()
        message_all = message_all + message_one
    f_all.write(message_all)
    f_all.close()
