

with open(r'Dataset/Paper.txt', 'r', encoding='UTF-8') as f_paper:
    with open(r'Dataset/CCF_A_ALL.txt', 'r', encoding='UTF-8') as f_ccf_a:
        with open(r'Dataset/CheckPaper.txt', 'w', encoding='UTF-8') as f_result:
            ccf_message = f_ccf_a.read()
            result = ''
            count = 1
            for line in f_paper:
                message = line.strip('\n')
                list_message = list(message.split('--'))
                # print(list_message)
                if list_message[1] in ccf_message:
                    result = message + '--' + 'Yes' + '\n'
                else:
                    result = message + '--' + 'No' + '\n'
                f_result.write(result)
                count = count + 1
                if (count - 1) % 10000 == 0:
                    print("执行到第{}行".format(count - 1))



