

with open(r'Dataset/CheckPaper.txt', 'r', encoding='UTF-8') as f_cp:
    with open(r'Dataset/CheckPaperIsCCF_A.txt', 'w', encoding='UTF-8') as f_cp_is:
        for line in f_cp:
            line_message = line.strip('\n')
            check = line.strip('\n').split('--')[3]
            # print(check)
            if check == 'Yes':
                f_cp_is.write(line_message+'\n')


